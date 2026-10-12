def switch_to_original_handle(driver, origina_handle):
    driver.switch_to.window(origina_handle)

def get_original_handle(driver):
    original_handle = driver.current_window_handle
    return original_handle

def close_all_tabs_but_original(driver, original_handle):
    for handle in driver.window_handles:
        if handle != original_handle:
            driver.switch_to.window(handle)
            driver.close()