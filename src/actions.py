from browser import driver
from humancursor import WebCursor

def move_mouse_to_element_rect(element):
    cursor = WebCursor(driver)
    cursor.show_cursor()
    cursor.move_to(element, relative_position=[0.4,0.6])
