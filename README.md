# Blind SQL Injection – Conditional Responses

A Python-based learning project focused on **Boolean-Based Blind SQL Injection** using conditional HTTP responses.

This project demonstrates how Python can automate SQL injection testing in a controlled environment by analyzing differences in HTTP responses.

Developed as part of my hands-on practice with [PortSwigger Web Security Academy](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses), this project integrates Python Requests with Burp Suite Proxy for HTTP traffic inspection and analysis.

---

## Project Overview

The project focuses on understanding and practicing Blind SQL Injection through conditional responses.

The Python script automates the testing process by sending HTTP requests containing SQL conditions and analyzing the application's responses.

The main objective is to understand how Boolean-based SQL injection works and how Python can be used to automate security testing in a controlled lab environment.

## Lab Information

| Category | Details |
|---|---|
| Platform | PortSwigger Web Security Academy |
| Lab | Blind SQL Injection with Conditional Responses |
| Vulnerability | Boolean-Based Blind SQL Injection |
| Language | Python 3 |
| HTTP Client | Requests |
| Proxy | Burp Suite |
| IDE | Visual Studio Code |

**Lab Reference:**  
[Blind SQL Injection with Conditional Responses](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses)

---

## How It Works

The automation follows these steps:

1. Establishes HTTP communication through Burp Suite Proxy.
2. Sends HTTP requests with modified `TrackingId` cookies.
3. Tests SQL conditions against the lab application.
4. Analyzes HTTP responses to identify true or false SQL conditions.
5. Uses SQL functions such as `SUBSTRING()` and `ASCII()` to test individual password characters.
6. Reconstructs the administrator password character by character.

The application response acts as a Boolean indicator:

- **TRUE:** The expected welcome message appears.
- **FALSE:** The expected welcome message does not appear.

---

## Architecture & Workflow

```text
Python Script (VS Code Terminal)
            |
            v
     Burp Suite Proxy
       127.0.0.1:8080
            |
            v
    PortSwigger Lab
            |
            v
   HTTP Response Analysis
            |
            v
 Conditional Response Detection
            |
            v
    Character Extraction
```

---

## Requirements

Before running the project, make sure you have:

- Python 3 installed
- Visual Studio Code
- Burp Suite Community or Professional
- PortSwigger Web Security Academy lab access
- Python dependencies listed in `requirements.txt`

## Installation

Clone the repository:

```bash
git clone https://github.com/nidarelyasa/Blind-SQLi-BruteForce-Tools.git
```

Navigate to the project directory:

```bash
cd Blind-SQLi-BruteForce-Tools
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Burp Suite Proxy Configuration

Burp Suite must be running before executing the Python script.

1. Open Burp Suite.
2. Navigate to **Proxy → Proxy settings**.
3. Ensure the Proxy Listener is active.
4. Configure the listener:

```text
Host: 127.0.0.1
Port: 8080
```

5. Keep Burp Suite running while executing the Python script.
6. Open **Proxy → HTTP history** to monitor the generated requests.

## Python Configuration

The script routes HTTP and HTTPS traffic through the local Burp Suite proxy.

```python
PROXIES = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}
```

This allows HTTP requests and responses to be inspected through Burp Suite.

**Note:** Use your own authorized lab session cookies. Never publish active session cookies or credentials in a public repository.

## Execution

Run the script through the VS Code terminal:

```bash
python exploit.py "https://YOUR-LAB-ID.web-security-academy.net/"
```

Replace the example URL with your own active PortSwigger lab URL.

Monitor the generated HTTP traffic through:

```text
Burp Suite → Proxy → HTTP History
```

Make sure Burp Suite is active and the local proxy listener is running.

## Dependencies

The project uses:

- `requests` – HTTP request handling.
- `urllib3` – HTTP connection utilities.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Learning Objectives

- Understand Boolean-Based Blind SQL Injection.
- Learn conditional SQL injection techniques.
- Practice HTTP cookie manipulation.
- Automate security testing using Python.
- Understand HTTP proxy integration with Burp Suite.
- Analyze application responses during security testing.

## Disclaimer

This project is intended strictly for educational purposes and authorized security testing within controlled environments, particularly PortSwigger Web Security Academy labs.

Do not use these techniques against systems without explicit authorization.

## Author

**Nidar Elyasa**

GitHub: [@nidarelyasa](https://github.com/nidarelyasa)
