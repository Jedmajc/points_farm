import random
import time

from selenium.webdriver.common.by import By
from humancursor import WebCursor

from src.actions import click_on_element


def get_daily_set_elements_rect(driver):
    daily_set_element_rects = []
    daily_set_elements = find_daily_set_elements(driver)

    cursor = WebCursor(driver)

    if not daily_set_elements:
        return daily_set_element_rects

    cursor.scroll_into_view_of_element(daily_set_elements[0])

    for element in daily_set_elements:
        rect = driver.execute_script("""
        const r = arguments[0].getBoundingClientRect();
        return {
        left: r.left,
        top: r.top,
        right: r.right,
        bottom: r.bottom,
        width: r.width,
        height: r.height,
        }
        """, element)

        daily_set_element_rects.append(rect)
    #returns list of coordinates
    #example: {'bottom': 557, 'height': 126, 'left': 284, 'right': 713, 'top': 431, 'width': 429}
    return daily_set_element_rects

def find_daily_set_elements(driver):
    section = driver.find_element(By.ID, "dailyset")
    return section.find_elements(By.XPATH, ".//a")

def click_daily_set_elements(driver, cursor):
    elements = find_daily_set_elements(driver)
    for element in elements:
        time.sleep(random.uniform(0.2, 0.4))
        click_on_element(cursor, element)
        break