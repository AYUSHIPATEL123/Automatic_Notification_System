# 🚀 Developer Learning Assistant

A Python-based desktop application that helps developers learn keyboard shortcuts daily through Windows notifications.

The application scrapes shortcut keys from websites, stores them in a SQLite database, and automatically displays notifications using Windows Task Scheduler.

---

## ✨ Features

* 🔔 Daily Windows notifications
* ⌨️ Learn keyboard shortcuts automatically
* 🌐 Web scraping with BeautifulSoup
* 🗄️ SQLite database storage
* ⏰ Automatic scheduling with Windows Task Scheduler
* 📊 Tracks shortcut usage with `show_count`
* 🐍 Built entirely with Python

---

## 🛠️ Tech Stack

* Python 3.11+
* SQLite3
* Selenium
* BeautifulSoup4
* Plyer
* Windows Task Scheduler

---

## 📂 Project Structure

```text
DeveloperLearningAssistant/
│
├── database/
│   ├── db.py
│   └── learning.db
│
├── scrapers/
│   └── shortcuts.py
│
├── notifications/
│   └── shortcut_notification.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/DeveloperLearningAssistant.git
cd DeveloperLearningAssistant
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install selenium beautifulsoup4 plyer
```

---

## 🗄️ Database Setup

Create the database:

```bash
python database/db.py
```

This file run creates:

```text
database/learning.db
```

---

## 🌐 Scrape Keyboard Shortcuts

Run:

```bash
python scrapers/shortcuts.py
```
This fetches shortcut keys from websites and stores them in the SQLite database.

---

## 🔔 Test Notification

Run:

```bash
python notifications/shortcut_notification.py
```

You should receive a notification like:

```text
Today's Shortcut

Ctrl + Shift + Esc
Open Windows Task Manager
```

---

## ⏰ Automate with Windows Task Scheduler

#### go in Create Basic Task in Task Scheduler App

### Program/Script

```text
D:\path\to\project\.venv\Scripts\pythonw.exe
```

> `pythonw.exe` runs Python without opening a command prompt.

### Add Arguments

```text
D:\path\to\project\notifications\shortcut_notification.py
```

### Start In

```text
D:\path\to\project
```

### Trigger

* Daily
* Set your preferred time (e.g., 9:00 AM)

---

## 📊 Database Schema

```sql
CREATE TABLE TASKS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category Text NOT NULL,
            title TEXT NOT NULL,  
            description TEXT NOT NULL,
            source TEXT,
            show_count INTEGER DEFAULT 0,
            create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(category,title)
) ;
```


## 👩‍💻 Author

**Ayushi Patel**

⭐ If you like this project, please give it a star on GitHub!
