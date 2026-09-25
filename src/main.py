from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from actions import move_mouse_to_element_rect

from browser import driver
from elements_utils import get_daily_set_elements_rect

driver.set_window_size(1920, 1080)
driver.get("https://rewards.bing.com/dashboard")

#TEST
first_element = get_daily_set_elements_rect(driver)[0]
move_mouse_to_element_rect(first_element)
#END TEST

input("Press Enter to close the browser")

driver.quit()