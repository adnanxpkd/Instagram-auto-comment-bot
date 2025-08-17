````markdown
# 🤖 Instagram Auto Comment Bot

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen)](https://www.python.org/)
[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red)]()

Automate your Instagram comments with style ⚡.  
This bot listens for posts and automatically comments with predefined or AI-powered replies.  
Perfect for engagement, campaigns, or just having fun 😎.

---

## ✨ Features

- 🔄 **Auto-comment** on posts (by username, hashtags, or feed)  
- 🎯 **Smart reply system** (randomized comments / AI-generated text)  
- 🔒 **Session-based login** (no repeated logins)  
- 📦 **Lightweight & Easy to Deploy** (run locally or on cloud 24/7)  
- 🛡️ **Safety Controls** – delay system to avoid spam flags  

---

## 📸 Demo

![Demo Bot](https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif)

---

## ⚡ Tech Stack

- [Python 3.9+](https://www.python.org/)  
- [Instagrapi](https://github.com/adw0rd/instagrapi) (Instagram private API)  
- [SQLite](https://www.sqlite.org/) for storing sessions  
- Optional: [OpenAI](https://platform.openai.com/) / [Gemini](https://ai.google.dev/) for AI comments  

---

## 🚀 Quick Start

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/adnanxpkd/Instagram-auto-comment-bot.git
cd Instagram-auto-comment-bot
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add Config

Edit `config.json`:

```json
{
  "username": "your_username",
  "password": "your_password",
  "comments": [
    "🔥 Awesome!",
    "💯 Keep it up!",
    "🚀 Amazing post!"
  ],
  "delay": 60
}
```

### 4️⃣ Run the Bot

```bash
python bot.py
```

---

## ☁️ Deploy 24/7

You can keep the bot running 24/7 with:

* [Railway](https://railway.app/)
* [Render](https://render.com/)
* [Koyeb](https://koyeb.com/)
* [Heroku](https://heroku.com/) (with worker dyno)

👉 Or use **GitHub Actions** to auto-run on schedule.

---

## 📂 Project Structure

```
Instagram-auto-comment-bot/
│── bot.py              # Main bot logic
│── config.json         # User settings (edit this)
│── requirements.txt    # Python dependencies
│── utils.py            # Helper functions
│── LICENSE             # MIT License
│── README.md           # You’re here
```

---

## ⚠️ Safety Notes

* Use test accounts first ⚡
* Don’t spam → Instagram bans are real
* Add delays between actions (`delay` in config)
* Use responsibly 🙏

---

## 📊 Roadmap

* [ ] Add hashtag-based auto-comment
* [ ] Support AI comment generator (OpenAI/Gemini)
* [ ] Docker setup for easier deployment
* [ ] Web UI dashboard

---

## 🤝 Contributing

PRs are welcome!

1. Fork it 🍴
2. Create your branch 🌱
3. Commit changes ✅
4. Open PR 🚀

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

💡 *Made with ❤️ by [Adnan](https://github.com/adnanxpkd)*
