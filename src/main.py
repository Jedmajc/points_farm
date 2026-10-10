from humancursor import WebCursor

from browser import create_driver
from src.elements_utils import click_daily_set_elements


def main():
    driver = create_driver()

    driver.set_window_size(1920, 1080)
    driver.get("https://rewards.bing.com/dashboard")

    cursor = WebCursor(driver)

    click_daily_set_elements(driver, cursor)

    input("Press Enter to continue...")
    driver.quit()

if __name__ == "__main__":
    main()