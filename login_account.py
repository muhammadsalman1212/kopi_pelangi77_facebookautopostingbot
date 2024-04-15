import time

from selenium import webdriver

# Path to your Chrome profile directory
# chrome_profile_directory = r"C:\Users\Kopipelangi\AppData\Local\Google\Chrome\User Data\Profile 34"
chrome_profile_directory = r"C:\Users\user\Documents\all_profiles\Profile 3"
# Configure ChromeOptions to use the specified profile directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={chrome_profile_directory}")

# Initialize Chrome WebDriver with the configured options
driver = webdriver.Chrome(options=chrome_options)

# Example usage: Open a website
driver.get('https://facebook.com/')

# Remember to quit the driver when done

time.sleep(5555)









