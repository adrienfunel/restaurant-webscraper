def smooth_scrolling(driver):
    """Allows to scroll through the entire webpage to charge dynamically the full HTML source"""
    total_height = int(driver.execute_script("return document.body.scrollHeight"))

    for i in range(1, total_height, 5):
        driver.execute_script("window.scrollTo(0, {});".format(i))
