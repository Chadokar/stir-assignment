from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
import time
import config


def get_data(proxy):
    options = Options()
    if proxy:
        options.add_argument(f'--proxy-server=http://{proxy}')
        print(f'Using the proxy: {proxy}')
    else:
        options.add_argument("--start-maximized")

    # Initializing the WebDriver (assuming ChromeDriver is in PATH)
    driver = webdriver.Chrome(options=options)

    try:
        # Open the URL
        driver.get("http://x.com/i/flow/login?mx=2")

        # Wait for the page to load
        time.sleep(3)  # Adjust this wait if needed

        # Locate the input field and fill it
        input_field = driver.find_element(
            By.XPATH, '//input[@autocomplete="username"]')
        input_field.send_keys(config.TWITTER_USERNAME)

        # Wait to ensure input is filled
        time.sleep(1)

        # Locate and click the button
        next_button = driver.find_element(
            By.CSS_SELECTOR, '[class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"]')
        next_button.click()

        time.sleep(5)

        input_field = driver.find_element(
            By.CSS_SELECTOR, '[class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"][type="password"]')
        input_field.send_keys(config.TWITTER_PASSWORD)

        time.sleep(1)

        next_button = driver.find_element(
            By.CSS_SELECTOR, '[class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"][data-testid="LoginForm_Login_Button"]')
        next_button.click()

        time.sleep(5)
        elements = driver.find_elements(
            By.CSS_SELECTOR, '[data-testid="trend"][role="link"]')
        # for element in elements:
        #     print(element.text)
        return [element.text for element in elements]

    finally:
        # will close the browser after a short delay
        time.sleep(5)
        driver.quit()
