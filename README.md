# Cliqly

A Selenium automation bot that **schedules email-campaign sends** in the Cliqly "SendMailPro" web panel, so a whole day's worth of sends can be queued in one run instead of clicking through the form dozens of times.

## What it does

1. Opens a Chrome window and logs in to the Cliqly member area.
2. Opens the SendMailPro **Schedule** page.
3. Generates a list of send times between a start and an end time, evenly spaced (the default is 04:00 → 17:20 split into steps of about 200 minutes — see `generate_schedule`).
4. For each time slot it fills in the scheduling form automatically:
   - sets the number of openers to send to,
   - chooses "Enter new link to send the clicks to" and enters the tracking link,
   - sets the sender name,
   - picks the send **date** (a configurable number of days ahead) and the **hour / minute** for that slot,
   - clicks through the steps and confirms the creative.
5. Retries any click that fails (the panel is slow and elements often are not clickable straight away) and resumes from the failed slot instead of starting over.

## How it works

```
main()
 ├─ webdriver.Chrome()                      (Selenium 4 resolves the driver itself)
 ├─ login_to_system(driver)                 → /member/sendmailpro3/schedule
 ├─ generate_schedule("04:00", "17:20", n)  → list of send times
 └─ for each time:
      schedule_emails(driver, start_time)
        ├─ openers_data  ← number of recipients
        ├─ click "next step" / creative box (click_until_success helpers retry with back-off)
        ├─ choose tracking-link option + enter link, from-name
        ├─ select date (today + N days), hour, minute (Select dropdowns)
        └─ submit → returns False on failure → main() re-runs from that slot
```

The page is zoomed to 33 % in the browser so the long form fits on screen without scrolling.

## Stack

- Python 3.12 (3.9+ should work)
- `selenium` 4.x — browser automation
- Google Chrome
- Other pinned packages are listed in `requirements.txt` (only Selenium is needed by `main.py`)

## Install

```bash
git clone https://github.com/SanaAkram/Cliqly.git
cd Cliqly

python3.12 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt   # or just: pip install selenium
```

macOS quick setup (Homebrew): `brew install python@3.12` then the commands above; PyCharm is optional — open the folder and select the `venv` interpreter.

## Configure

Everything you would tweak lives in `main.py`:

| What | Where |
|---|---|
| Your Cliqly login | `login_to_system()` — **use your own account and keep credentials out of git** (read them from environment variables rather than typing them into the file) |
| Send window and spacing | `generate_schedule("04:00", "17:20", 200)` in `main()` |
| Openers per send | `openers_data.send_keys("20000")` |
| Tracking link and sender name | inside `schedule_emails()` |
| How many days ahead to schedule | `timedelta(days=3)` in `schedule_emails()` |
| Resume from a later slot | `inter = 0` in `main()` (set to the slot index to skip) |

If Chrome/ChromeDriver is not found, put a matching `chromedriver` on your `PATH` (or point `chromedriver_path` at it).

## Run

```bash
python main.py
```

A Chrome window opens and works through the schedule; the terminal prints each slot as it is queued and ends with a completion message.

## Notes

- This automates a third-party web UI; if Cliqly changes element IDs (`openers_data`, `subsTypeBtn`, `creativeBox_1`, …) the selectors in `main.py` need updating.
- Use only with your own Cliqly account and follow Cliqly's terms and anti-spam rules for the campaigns you schedule.
