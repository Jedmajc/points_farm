from selenium import webdriver
from constants import USER_DATA_DIR, PROFILE_NAME
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.EdgeOptions()

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
options.add_argument(f"--profile-directory={PROFILE_NAME}")

driver = webdriver.Edge(options=options)

driver.set_window_size(1920, 1080)
driver.get("https://rewards.bing.com/dashboard")

driver.implicitly_wait(5)

element = driver.find_element(
    By.XPATH,
    f"//*[contains(text(), 'Twoja aktywność')]"
)

actions = ActionChains(driver)
actions.move_to_element(element).perform()

print(element.location)


input("Press Enter to close the browser")

driver.quit()