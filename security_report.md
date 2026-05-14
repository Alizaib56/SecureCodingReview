\# 🔐 Secure Coding Review Report



\## 📌 Project Overview



This project demonstrates a security review of a vulnerable Python login application developed as part of the CodeAlpha Cyber Security Internship.



The purpose of this review is to identify common security vulnerabilities in authentication systems and implement secure coding practices to improve application security.



\---



\# 🔍 Vulnerabilities Identified



\## 1. Hardcoded Credentials



\### Problem



The username and password were directly written inside the source code.



\### Example



```python

stored\_username = "admin"

stored\_password = "admin123"

```



\### Security Risk



If attackers gain access to the source code, they can easily view login credentials and access the system.



\### Recommendation



Credentials should never be hardcoded inside applications. Use:



\* Environment variables

\* Databases

\* Secure secret managers



\---



\## 2. Weak Password



\### Problem



The password `admin123` is weak and predictable.



\### Security Risk



Weak passwords are vulnerable to:



\* Brute-force attacks

\* Dictionary attacks

\* Credential guessing



\### Recommendation



Use strong passwords containing:



\* Uppercase letters

\* Lowercase letters

\* Numbers

\* Special symbols



\### Example



```plaintext

StrongPassword123!

```



\---



\## 3. Plain Text Password Storage



\### Problem



Passwords were stored in plain text format.



\### Security Risk



If source code or databases are leaked, attackers can directly read user passwords.



\### Recommendation



Passwords should always be hashed using secure hashing algorithms such as:



\* SHA-256

\* bcrypt

\* Argon2



\---



\# 🛡️ Security Improvements Implemented



\## ✅ SHA-256 Password Hashing



Passwords are now converted into secure hashes before storage and comparison.



\### Example



```python

hashlib.sha256(password.encode()).hexdigest()

```



\### Benefit



Even if attackers access stored data, original passwords remain hidden.



\---



\## ✅ Strong Password Policy



A stronger password was implemented to improve authentication security.



\### Implemented Password



```plaintext

StrongPassword123!

```



\---



\## ✅ Improved Authentication Logic



The secure application compares hashed passwords instead of plain text passwords.



\### Benefit



This reduces the risk of credential exposure and improves overall application security.



\---



\# 🛠️ Technologies Used



\* Python

\* hashlib library

\* SHA-256 hashing



\---



\# 📚 Learning Outcomes



Through this project, I learned:



\* The importance of secure coding practices

\* Risks associated with weak authentication systems

\* How password hashing improves security

\* Basic application security concepts



\---



\# 🧠 Conclusion



This project demonstrates how insecure coding practices can create serious security vulnerabilities in applications.



By implementing secure authentication methods such as password hashing and stronger password policies, application security can be significantly improved.



Secure coding is an essential part of cybersecurity and helps protect sensitive user information from attackers.



\---



\# 👨‍💻 Author



Ali Zaib

Cyber Security Intern @ CodeAlpha



