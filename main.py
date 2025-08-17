from selenium.webdriver.common.by import By
from config.settings import MAX_COMMENTS, get_target_url
from config.credentials import USERNAME
from utils.stealth import create_stealth_driver
from utils.login import login
from utils.comments import post_comment
from selenium.webdriver.support.ui import WebDriverWait
import time
import random

def main():
    print(f"🚀 Instagram Auto Comment Bot (User: {USERNAME})\n")

    driver = create_stealth_driver()
    wait = WebDriverWait(driver, 10)

    try:
        # Login
        if not login(driver, wait):
            print("❌ Unable to log in. Exiting.")
            return

        # Go to target post
        target_url = get_target_url()
        driver.get(target_url)
        time.sleep(3)

        posted = 0
        failed_attempts = 0

        while posted < MAX_COMMENTS:
            print(f"\n🔁 Attempting comment #{posted + 1}...")
            if post_comment(driver, wait):
                posted += 1
                delay = random.uniform(5, 15)
                print(f"⏳ Waiting {delay:.1f} seconds before next action...")
                time.sleep(delay)
                failed_attempts = 0
            else:
                failed_attempts += 1
                if failed_attempts >= 3:
                    print("❌ Too many failures. Stopping.")
                    break
                time.sleep(5)

        print(f"\n🎉 Finished! Posted {posted} comments.")

    except Exception as e:
        print(f"💥 Unexpected error: {e}")
    finally:
        print("👋 Closing browser...")
        driver.quit()

if __name__ == "__main__":
    main()
