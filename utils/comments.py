import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import MIN_DELAY, MAX_DELAY, COMMENTS_FILE

def load_comments():
    try:
        with open(COMMENTS_FILE, 'r', encoding='utf-8') as f:
            comments = [line.strip() for line in f if line.strip()]
        return comments
    except FileNotFoundError:
        print(f"⚠️ Comment file not found: {COMMENTS_FILE}")
        return ["Nice!", "Love this!", "So cool!"]

def post_comment(driver, wait):
    comments = load_comments()
    selected_comment = random.choice(comments)

    try:
        # Wait for comment box
        comment_box = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Add a comment…']"))
        )
        comment_box.click()

        input_field = driver.find_element(By.CSS_SELECTOR, "textarea[aria-label='Add a comment…']")
        input_field.clear()
        input_field.send_keys(selected_comment)

        post_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']:not([disabled])"))
        )
        post_button.click()

        time.sleep(random.uniform(2, 4))  # Wait for comment to post

        print(f"✅ Comment posted: {selected_comment}")
        return True

    except Exception as e:
        print(f"❌ Failed to post comment: {e}")
        return False
