from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from typing import List, Dict
from .safety import SafetyManager

class InstagramBot:
    def __init__(self, headless: bool = False):
        self.options = ChromeOptions()
        if headless:
            self.options.add_argument("--headless=new")
        self.driver = Chrome(options=self.options)
        self.safety = SafetyManager()
        
    def login(self, username: str, password: str):
        """Secure login with 2FA support"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(self.safety.get_delay())
        
        # Accept cookies if needed
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Allow essential and optional cookies']"))
            ).click()
        except:
            pass
            
        # Fill credentials
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        
        self.safety.human_type(username_field, username)
        self.safety.human_type(password_field, password)
        
        # Login
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(self.safety.get_delay(10, 15))
        
    def reply_to_comments(self, post_url: str, responses: Dict[str, str]):
        """Smart comment reply system"""
        self.driver.get(post_url)
        time.sleep(self.safety.get_delay(5, 8))
        
        # Load all comments
        self._load_all_comments()
        
        # Get new comments
        comments = self._get_unreplied_comments()
        
        for comment in comments:
            reply = self._generate_reply(comment.text, responses)
            if reply:
                self._post_reply(comment, reply)
                
    def _load_all_comments(self):
        """Scroll to load all comments"""
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.safety.get_delay(2, 4))
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
