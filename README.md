🚀 SHIPSTICKS Playwright Automation Framework

Modern • Scalable • Maintainable • Enterprise‑Ready

A robust UI automation framework built with Python, Playwright, and Pytest, following clean architecture principles and Page Object Model (POM) design.
Perfect for enterprise QA teams, CI/CD pipelines, and high‑coverage automated testing.

🏗️ Project Architecture
SHIPSTICKS/
│── config/
│── pages/
│   ├── home_page.py
│   ├── ship_page.py
│   └── __init__.py
│── tests/
│   ├── test_step1_booking.py
│   └── __init__.py
│── utilities/
│   ├── data_manager.py
│   └── __init__.py
│── resources/
│── reports/
│   └── report.html
│── conftest.py
│── pytest.ini
│── requirements.txt
│── README.md

📂 Folder Overview
Folder / File	Description
config/	Environment configs, constants, URLs, test settings
pages/	Page Object Model classes for UI interactions
tests/	All test cases written using Pytest
utilities/	Reusable helpers, data managers, utilities
resources/	Test data files (CSV, JSON, images, etc.)
reports/	HTML reports, logs, screenshots
conftest.py	Global fixtures for browser, context, reporting
pytest.ini	Pytest configuration (markers, options)
requirements.txt	Python dependencies

🧰 Tech Stack & Tools
🐍 Python 3.13
🎭 Playwright
🧪 Pytest
🧱 Page Object Model (POM)
📊 HTML Reporting

⚙️ Setup Instructions (From GitHub)
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/shipsticks-automation.git
cd shipsticks-automation

2️⃣ Install Dependencies
pip install -r requirements.txt
        (or)
Execute the following commands manually
pip install playwright
pip install pytest
pip install pytest-playwright
playwright install

3️⃣ Install Playwright Browsers
playwright install

▶️ Running Tests
pytest --html=reports/report.html --self-contained-html

📊 Reports & Logs
After execution, reports are generated under: /reports/report.html

Open it in any browser to view:
Test results
Screenshots
Execution logs
Failure traces



