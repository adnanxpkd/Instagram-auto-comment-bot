<h1 align="center">🤖 Instagram Auto Comment Bot (v1)</h1>
<p align="center">
  <i>Automate Instagram comments safely and efficiently.</i><br>
  <b>Python + Selenium + Undetected Chrome</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Selenium-Automation-green?logo=selenium" />
  <img src="https://img.shields.io/badge/Chrome-Stealth-success?logo=googlechrome" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

---

## 📸 Overview

**Instagram Auto Comment Bot v1** is a Python automation tool for posting comments on Instagram posts while mimicking human behavior.

Features:
- Stealth mode with `undetected-chromedriver`  
- Randomized comment delays  
- Cookie-based login persistence  

> ⚠️ **Educational Use Only:** Misuse may violate Instagram's [Terms of Use](https://help.instagram.com/581066165581870).

---

## ✨ Features

| Feature                  | Description                                      |
|---------------------------|--------------------------------------------------|
| 🥷 Undetectable Mode      | Uses `undetected-chromedriver` to avoid detection |
| 💬 Comment Rotation       | Randomly selects comments from a file           |
| ⏱️ Human-like Delay       | Random delay between comments                    |
| 🔐 Encrypted Credentials  | Stores login info securely in `.env`            |
| 💾 Cookie Storage         | Saves sessions to avoid repeated logins         |
| 🧩 Modular Codebase       | Easily extend or modify logic                   |

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/adnanxpkd/Instagram-auto-comment-bot.git
cd Instagram-auto-comment-bot
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file:

```env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
```

> 🔐 Keep this private!

### 4. Add Your Comments

Create a `comments.txt` in `config/`:

```txt
🔥 Amazing content!
🙌 Keep up the great work!
💯 Loved this!
👏 Super insightful!
```

### 5. Run the Bot

```bash
python main.py
```

Default behavior:

1. Loads Instagram in stealth mode
2. Logs in via saved credentials or cookies
3. Navigates to the target post
4. Posts comments with randomized delays

---

## ⚙️ Configuration Options

```python
MIN_DELAY = 5         # Minimum delay in seconds
MAX_DELAY = 12        # Maximum delay in seconds
COMMENT_LIMIT = 10    # Number of comments per run
COMMENTS_FILE = "config/comments.txt"
```

---

## 🗄️ Optional MongoDB Integration

Use MongoDB to store sessions and comment logs:

1. Setup MongoDB Atlas or local MongoDB
2. Add connection string to `.env`:

```env
MONGO_URI=mongodb+srv://username:password@cluster0.mongodb.net/instagram-bot
```

3. Example usage:

```python
from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client["instagram_bot"]

db.comments.insert_one({
    "post_id": "12345",
    "comment": "🔥 Amazing!",
    "timestamp": "2025-08-18 00:00"
})
```

---

## 📁 Project Structure

```
Instagram-auto-comment-bot/
├── config/
│   └── comments.txt      # Comment templates
├── data/
│   └── cookies.pkl       # Saved login sessions
├── utils/
│   ├── login.py          # Login helper
│   └── comment.py        # Comment logic
├── main.py               # Entry point
├── .env                  # Credentials (not committed)
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

---

## 💡 Pro Tips

* Use a **test account**
* Adjust delays to stay under Instagram limits
* Refresh comment list frequently
* Avoid spammy or repetitive comments

---

## 🛠️ Built With

* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [MongoDB](https://www.mongodb.com/) (optional)

---

## 📜 License

MIT License – see [`LICENSE`](LICENSE)

---

## 🙋‍♂️ Contributing

Contributions, bug reports, and feature requests welcome!

```bash
# Fork → Branch → Commit → PR
```

---

## 👨‍💻 Author

Made with ❤️ by [Adnan](https://github.com/adnanxpkd)

```

---

This version:  
- Adds **MongoDB section** for production-ready storage  
- Keeps **professional badges, tables, and structured sections**  
- Maintains **modern, developer-friendly style** with emojis and clear flow  
- Fully compatible with **v1 repo structure**  

If you want, I can also **add clickable “Deploy 24/7” buttons for Render/Railway/Koyeb** so users can literally run it in the cloud without touching the code.  

Do you want me to do that next?
```
