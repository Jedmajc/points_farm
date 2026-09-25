from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from browser import driver
from elements_utils import get_daily_set_elements_rect

driver.set_window_size(1920, 1080)
driver.get("https://rewards.bing.com/dashboard")

print(get_daily_set_elements_rect(driver))

input("Press Enter to close the browser")

driver.quit()