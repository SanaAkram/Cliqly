import time
import os
import errno
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException, ElementClickInterceptedException

# Path to Chrome Driver
chromedriver_path = '../OpenAI/chromedriver.exe'  # Replace with your actual driver path if Chrome Driver Library does not work

def login_to_system(driver):
    try:
        driver.get("https://system.cliqly.com")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'loginEmail')))
        driver.find_element(By.ID, 'loginEmail').send_keys("info@xandercon.com.au")
        driver.find_element(By.ID, 'floatingPassword').send_keys("1787496593")
        driver.find_element(By.ID, 'userLoginBtn').click()
        driver.get("https://system.cliqly.com/member/sendmailpro3/")
        time.sleep(10)
        driver.get("https://system.cliqly.com/member/sendmailpro3/schedule")
    except Exception as e:
        print(f"Error occurred while logging in: {e}")
        driver.quit()
        raise


def click_until_success(driver, element, delay=10, max_attempts=None):
    """
    Continuously attempts to click on a given web element until successful.

    Parameters:
    - driver: The web driver instance controlling the browser.
    - element: The web element to be clicked.
    - delay: Time to wait between attempts (default is 10 seconds).
    - max_attempts: Optional maximum number of attempts before giving up. If None, it will keep trying indefinitely.

    Returns:
    - True if the click was successful.
    - False if the maximum attempts were reached without success.
    """
    attempts = 0

    while True:
        try:
            # element = find_element_func()  # Re-find the element each time
            if element:
                element.click()
                print("Element has been clicked successfully!")
                return True
            else: # Exit the function if the click is successful
                driver.get(element)
        except Exception as e:
            driver.execute_script("arguments[0].scrollIntoView();", element)
            print(f"Retrying...")
            attempts += 1
            if max_attempts and attempts >= max_attempts:
                print(f"Maximum attempts ({max_attempts}) reached. Could not click the element.")
                return False
            if attempts > 2000:
                return False# Exit the function if max attempts are reached
            time.sleep(delay)


