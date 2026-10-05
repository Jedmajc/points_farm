from random import random

from humancursor import WebCursor
from selenium.webdriver import ActionChains

from actions import move_mouse_to_element_rect

from browser import driver
from elements_utils import get_daily_set_elements_rect
from src.tabs_utils import switch_to_original_handle
from selenium.webdriver.support import expected_conditions as EC

driver.set_window_size(1920, 1080)
driver.get("https://rewards.bing.com/dashboard")

cursor = WebCursor(driver)
cursor.show_cursor()

element_rects = get_daily_set_elements_rect(driver)

original_handle = driver.current_window_handle

for rect in element_rects:
    move_mouse_to_element_rect(rect, cursor)
    ActionChains(driver).click().perform()
    switch_to_original_handle(driver, original_handle)

input("Press Enter to close the browser")

driver.quit()