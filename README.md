# ✈️ Flight Automation Testing Framework

A robust end-to-end test automation framework built using **Playwright + Pytest** to validate flight search functionality on a demo flight booking website.

---

## 🚀 Project Overview

This project automates the process of searching for flights between cities and validates whether results are displayed correctly. It demonstrates real-world QA automation practices including browser automation, assertions, and structured test design.

---

## 🧰 Tech Stack

* 🐍 Python 3.11
* 🎭 Playwright
* 🧪 Pytest
* 📊 Pytest-HTML (for reports)

---

## 📁 Project Structure

```
Flight-automation/
│
├── tests/
│   └── test_flights.py        # Test cases
│
├── pages/
│   └── flight_page.py         # Page Object Model (optional/advanced)
│
├── pytest.ini                # Pytest configuration
├── requirements.txt         # Dependencies
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/Flight-Automation.git
cd Flight-Automation
```

---

### 2️⃣ Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
playwright install
```

---

## ▶️ Running Tests

Run all tests:

```
pytest
```

---

## 📊 Generate HTML Report

```
pytest --html=report.html
```

Open `report.html` in your browser to view results.

---

## ✅ Sample Test Scenario

* Navigate to flight booking site
* Select departure and destination cities
* Search for flights
* Validate that flight results are displayed

---

## 🧠 Key Features

* ✔️ Fast and reliable browser automation
* ✔️ Smart waits (no unnecessary delays)
* ✔️ Assertion-based validation
* ✔️ Clean and scalable structure
* ✔️ Easy integration with CI/CD (optional)

---

## 📸 Output Example

```
1 passed in ~3-5 seconds
```

---

## 🚀 Future Enhancements

* 🔹 Page Object Model (POM) implementation
* 🔹 Parallel test execution
* 🔹 Docker support
* 🔹 CI/CD integration
* 🔹 API testing integration

---

## 👨‍💻 Author

**Sanjay G**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
