# Job Alert System


## Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd jobAlertSystem
```

### 2. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies


install dependencies:

```bash
pip install beautifulsoup4>=4.13.4
pip install lxml>=6.0.0
pip install openpyxl>=3.1.5
pip install pandas>=2.3.1
pip install requests>=2.32.4
```

## Project Structure

```
jobAlertSystem/
├── customParsers/
│   ├── cutomParser.py      # Main job scraping logic for Moody's
│   └── example.py          # Example implementation
├── data/
│   ├── data.xlsx           # Coordinator and company data
│   └── Working Professionals Data.xlsx
├── main.py                 # Main application entry point
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Lock file for dependency versions
└── README.md               # This file
```


### Basic Usage

Run the main job scraper:

```bash
cd customParser
python customParsers/cutomParser.py
```



Expected output:
<img width="1100" height="539" alt="image" src="https://github.com/user-attachments/assets/2a943745-bb6a-4e4e-b18d-015a3a095d20" />


Will add email section lateer
