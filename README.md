# 🖥️ System Monitor – DevOps Project

![Python](https://img.shields.io/badge/Python-3.14-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A lightweight Python-based system monitoring tool that tracks real-time CPU, RAM, and disk usage. Built as part of my Cloud DevOps learning journey.

---

## 🚀 Features

- 📊 Real-time CPU, RAM, and Disk monitoring
- 📝 Logs data with timestamps (`health.log`)
- ⚠️ Alerts when usage exceeds 80%
- ⏱️ Automated execution via `cron`
- 🐍 Built with Python 3 + `psutil`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core scripting |
| psutil | System metrics |
| Linux (WSL) | Development environment |
| Git & GitHub | Version control |
| Cron | Task automation |

---

## 📁 Project Structure
devops-project/
├── system_monitor.py # Main script
├── health.log # Auto-generated logs
├── requirements.txt # Dependencies
├── .gitignore # Ignored files
└── README.md # Documentation

---

## ⚙️ How to Run

```bash
# Clone the repo
git clone https://github.com/wadood-bangash/devops-project.git
cd devops-project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the script
python system_monitor.py

SAMPLE OUTPUT:
[2026-06-28 20:15:00] CPU: 12% | RAM: 34% | DISK: 28%
✅ Script ran successfully!
