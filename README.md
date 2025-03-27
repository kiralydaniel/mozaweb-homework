# E-commerce Website Automation Testing

This project contains automated tests for an e-commerce website using Playwright with Python. The tests simulate user interactions like browsing products, adding items to cart, and checking out.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install the required dependencies:
```bash
# Option 1: Install from requirements.txt
pip install -r requirements.txt

# Option 2: Install packages individually
pip install playwright
pip install pytest
pip install pytest-playwright
```

4. Install Playwright browsers:
```bash
playwright install
```

## Project Structure 
```bash
├── pages/
│ ├── base_page.py
│ ├── checkout_page.py
│ ├── profile_page.py
│ ├── registration_page.py
│ └── shopping_page.py
├── tests/
│ └── test_purchase_flow.py
├── README.md
└── requirements.txt
```

## Running the Tests

To run all tests:
```bash
pytest
```
To run tests with visible browser:
```bash
pytest --headed
```

To run tests in a specific browser:
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

To generate HTML test report:
```bash
pytest --html=report.html --self-contained-html
```
The HTML report will be generated in your project directory as `report.html`. This is a self-contained HTML file that includes all styling and can be easily shared.

## Features

The automation framework includes:
- Page Object Model design pattern
- Shopping cart functionality testing
- Product sorting and filtering
- Checkout process validation
