# 🔐 Secure Coding Review Report

**Python Authentication Security Analysis**
**CodeAlpha Cyber Security Internship**
**Author:** Ali Zaib

---

## 📌 Table of Contents

1. [Project Overview](#1-project-overview)
2. [Vulnerabilities Identified](#2-vulnerabilities-identified)
   - [2.1 Hardcoded Credentials](#21-hardcoded-credentials)
   - [2.2 Weak Password](#22-weak-password)
   - [2.3 Plain Text Password Storage](#23-plain-text-password-storage)
   - [2.4 No Brute-Force Protection](#24-no-brute-force-protection)
   - [2.5 Timing Attack Vulnerability](#25-timing-attack-vulnerability)
   - [2.6 No Audit Logging](#26-no-audit-logging)
3. [Security Improvements Implemented](#3-security-improvements-implemented)
4. [Technologies Used](#4-technologies-used)
5. [Learning Outcomes](#5-learning-outcomes)
6. [Conclusion](#6-conclusion)

---

## 1. Project Overview

This report presents a security review of a vulnerable Python login application, developed as part of the **CodeAlpha Cyber Security Internship**. The objective is to identify common authentication vulnerabilities and demonstrate how each can be remediated using industry-accepted secure coding practices.

The review covers **six distinct vulnerability classes**, proposes concrete fixes, and documents the improvements implemented in the corrected version of the application.

---

## 2. Vulnerabilities Identified

### 2.1 Hardcoded Credentials

#### Description
The username and password were written directly inside the source code, meaning any person who gains read access to the file immediately obtains valid credentials.

#### Vulnerable Code
```python
# vulnerable_app.py
stored_username = "admin"
stored_password = "admin123"   # hardcoded — visible to anyone reading the file
```

#### Risk
**Severity: 🔴 High** — Source code is frequently shared via version control systems (e.g. GitHub). A single accidental public commit exposes credentials permanently.

#### Recommendation
Load credentials at runtime from environment variables or a secrets manager — never from source code.

```python
import os

# Load from environment — never from source
stored_username      = os.environ["APP_USERNAME"]
stored_password_hash = os.environ["APP_PASSWORD_HASH"]
```

---

### 2.2 Weak Password

#### Description
The password `admin123` is one of the most common passwords worldwide and appears in every major credential-stuffing wordlist.

#### Risk
**Severity: 🔴 High** — Weak passwords are defeated instantly by brute-force, dictionary, and credential-stuffing attacks.

#### Recommendation
Enforce a minimum password policy at the application level. A strong password must:

- Be at least **12 characters** long
- Contain **uppercase and lowercase** letters
- Include at least one **digit**
- Include at least one **special character** (e.g. `!`, `@`, `#`, `$`)
- Not appear in known-breached password lists

---

### 2.3 Plain Text Password Storage

#### Description
The original application compared user input directly against a plain-text string. Any database or source-code leak immediately reveals every user's password.

#### Risk
**Severity: 🔴 Critical** — Plain-text storage violates [OWASP A02 (Cryptographic Failures)](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/) and most data-protection regulations (GDPR, PCI-DSS, etc.).

#### Recommendation
Passwords must be hashed with a **slow, salted algorithm** designed specifically for password storage.

> ⚠️ **Important:** SHA-256 is NOT appropriate for passwords. It is designed to be fast, which means attackers can hash billions of guesses per second. Use **bcrypt** or **Argon2** instead.

```python
import bcrypt

# Hashing a new password (e.g. during registration)
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))

# Verifying at login
if bcrypt.checkpw(entered_password.encode(), stored_hash):
    print("Login successful")
```

---

### 2.4 No Brute-Force Protection

#### Description
The original application places no limit on the number of login attempts. An attacker can submit an unlimited number of password guesses without any delay or lockout.

#### Risk
**Severity: 🔴 High** — Without rate limiting, automated tools can test millions of passwords per minute against the login endpoint.

#### Recommendation
Implement an **account lockout** or exponential back-off after a threshold of failed attempts (e.g. lock for 15 minutes after 5 failures).

```python
failed_attempts = {}
MAX_ATTEMPTS = 5

def check_login(username, password):
    attempts = failed_attempts.get(username, 0)
    if attempts >= MAX_ATTEMPTS:
        return "Account locked. Contact administrator."
    if not verify_password(username, password):
        failed_attempts[username] = attempts + 1
        return "Invalid credentials."
    failed_attempts[username] = 0   # reset on success
    return "Login successful."
```

---

### 2.5 Timing Attack Vulnerability

#### Description
Using Python's `==` operator to compare passwords or hashes exits the comparison as soon as a mismatch is found. This creates a measurable timing difference that an attacker can use to guess the correct value one character at a time.

#### Risk
**Severity: 🟡 Medium** — Exploiting this remotely is difficult but well-documented against high-value targets.

#### Recommendation
Use `hmac.compare_digest()` for all secret comparisons. It always takes the same time regardless of where the strings differ.

```python
import hmac

# Safe constant-time comparison
if hmac.compare_digest(entered_hash, stored_hash):
    print("Login successful")
```

---

### 2.6 No Audit Logging

#### Description
The original application produces no log output. There is no record of successful logins, failed attempts, or lockout events, making it impossible to detect or investigate an attack after the fact.

#### Risk
**Severity: 🟡 Medium** — Absence of logging violates [OWASP A09 (Security Logging and Monitoring Failures)](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/) and hinders incident response.

#### Recommendation
Log all authentication events with a timestamp and source identifier. **Never log the password itself.**

```python
import logging, datetime

logging.basicConfig(filename='auth.log', level=logging.INFO)

def log_event(username, success):
    status = 'SUCCESS' if success else 'FAILURE'
    logging.info(f'{datetime.datetime.utcnow()} | {status} | user={username}')
```

---

## 3. Security Improvements Implemented

The `secure_app.py` file demonstrates the following improvements over the original vulnerable application:

| Issue | Original Code | Improved Code |
|---|---|---|
| Password Hashing | None (plain text) | SHA-256 hashing* |
| Credential Storage | Hardcoded in source | Environment variables (recommended) |
| Password Strength | `admin123` (weak) | Strong + complexity rules |
| Brute-Force Protection | None | Rate limiting / lockout |
| Timing Attack Defence | None | `hmac.compare_digest()` |
| Audit Logging | None | Failed login logging |

> *SHA-256 is used in `secure_app.py` as a step up from plain text. For production systems, **bcrypt** or **Argon2** is strongly recommended — see [Section 2.3](#23-plain-text-password-storage).

---

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| `hashlib` (SHA-256) | Used in `secure_app.py` |
| `bcrypt` | Recommended for production password hashing |
| `hmac` | Recommended for constant-time comparison |
| `os.environ` | Recommended for secret loading |
| `logging` | Recommended for audit trails |

---

## 5. Learning Outcomes

Through this project the following key concepts were explored and applied:

- Why **hardcoded credentials** are dangerous, especially in version-controlled projects
- The difference between **general-purpose hashing** (SHA-256) and **password-specific hashing** (bcrypt, Argon2), and why only the latter is appropriate for credential storage
- How **timing attacks** work and how constant-time comparison functions eliminate the risk
- The importance of **rate limiting** as a defence against automated credential-guessing attacks
- How **audit logging** enables detection and investigation of authentication abuse

---

## 6. Conclusion

This project demonstrates how several common but critical vulnerabilities can coexist in a minimal authentication system, and how each can be addressed through established secure coding practices.

The most important takeaway is that **security is layered** — fixing only one vulnerability while leaving others in place does not make a system secure. Effective authentication requires all layers to be addressed together.

Secure coding practices are not optional extras — they are the foundation of any system that handles user data.

---

*Ali Zaib — Cyber Security Intern @ CodeAlpha*
