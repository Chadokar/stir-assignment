# Flask Web Scraping Project with Selenium and Proxy

This project is a web scraping application built using Flask. It scrapes data from **x.com** using **Selenium** for automation and **Web Proxy** to bypass restrictions and manage traffic. 

## Features:
- Scrapes data from **x.com**.
- Uses **Selenium** for browser automation.
- Implements **Web Proxy** to manage requests and avoid detection.
- Built using **Flask** as the web framework to serve the app.

## Prerequisites:
Before running the application, ensure that you have the following installed:
- Python 3.x
- Web browser (e.g., Chrome)
- WebDriver for your browser (e.g., ChromeDriver for Chrome)

## Installation:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Install the Dependencies**:
   This project relies on several Python libraries, which are listed in the `requirements.txt` file. Install them by running:
   ```bash
   pip install -r requirements.txt
   ```

## Setting Up Web Proxy:
To use a proxy with Selenium: Create a file valid_proxies.txt and add proxies inside that


## Running the Application:

Once the dependencies are installed and the proxy is configured:

1. **Run the Flask application**:
   ```bash
   python app.py
   ```

2. The application will start and you can visit it by navigating to:
   ```
   http://127.0.0.1:5000
   ```

## Dependencies:
- Flask
- Selenium
- (Any other dependencies in `requirements.txt`)
