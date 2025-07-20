from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


profile_path = r"C:\ChromeProfiles\NewChromeProfile1"
profile_name = "Default"

options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={profile_path}")
options.add_argument(f"--profile-directory={profile_name}")
# options.add_argument("--headless")           # Run in headless mode

driver = webdriver.Chrome(options=options)