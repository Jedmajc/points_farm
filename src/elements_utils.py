from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def find_daily_set_elements(driver):
    daily_set_elements = []

    wait = WebDriverWait(driver, 10)

    redeem = driver.find_element(By.XPATH, "//*[@id='redeem']")

    wait.until(EC.visibility_of(redeem))

    for link in driver.find_elements(By.XPATH, "//a[@href]"):
        if '+10' in link.text:
            daily_set_elements.append(link)

    return daily_set_elements


def get_daily_set_elements_rect(driver):
    daily_set_element_rects = []

    for element in find_daily_set_elements(driver):
        driver.execute_script("""
        arguments[0].scrollIntoView({
        block: "center",
        });
        """, element)

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

    return daily_set_element_rects

