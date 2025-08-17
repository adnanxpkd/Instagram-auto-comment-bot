import random

# Delays (in seconds)
MIN_DELAY = 5
MAX_DELAY = 15
PAGE_LOAD_TIMEOUT = 10

# Max comments to post
MAX_COMMENTS = 20

# Comment file path
COMMENTS_FILE = "../data/comments_list.txt"

# Target post
def get_target_url():
    from config.credentials import TARGET_POST_URL
    return TARGET_POST_URL
