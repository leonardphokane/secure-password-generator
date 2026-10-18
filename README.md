![Header](images/header.png)

# 🔐 Secure Password Generator

![Auspify](https://img.shields.io/badge/Auspify-Bring%20Future%20Through%20Tech-blueviolet?style=for-the-badge&logo=github)
![Project](https://img.shields.io/badge/AuspifyProject-Python%20Developer-ff69b4?style=for-the-badge&logo=python)
![Task](https://img.shields.io/badge/Task-Password%20Generator-brightgreen?style=for-the-badge&logo=lock)
![Skills](https://img.shields.io/badge/Skills-Python%20Basics%20%7C%20Random%20Module%20%7C%20String%20Manipulation-orange?style=for-the-badge&logo=code)
![Technologies](https://img.shields.io/badge/Auspify-Technologies-lightblue?style=for-the-badge&logo=azuredevops)
![Internship](https://img.shields.io/badge/Auspify-Internship-yellow?style=for-the-badge&logo=book)


A Python application that generates secure and customizable passwords.  
Users can choose password length and decide whether to include lowercase, uppercase, digits, and symbols.

---

## 🚀 Features
- Random password generation
- Customizable length
- Toggle inclusion of lowercase, uppercase, digits, and symbols
- Error handling if no character sets are selected
- Unit tests for reliability

---

## 📸 Screenshots

### 🧩 App Run
![App Run Screenshot](screenshots/secure_password_generator_app_run.png)

### 🧪 Tests Passed
![Tests Screenshot](screenshots/secure_password_generator_tests_pass.png)

---

## 📂 Project Structure
secure-password-generator/
│── README.md
│── requirements.txt
│── password_generator.py
│── utils/
│   └── init.py
│── tests/
│   └── test_password.py


---

## ⚡ Setup & Usage

### 1. Clone the repo
```bash
git clone https://github.com/your-username/secure-password-generator.git
cd secure-password-generator
```

### 2. Run the generator
```bash
python password_generator.py
```
You’ll be prompted for:

- Password length

- Whether to include lowercase, uppercase, digits, and symbols


### 3. Example
```bash
🔐 Customizable Secure Password Generator
Enter desired password length: 12
Include lowercase letters? (y/n): y
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): n
Generated Password: aB9xYzQwLmNp
```
---

## 🧪 Running Tests
From the project root:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
---

## 📘 Skills Learned
- Python basics

- Random module

- String manipulation

- Unit testing with `unittest`

## ✅ Future Improvements
- Add GUI or web interface

- Save generated passwords securely

- Add entropy/strength meter

![Footer](images/footer.png)