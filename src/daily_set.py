import random
import time

from src.actions import click_on_element
from src.elements_utils import find_daily_set_elements
from src.tabs_utils import get_original_handle, switch_to_original_handle, close_all_tabs_but_original


def click_daily_set_elements(driver, cursor):
    original_handle = get_original_handle(driver)
    elements = find_daily_set_elements(driver)
    for element in elements:
        time.sleep(random.uniform(0.2, 0.4))
        click_on_element(cursor, element)
        time.sleep(random.uniform(0.5, 0.9))
        switch_to_original_handle(driver, original_handle)

