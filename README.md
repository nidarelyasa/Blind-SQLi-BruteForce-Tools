# Blind SQL Injection – Conditional Responses

A Python-based automation project for practicing **Boolean-Based Blind SQL Injection** using conditional HTTP responses.

This project is developed as part of my hands-on learning experience with [PortSwigger Web Security Academy](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses).

The script automates the process of extracting administrator password characters by evaluating SQL conditions and analyzing differences in HTTP responses.

## Lab Information

| Category | Details |
|---|---|
| Platform | PortSwigger Web Security Academy |
| Lab | Blind SQL Injection with Conditional Responses |
| Vulnerability | Boolean-Based Blind SQL Injection |
| Language | Python 3 |
| HTTP Client | Requests |
| Proxy | Burp Suite |
| Proxy Address | 127.0.0.1:8080 |

## How It Works

The automation follows these steps:

1. Establishes HTTP communication through Burp Suite Proxy.
2. Sends HTTP requests with modified `TrackingId` cookies.
3. Injects SQL conditions into the tracking cookie.
4. Analyzes HTTP responses to identify true or false SQL conditions.
5. Uses SQL functions such as `SUBSTRING()` and `ASCII()` to test individual password characters.
6. Reconstructs the administrator password character by character.

The application response acts as a Boolean indicator:

- **TRUE:** The expected welcome message appears.
- **FALSE:** The expected welcome message does not appear.

## Architecture & Workflow

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

## Requirements

- Python 3.x
- Burp Suite Community Edition
- Visual Studio Code
- PortSwigger Web Security Academy account
- An authorized and active lab instance

## Installation

Clone the repository:

```bash
git clone https://github.com/nidarelyasa/Blind-SQLi-BruteForce-Tools.git

cd Blind-SQLi-BruteForce-Tools
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Burp Suite Proxy Configuration

Before running the Python script, make sure Burp Suite is running.

1. Open Burp Suite.
2. Navigate to **Proxy → Proxy settings**.
3. Ensure the Proxy Listener is active.
4. Configure the listener to use:

```text
Host: 127.0.0.1
Port: 8080
```

5. Keep Burp Suite running while executing the Python script.
6. Intercept can remain OFF. Requests will still appear in HTTP History.

## Python Configuration

The script uses the following proxy configuration:

```python
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}
```

This routes HTTP and HTTPS requests through Burp Suite, allowing requests and responses to be inspected in HTTP History.

## Execution

Run the script through the VS Code terminal:

```bash
python sqli-lab-11.py
```

Monitor the generated HTTP requests through:

```text
Burp Suite → Proxy → HTTP History
```

## Dependencies

The project uses:

- `requests` – HTTP request handling.
- `urllib3` – HTTP connection utilities.

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
