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
4. Analyzes HTTP responses