def schedule_emails(driver, start_time):
    try:
        current_url = driver.current_url
        if not current_url.endswith("/schedule"):
            # If it doesn't, navigate to the URL with '/schedule' added
            driver.get(current_url.rstrip('/') + "/schedule")
        print(driver.current_url)
        # Maximize the browser window
        driver.maximize_window()
        time.sleep(1)
        driver.execute_script("document.body.style.zoom = '33%';")
        # Initialize variable
        openers_data = None
        try:
            openers_data = WebDriverWait(driver, 160).until(EC.presence_of_element_located((By.ID, 'openers_data')))
            if openers_data:
                # time.sleep(6)
                openers_data.clear()
                openers_data.send_keys("20000")
                print("Openers Button has been Clicked!")
        except Exception as e:
            print("Trying to click Openers Button ")
            click_until_success(driver, openers_data, delay=4)
            openers_data.clear()
            openers_data.send_keys("20000")

        # Initialize variable
        next_step_button = None
        try:
            next_step_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'subsTypeBtn')))
            if next_step_button:
                time.sleep(6)
                next_step_button.click()
                print("Next Step Button has been Clicked!")
        except Exception as e:
            if not next_step_button:
                next_step_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'subsTypeBtn')))
            print("Trying to click Next Step Button ")
            click_until_success(driver, next_step_button, delay=4)

        # Initialize variable
        button = None
        creative_box = None
        try:
            # Locate the creative box by its ID
            creative_box = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'creativeBox_1')))

            # Find the button within the creative box
            button = WebDriverWait(creative_box, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-primary.sMailBtn')))
            if button:
                button.click()
                print("Creative Box 1 has been Clicked!")
        except Exception as e:
            if not button:
                time.sleep(4)
                button = WebDriverWait(creative_box, 90).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-primary.sMailBtn')))

            # Call the function to click on the element
            print("Trying to click Creative Box 1")
            click_until_success(driver, button, delay=4)
        track_option = None
        try:
            track_option = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'trackOpt1')))
            if track_option:
                Select(track_option).select_by_visible_text("Enter New Link To Send The Clicks To")
        except Exception as e:
            time.sleep(4)
            Select(track_option).select_by_visible_text("Enter New Link To Send The Clicks To")

        # Initialize variable
        user_url_link = None
        try:
            user_url_link = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, 'user_urlLink')))
            if user_url_link:
                user_url_link.click()
                user_url_link.clear()
                user_url_link.send_keys("https://linktracksystem.biz/?affid=420508&subid=cPRO")
                print("User URL Link has been Set!")
        except Exception as e:
            print("Trying to click URL Link")
            click_until_success(driver, user_url_link, delay=4)
            user_url_link.clear()
            user_url_link.send_keys("https://linktracksystem.biz/?affid=420508&subid=cPRO")
            print("User URL Link has been Set!")

        # Initialize variable
        from_name = None
        try:
            from_name = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, 'fromName')))
            if from_name:
                from_name.click()
                from_name.clear()
                from_name.send_keys("Alex")
                print("From Name has been Set!")
        except Exception as e:
            print("Trying to From Name")
            click_until_success(driver, from_name, delay=4)
            from_name.clear()
            from_name.send_keys("Alex")
            print("From Name has been Set!")

        target_date = datetime.now() + timedelta(days=1)
        target_day = target_date.day
        time.sleep(3)

        # Initialize variable
        date_calender = None
        try:
            date_calender = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#s_date1 .col-md-4:nth-child(1)')))
            if date_calender:
                date_calender.click()
                print("Date Calendar has been Clicked!")
        except Exception as e:
            print("Trying to click Date Calendar")
            click_until_success(driver, date_calender, delay=4)


        # Initialize variable
        date_picker = None
        day_to_select = None
        try:
            time.sleep(1)
            driver.execute_script("document.body.style.zoom = '100%';")
            date_picker = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'ui-datepicker-div')))
            day_to_select = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, f'//a[text()="{target_day}"]')))
            if day_to_select:
                day_to_select.click()
                print("Day to Select has been Clicked!")
        except Exception as e:
            print("Trying to click Day to Select Button")
            click_until_success(driver, day_to_select, delay=4)
        time.sleep(1)
        driver.execute_script("document.body.style.zoom = '33%';")
        # Initialize variable
        hours_select = None
        try:
            hours_select = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, 'hours')))
            Select(hours_select).select_by_visible_text(f"{start_time.hour:02d} hrs")
            print("Hours Select has been Set!")
        except Exception as e:
            if hours_select:
                time.sleep(10)
                Select(hours_select).select_by_visible_text(f"{start_time.hour:02d} hrs")
                print("Hours Select has been Set!")

        # Initialize variable
        minutes_select = None
        try:
            minutes_select = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, 'mins')))
            Select(minutes_select).select_by_visible_text(f"{start_time.minute:01d} mins")
            print("Minutes Select has been Set!")
        except Exception as e:
            if minutes_select:
                time.sleep(10)
                Select(minutes_select).select_by_visible_text(f"{start_time.minute:01d} mins")
                print("Minutes Select has been Set!")

        # Initialize variable
        submit_button = None
        confirm_button = None
        try:
            submit_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'emailAdSubmitformid1')))
            if submit_button:
                submit_button.click()
                print("Submit Button has been Clicked!")
        except Exception as e:
            print("Trying to click Submit Button")
            click_until_success(driver, submit_button, delay=4)
        try:
            confirm_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'formSubmitBtn')))
            confirm_button.click()
            print("Confirm Button has been Clicked!")
        except Exception as e:
            print("Trying to click Confirm Button")
            click_until_success(driver, confirm_button, delay=4)

    except TimeoutException as e:
        print("Timeout occurred while waiting for an element: ", e)
    except NoSuchElementException as e:
        print("Element not found: ", e)
    except ElementClickInterceptedException as e:
        print("Element click intercepted: ")
        return False
    except Exception as e:
        print("Error occurred: ", e)

def generate_schedule(start_time_str, end_time_str, steps):
    start_time = datetime.strptime(start_time_str, "%H:%M")
    end_time = datetime.strptime(end_time_str, "%H:%M")
    total_duration_minutes = (end_time - start_time).total_seconds() / 60
    interval_minutes = total_duration_minutes / steps

    current_time = start_time
    schedule_times = []

    for _ in range(steps):
        schedule_times.append(current_time.time())
        current_time += timedelta(minutes=interval_minutes)

    return schedule_times

def main():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    try:
        driver = webdriver.Chrome(options=options)  # Will automatically get driver from library
    except OSError as err:
        if err.errno == errno.ENOENT:
            raise WebDriverException(
                "'%s' executable needs to be in PATH. %s" % (
                    os.path.basename(chromedriver_path), "Ensure chromedriver is in your PATH.")
            )
        elif err.errno == errno.EACCES:
            raise WebDriverException(
                "'%s' executable may have wrong permissions. %s" % (
                    os.path.basename(chromedriver_path), "Ensure chromedriver has the correct permissions.")
            )

    login_to_system(driver)

    afternoon_schedule = generate_schedule("04:00", "17:20", 200)
    iterate = 110
    for i, schedule_time in enumerate(afternoon_schedule[iterate:], 1):
        print(f"Executing for time: {schedule_time} with Step: {i+iterate}")
        time.sleep(1)
        driver.execute_script("document.body.style.zoom = '33%';")
        schedule_emails(driver, start_time=schedule_time)
        # time.sleep(10)  # Adding delay between scheduling emails to avoid rate limiting or server overload

    driver.quit()

if __name__ == "__main__":
    main()
