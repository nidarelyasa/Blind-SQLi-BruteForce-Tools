# Blind SQL Injection – Conditional Responses

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Burp Suite](https://img.shields.io/badge/Burp%20Suite-Proxy-orange.svg)](https://portswigger.net/burp)
[![PortSwigger](https://img.shields.io/badge/PortSwigger-Web%20Security%20Academy-green.svg)](https://portswigger.net/web-security)
[![SQL Injection](https://img.shields.io/badge/SQL%20Injection-Boolean--Based-red.svg)](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses)

> **🎯 Hands-on SQL Injection Practice!**  
> A Python-based automation project for practicing **Boolean-Based Blind SQL Injection** using conditional HTTP responses.

This project is developed as part of my hands-on learning experience with [PortSwigger Web Security Academy](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses).

The project demonstrates how SQL injection conditions can be evaluated by analyzing differences in HTTP responses, with Python automation and Burp Suite Proxy integration.

## 📖 Table of Contents

- [Quick Start](#-quick-start)
- [Lab Information](#-lab-information)
- [Project Structure](#-project-structure)
- [Scripts](#-scripts)
- [How It Works](#-how-it-works)
- [Architecture & Workflow](#-architecture--workflow)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Burp Suite Proxy Configuration](#-burp-suite-proxy-configuration)
- [Python Proxy Configuration](#-python-proxy-configuration)
- [Execution](#-execution)
- [Dependencies](#-dependencies)
- [Learning Objectives](#-learning-objectives)
- [Limitations](#-limitations)
- [Disclaimer](#-disclaimer)
- [Author](#-author)

## 🚀 Quick Start

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/nidarelyasa/Blind-SQLi-BruteForce-Tools.git
cd Blind-SQLi-BruteForce-Tools
pip install -r requirements.txt
```

**Run the connection test:**

```bash
python test_connection.py
```

**Execute the main script:**

```bash
python exploit.py "https://YOUR-LAB-ID.web-security-academy.net/"
```

Make sure Burp Suite is running and the Proxy Listener is active before executing the main script.

## 📋 Lab Information

| Category | Details |
|---|---|
| Platform | PortSwigger Web Security Academy |
| Lab | Blind SQL Injection with Conditional Responses |
| Vulnerability | Boolean-Based Blind SQL Injection |
| Language | Python 3 |
| HTTP Client | Requests |
| Proxy | Burp Suite |
| Testing Environment | VS Code Terminal |

## 📁 Project Structure

```text
Blind-SQLi-BruteForce-Tools/
│
├── exploit.py
├── test_connection.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🛠️ Scripts

### 1. `test_connection.py`

A connectivity testing script used to verify communication with the PortSwigger lab.

**Features:**

- Sends an HTTP GET request to the lab.
- Checks the HTTP response status code.
- Checks the availability of TrackingId and session cookies.

### 2. `exploit.py`

The main Python automation script for practicing Boolean-Based Blind SQL Injection.

**Features:**

- Sends HTTP requests through Burp Suite Proxy.
- Injects SQL conditional statements into the TrackingId cookie.
- Analyzes HTTP responses to identify true or false conditions.
- Demonstrates character-by-character password extraction in the authorized lab environment.

## ⚙️ How It Works

The automation follows these steps:

1. Establishes HTTP communication with the PortSwigger lab.
2. Routes HTTP requests through Burp Suite Proxy.
3. Modifies the TrackingId cookie with SQL conditions.
4. Analyzes HTTP responses to identify conditional results.
5. Uses SQL functions such as `SUBSTRING()` and `ASCII()` to test individual characters.
6. Demonstrates character-by-character password extraction.

**The application response acts as a Boolean indicator:**

| Condition | HTTP Response |
|---|---|
| TRUE | The expected welcome message appears. |
| FALSE | The expected welcome message does not appear. |

## 🏗️ Architecture & Workflow

The following diagram illustrates how the Python automation script communicates with the PortSwigger lab through Burp Suite Proxy.

```text
Python Script (VS Code Terminal)
             |
             v
      HTTP Proxy Request
        127.0.0.1:8080
             |
             v
         Burp Suite
       Proxy Listener
             |
             v
    PortSwigger Web Security
         Academy Lab
             |
             v
    HTTP Response Analysis
             |
             v
  Password Character Extraction
```

## 📋 Requirements

**Required Software:**

- **Python:** Version 3.x
- **Burp Suite:** Community or Professional
- **Visual Studio Code:** For running Python scripts
- **PortSwigger Web Security Academy:** An active lab instance

## 📦 Installation

**Step 1 - Clone the repository**

```bash
git clone https://github.com/nidarelyasa/Blind-SQLi-BruteForce-Tools.git
cd Blind-SQLi-BruteForce-Tools
```

**Step 2 - Install dependencies**

```bash
pip install -r requirements.txt
```

## 🔒 Burp Suite Proxy Configuration

Before running the main Python script:

1. Open Burp Suite.
2. Navigate to **Proxy → Proxy settings**.
3. Ensure the Proxy Listener is active.
4. Configure the listener:

```text
Host: 127.0.0.1
Port: 8080
```

5. Keep Burp Suite running while executing the Python script.
6. Intercept can remain OFF. Requests will still appear in HTTP History.

## 🌐 Python Proxy Configuration

The main script uses the following proxy configuration:

```python
PROXIES = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}
```

This routes HTTP and HTTPS requests through Burp Suite, allowing requests and responses to be inspected in HTTP History.

## ▶️ Execution

### Step 1 - Test Lab Connectivity

Run the connection testing script:

```bash
python test_connection.py
```

This checks basic HTTP connectivity with the configured PortSwigger lab.

### Step 2 - Run the Main Script

Make sure Burp Suite is running and the Proxy Listener is active.

Execute:

```bash
python exploit.py "https://YOUR-LAB-ID.web-security-academy.net/"
```

Replace the example URL with your own active lab URL.

### Step 3 - Monitor HTTP Traffic

Open:

```text
Burp Suite → Proxy → HTTP History
```

Monitor the HTTP requests generated by the Python script.

## 📚 Dependencies

The project uses:

- `requests` – HTTP request handling.
- `urllib3` – HTTP connection utilities.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## 🎓 Learning Objectives

Through this project, the following concepts can be explored:

- Understand Boolean-Based Blind SQL Injection.
- Learn conditional SQL injection techniques.
- Practice HTTP cookie manipulation.
- Automate security testing using Python.
- Understand HTTP proxy integration with Burp Suite.
- Analyze application responses during security testing.

## ⚠️ Limitations

- Designed specifically for the PortSwigger conditional response lab.
- Requires an active lab instance and valid session cookies.
- Uses a predefined character range and maximum extraction length.
- HTTPS certificate verification is disabled for the controlled lab environment.

## 🛡️ Disclaimer

This project is intended strictly for educational purposes and authorized security testing within controlled environments, particularly PortSwigger Web Security Academy labs.

Do not use these techniques against systems without explicit authorization.

## 👨‍💻 Author

**Nidar Elyasa**

GitHub: [@nidarelyasa](https://github.com/nidarelyasa)
Email: nidarelyasa5@gmail.com

---

⭐ **If you find this project helpful, please give it a star!**
