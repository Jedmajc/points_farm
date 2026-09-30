import random

from browser import driver
from humancursor import WebCursor

def move_mouse_to_element_rect(rect, cursor):

    print(calculate_element_center_area(rect))
    x = calculate_element_center_area(rect)[0]
    y = calculate_element_center_area(rect)[1]
    cursor.move_to([x, y])

def calculate_element_center_area(rect):
    area_x = rect['left'] + rect['width']/random.uniform(1.25, 2.75)
    area_y = rect['top'] + rect['height']/random.uniform(1.25, 2.75)

    return area_x, area_y
