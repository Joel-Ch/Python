from selenium import webdriver
from selenium.webdriver.common.by import By

def test_eight_components():
    driver = webdriver.Chrome()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    assert title == "Web form"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    dropdown_menu = driver.find_element(by=By.NAME, value="my-select")

    dropdown_menu.find_element(by=By.CSS_SELECTOR, value="option:nth-child(3)").click()

    text_box.send_keys("Selenium")
    submit_button.click()
    
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"
    
    driver.implicitly_wait(10)

    driver.quit()
    
test_eight_components()