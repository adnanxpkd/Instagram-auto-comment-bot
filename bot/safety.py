import time
import random
from typing import Tuple
import logging

class SafetyManager:
    def __init__(self):
        self.last_action_time = 0
        self.activity_log = []
        
    def get_delay(self, min_delay: float = 3.0, max_delay: float = 7.0) -> float:
        """Random delay with human-like variance"""
        delay = random.uniform(min_delay, max_delay)
        self._log_activity(f"Delay: {delay:.2f}s")
        time.sleep(delay)
        return delay
        
    def human_type(self, element, text: str):
        """Human-like typing simulation"""
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.05, 0.2))
        self._log_activity(f"Typed: {text}")
        
    def _log_activity(self, action: str):
        """Track all bot actions"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {action}"
        self.activity_log.append(log_entry)
        logging.info(log_entry)
        
    def emergency_stop(self):
        """Clean shutdown procedure"""
        self._log_activity("EMERGENCY STOP INITIATED")
        # Add cleanup logic here
