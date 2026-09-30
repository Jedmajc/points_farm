from humancursor import WebCursor

from actions import move_mouse_to_element_rect

from browser import driver
from elements_utils import get_daily_set_elements_rect

driver.set_window_size(1920, 1080)
driver.get("https://rewards.bing.com/dashboard")

cursor = WebCursor(driver)
cursor.show_cursor()

element_rects = get_daily_set_elements_rect(driver)
for rect in element_rects:
    move_mouse_to_element_rect(rect, cursor)

input("Press Enter to close the browser")

driver.quit()