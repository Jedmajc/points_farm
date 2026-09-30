from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from humancursor import WebCursor

def find_daily_set_elements(driver):
    daily_set_elements = []

    wait = WebDriverWait(driver, 10)

    redeem = driver.find_element(By.XPATH, "//*[@id='redeem']")

    wait.until(EC.visibility_of(redeem))

    for link in driver.find_elements(By.XPATH, "//a[@href]"):
        if '+10' in link.text:
            daily_set_elements.append(link)
    #returns list of WebElements
    return daily_set_elements


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
