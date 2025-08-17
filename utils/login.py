import os
import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.credentials import USERNAME, PASSWORD

COOKIE_FILE = "cookies.pkl"

def login(driver, wait):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    # Check if cookies exist
    if os.path.exists(COOKIE_FILE):
        try:
            cookies = pickle.load(open(COOKIE_FILE, "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            time.sleep(3)
            if "login" not in driver.current_url:
                print("✅ Logged in using saved session.")
                return True
        except Exception as e:
            print(f"⚠️ Failed to load cookies: {e}")

    print("🔐 Logging in...")

    try:
        # Wait for login inputs
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)

        # Click login button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()

        time.sleep(5)

        # Handle "Save Info" and "Turn on Notifications" popups
        try:
            not_now = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not now')]")))
            not_now.click()
            time.sleep(2)
        except:
            pass

        try:
            not_now2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
            not_now2.click()
            time.sleep(2)
        except:
            pass

        # Save cookies
        pickle.dump(driver.get_cookies(), open(COOKIE_FILE, "wb"))
        print("✅ Login successful and session saved.")
        return True

    except Exception as e:
        print(f"❌ Login failed: {e}")
        return False
