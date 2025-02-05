from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def setup():
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen")
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver

def test_login():
    driver = setup()
    driver.get("https://www.demoblaze.com/")
    driver.implicitly_wait(10)

    login_button = driver.find_element(By.ID, "login2")
    login_button.click()
    time.sleep(2)

    username = driver.find_element(By.ID, "loginusername")
    username.send_keys("testuser")

    password = driver.find_element(By.ID, "loginpassword")
    password.send_keys("testpassword")

    submit = driver.find_element(By.XPATH, "//button[text()='Log in']")
    submit.click()

    time.sleep(3)

    welcome_text = driver.find_element(By.ID, "nameofuser")
    assert "Welcome" in welcome_text.text

    print("Login test passed!")
    driver.quit()

def test_logout():
    driver = setup()
    driver.get("https://www.demoblaze.com/")
    driver.implicitly_wait(10)

    test_login()

    logout_button = driver.find_element(By.ID, "logout2")
    logout_button.click()
    time.sleep(3)

    assert driver.find_element(By.ID, "login2").is_displayed()
    print("Logout test passed!")
    driver.quit()

def test_add_to_favorites():
    driver = setup()
    driver.get("https://www.demoblaze.com/")
    driver.implicitly_wait(10)

    test_login()

    driver.get("https://www.demoblaze.com/prod.html?idp_=1")#ovo je za otvaranje nekoog proizvoda
    time.sleep(2)

    fav_button = driver.find_element(By.XPATH, "//a[text()='Add to favorite']")
    fav_button.click()

    time.sleep(2)

    alert = driver.switch_to.alert
    assert "Added" in alert.text
    alert.accept()

    print("Add to favorites test passed!")
    driver.quit()

if __name__ == "__main__":
    test_login()
    test_logout()
    test_add_to_favorites()
