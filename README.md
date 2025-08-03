# Job Alert System

A Python-based job alert system that scrapes job listings from career websites and provides automated job monitoring capabilities. Currently configured to scrape Moody's career portal and can be extended to support other job sites.

## Features

- **Web Scraping**: Automated job listing extraction from career websites
- **Data Processing**: Excel data integration for coordinator information
- **Job Monitoring**: Real-time job posting tracking
- **Structured Output**: Organized job data with role details, locations, and categories
- **Extensible Architecture**: Modular design for adding new job sites

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

The project uses `pyproject.toml` for dependency management. Install all required packages:

```bash
pip install -e .
```

Alternatively, install dependencies manually:

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

## Configuration

### 1. Data Setup

Place your coordinator and company data in the `data/data.xlsx` file with the following structure:

| Name | Mobile Number | Company Name |
|------|---------------|--------------|
| Coordinator Name | Phone Number | Company Name |

### 2. Customizing Job Sources

The system is currently configured for Moody's career portal. To add new job sources:

1. Create a new parser in the `customParsers/` directory
2. Follow the structure in `cutomParser.py`
3. Update the main application to use your new parser

## Usage

### Basic Usage

Run the main job scraper:

```bash
python customParsers/cutomParser.py
```

### Expected Output

The system will output job listings with the following information for each role:

- **Role**: Job title
- **Role Apply URL**: Direct link to apply
- **Posted**: Date when the job was posted
- **Location**: Job location
- **Job Category**: Category of the job

Example output:
```
Following roles found

{'role': 'Software Engineer', 'roleApplyUrl': 'https://careers.moodys.com/jobs/123', 'Posted': '2024-01-15', 'Location': 'New York, NY', 'JobCategory': 'Technology'}

{'role': 'Data Analyst', 'roleApplyUrl': 'https://careers.moodys.com/jobs/456', 'Posted': '2024-01-14', 'Location': 'London, UK', 'JobCategory': 'Analytics'}
```

## Development

### Adding New Job Sources

1. **Create a new parser file** in `customParsers/`
2. **Implement the scraping logic** following the existing pattern
3. **Update the data structure** to match your requirements
4. **Test the parser** with sample data

### Example Parser Structure

```python
import pandas as pd
from bs4 import BeautifulSoup
import requests

def getJobsList(url):
    # Your scraping logic here
    pass

def getJobsDetailsFromJobsList(data, jobLists):
    # Your job details extraction logic here
    pass

# Main execution
jobList = getJobsList(jobUrl)
result = getJobsDetailsFromJobsList(data, jobList)
```

## Dependencies

- **beautifulsoup4**: HTML parsing and web scraping
- **lxml**: XML/HTML parser backend
- **openpyxl**: Excel file reading and writing
- **pandas**: Data manipulation and analysis
- **requests**: HTTP library for making web requests

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Excel File Not Found**: Verify `data/data.xlsx` exists and has the correct structure

3. **Web Scraping Issues**: Check if the target website structure has changed

4. **Permission Errors**: Ensure you have write permissions in the project directory

### Debug Mode

To debug scraping issues, add print statements in the parser functions:

```python
def getJobsList(url):
    print(f"Fetching jobs from: {url}")
    html_data = requests.get(url).text
    print(f"Response status: {requests.get(url).status_code}")
    # ... rest of the function
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the troubleshooting section above

## Changelog

### Version 0.1.0
- Initial release
- Moody's career portal scraping
- Basic job data extraction
- Excel data integration
