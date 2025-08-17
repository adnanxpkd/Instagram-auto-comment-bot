**README.md**

````markdown
# 📸 Instagram Auto Comment Reply Bot

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Deploy](https://img.shields.io/badge/Deploy-Render%20|%20Railway-orange)](https://render.com/)

An automated **Instagram bot** built with Python that continuously monitors your post and **replies to comments**.  
Customizable, safe-paced, and deployable 24/7 on cloud platforms.

---

## ✨ Features

- 🔑 **Keyword-based replies** – define triggers and custom responses.  
- 📝 **Default fallback reply** – ensures every comment gets attention.  
- 🕒 **Human-like behavior** – built-in delays to reduce spam detection.  
- 🔄 **Continuous monitoring** – checks for new comments every minute.  
- ☁️ **Deploy anywhere** – Render, Railway, PythonAnywhere, or VPS.  

---

## ⚙️ Setup

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

1. Copy `.env.example` → `.env`

   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and add your details:

   ```
   INSTAGRAM_USERNAME=your_username
   INSTAGRAM_PASSWORD=your_password
   POST_LINK=https://www.instagram.com/p/POST_ID/
   ```

⚠️ **Never commit your real credentials** — keep `.env` private.

---

## ▶️ Run Locally

```bash
python insta_bot.py
```

* Logs into Instagram with your credentials
* Fetches comments on the given post
* Replies with keyword-based or default messages
* Loops every minute to catch new comments

---

## ☁️ Deployment (24/7)

### Render / Railway

* Connect your GitHub repo
* Set build command:

  ```bash
  pip install -r requirements.txt
  ```
* Set start command:

  ```bash
  python insta_bot.py
  ```
* Add environment variables:

  * `INSTAGRAM_USERNAME`
  * `INSTAGRAM_PASSWORD`
  * `POST_LINK`

### VPS / Raspberry Pi

Run in background:

```bash
nohup python insta_bot.py &
```

---

## 🔒 Safety Guidelines

* ⏳ Always use delays (`time.sleep()`) to mimic human activity.
* 🧪 Test on a **dummy account** first.
* 🚫 Avoid replying to hundreds of comments instantly.
* 📉 Spread activity across time to prevent account restrictions.

---

## 📂 Project Structure

```
├── insta_bot.py        # Main bot logic
├── requirements.txt    # Dependencies (instabot, python-dotenv)
├── .env.example        # Sample environment variables
└── README.md           # Documentation
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to **fork** this repo and submit a **pull request**.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Built with ❤️ by **Adnan**
📩 Got ideas? Open an [issue](../../issues) or ping me!

---
