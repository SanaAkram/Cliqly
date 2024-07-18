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
chromedriver_path = '../OpenAI/chromedriver.exe'  # Replace with your actual driver path


def schedule_emails(start_time, steps):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

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

    def login_to_system():
        try:
            driver.get("https://system.cliqly.com")
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'loginEmail')))
            driver.find_element(By.ID, 'loginEmail').send_keys("info@xandercon.com.au")
            driver.find_element(By.ID, 'floatingPassword').send_keys("1787496593")
            driver.find_element(By.ID, 'userLoginBtn').click()
        except Exception as e:
            print(f"Error occurred while logging in: {e}")
            driver.quit()

    login_to_system()

    try:
        driver.get("https://system.cliqly.com/member/sendmailpro3/")
        time.sleep(20)
        driver.get("https://system.cliqly.com/member/sendmailpro3/schedule")
        time.sleep(10)

        # Initialize variable
        openers_data = None
        try:
            openers_data = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'openers_data')))
            if openers_data:
                time.sleep(10)
                openers_data.clear()
                openers_data.send_keys("20000")
                print("Openers Button has been Clicked!")
        except Exception as e:
            if openers_data:
                time.sleep(20)
                openers_data.clear()
                openers_data.send_keys("20000")
                print("Openers Button has been Clicked!")

        # Initialize variable
        next_step_button = None
        try:
            next_step_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'subsTypeBtn')))
            if next_step_button:
                time.sleep(20)
                next_step_button.click()
                print("Next Step Button has been Clicked!")
        except Exception as e:
            if next_step_button:
                time.sleep(20)
                next_step_button.click()
                print("Next Step Button has been Clicked!")

        # Initialize variable
        creative_box_1 = None
        try:
            creative_box_1 = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="creativeBox_1"]/div[3]/button')))
            if creative_box_1:
                time.sleep(20)
                creative_box_1.click()
                print("Creative Box 1 has been Clicked!")
        except Exception as e:
            if creative_box_1:
                time.sleep(20)
                creative_box_1.click()
                print("Creative Box 1 has been Clicked!")

        track_option = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'trackOpt1')))
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
            if user_url_link:
                time.sleep(20)
                user_url_link.click()
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
            if from_name:
                time.sleep(20)
                from_name.click()
                from_name.clear()
                from_name.send_keys("Alex")
                print("From Name has been Set!")

        target_date = datetime.now() + timedelta(days=1)
        target_day = target_date.day
        time.sleep(10)

        # Initialize variable
        date_calender = None
        try:
            date_calender = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#s_date1 .col-md-4:nth-child(1)')))
            time.sleep(10)
            if date_calender:
                date_calender.click()
                print("Date Calendar has been Clicked!")
        except Exception as e:
            if date_calender:
                time.sleep(20)
                date_calender.click()
                print("Date Calendar has been Clicked!")

        # Initialize variable
        date_picker = None
        day_to_select = None
        try:
            date_picker = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'ui-datepicker-div')))
            day_to_select = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, f'//a[text()="{target_day}"]')))
            time.sleep(10)
            if day_to_select:
                day_to_select.click()
                print("Day to Select has been Clicked!")
        except Exception as e:
            if day_to_select:
                time.sleep(20)
                day_to_select.click()
                print("Day to Select has been Clicked!")

        # Initialize variable
        hours_select = None
        try:
            hours_select = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, 'hours')))
            Select(hours_select).select_by_visible_text(f"{start_time.hour:02d} hrs")
            print("Hours Select has been Set!")
        except Exception as e:
            if hours_select:
                time.sleep(20)
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
                time.sleep(20)
                Select(minutes_select).select_by_visible_text(f"{start_time.minute:02d} mins")
                print("Minutes Select has been Set!")

        # Initialize variable
        submit_button = None
        confirm_button = None
        try:
            submit_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'emailAdSubmitformid1')))
            if submit_button:
                time.sleep(10)
                submit_button.click()
                print("Submit Button has been Clicked!")
            confirm_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'formSubmitBtn')))
            confirm_button.click()
            print("Confirm Button has been Clicked!")
        except Exception as e:
            if submit_button:
                time.sleep(20)
                submit_button.click()
                print("Submit Button has been Clicked!")
            if confirm_button:
                time.sleep(20)
                confirm_button.click()
                print("Confirm Button has been Clicked!")

    except TimeoutException as e:
        print("Timeout occurred while waiting for an element: ", e)
    except NoSuchElementException as e:
        print("Element not found: ", e)
    except ElementClickInterceptedException as e:
        print("Element click intercepted: ", e)
    except Exception as e:
        print("Error occurred: ", e)
    finally:
        driver.quit()


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
    afternoon_schedule = generate_schedule("04:00", "17:20", 160)

    for i, schedule_time in enumerate(afternoon_schedule, 1):
        print(f"Executing for time: {schedule_time} with Step: {i}")
        schedule_emails(start_time=schedule_time, steps=160)
        time.sleep(10)  # Adding delay between scheduling emails to avoid rate limiting or server overload


if __name__ == "__main__":
    main()
