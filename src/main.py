from humancursor import WebCursor

from browser import create_driver
from src.constants import WINDOW_SIZE, WINDOWS_URL
from src.daily_set import click_daily_set_elements


def main():
    driver = create_driver()

    driver.set_window_size(WINDOW_SIZE[0], WINDOW_SIZE[1])
    driver.get(WINDOWS_URL)

    cursor = WebCursor(driver)

    click_daily_set_elements(driver, cursor)

    input("Press Enter to continue...")
    driver.quit()

if __name__ == "__main__":
    main()