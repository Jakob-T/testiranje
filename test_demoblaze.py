from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup():
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen")
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver

def test_login(driver):
    driver.get("https://www.demoblaze.com/")
    driver.implicitly_wait(10)

    login_button = driver.find_element(By.ID, "login2")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loginusername")))

    username = driver.find_element(By.ID, "loginusername")
    username.send_keys("testuserjakob")

    password = driver.find_element(By.ID, "loginpassword")
    password.send_keys("testpasswordjakob")

    submit = driver.find_element(By.XPATH, "//button[text()='Log in']")
    submit.click()

    welcome_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nameofuser")))
    assert "Welcome" in welcome_text.text

    print("Login test passed!")

def test_logout(driver):
    logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout2")))
    logout_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login2")))

    print("Logout test passed!")

def test_add_to_favorites(driver):
    driver.get("https://www.demoblaze.com/prod.html?idp_=1")  # Otvaranje proizvoda

    fav_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to favorite']")))
    fav_button.click()

    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "Added" in alert.text
    alert.accept()

    print("Add to favorites test passed!")

if __name__ == "__main__":
    driver = setup()
    try:
        test_login(driver)
        test_add_to_favorites(driver)
        test_logout(driver)
    finally:
        driver.quit()
