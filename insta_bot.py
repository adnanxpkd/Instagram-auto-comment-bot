from instabot import Bot
import os
import time
from dotenv import load_dotenv

# Load env variables
load_dotenv()

USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
POST_LINK = os.getenv("POST_LINK")

# Keywords & replies
REPLY_KEYWORDS = {
    "hi": "Hey! Thanks for commenting 😎",
    "hello": "Hello there! 👋",
    "awesome": "Glad you liked it! 💯"
}
DEFAULT_REPLY = "Thanks for your comment! 😊"

# Login
bot = Bot()
bot.login(username=USERNAME, password=PASSWORD)

# Get media ID
media_id = bot.get_media_id_from_link(POST_LINK)

# Main loop
while True:
    comments = bot.get_media_comments_all(media_id)
    for comment in comments:
        comment_text = comment['text'].lower()
        comment_id = comment['pk']

        # Skip if already replied
        replies = bot.get_comment_replies(comment_id)
        if replies:
            continue

        # Keyword reply
        replied = False
        for keyword, reply_text in REPLY_KEYWORDS.items():
            if keyword in comment_text:
                bot.reply_to_comment(comment_id, reply_text)
                replied = True
                break

        if not replied:
            bot.reply_to_comment(comment_id, DEFAULT_REPLY)

        time.sleep(5)  # avoid spam detection

    # Sleep before checking new comments
    time.sleep(60)
