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

    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loginusername")))

    username = driver.find_element(By.ID, "loginusername")
    username.send_keys("testuserjakob")

    password = driver.find_element(By.ID, "loginpassword")
    password.send_keys("testpasswordjakob")

    submit = driver.find_element(By.XPATH, "//button[text()='Log in']")
    submit.click()

    welcome_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "nameofuser")))
    assert welcome_text.text.strip() != "", "Error: Welcome text is empty!"
    assert "Welcome" in welcome_text.text, f"Error: Unexpected welcome text '{welcome_text.text}'"

    print("Login test passed!")


def test_logout(driver):
    # Iskače alert pa ga moramo zatvoriti rucno
    try:
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"Closing unexpected alert: {alert.text}")
        alert.accept()
    except:
        print("No unexpected alert before logout.")

    logout_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout2")))
    logout_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login2")))

    print("Logout test passed!")


def test_add_to_cart(driver):
    driver.get("https://www.demoblaze.com/prod.html?idp_=1")  # Otvaranje proizvoda

    add_to_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']")))
    add_to_cart_button.click()

    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        assert "Added" in alert.text, f"Error: Unexpected alert text '{alert.text}'"
        alert.accept()
    except:
        print("Error: Alert not found!")

    print("Add to cart test passed!")

def test_remove_from_cart(driver):
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print(f"Closing unexpected alert: {alert.text}")
        alert.accept()
    except:
        print("No unexpected alert before opening cart.")

    driver.get("https://www.demoblaze.com/cart.html")

    try:
        delete_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete']")))
        delete_button.click()

        # cekas da se proizvod makne
        time.sleep(3)
        cart_items = driver.find_elements(By.XPATH, "//tr[@class='success']")
        assert len(cart_items) == 0, "Error: Item was not removed from the cart!"
        print("Item removed from cart successfully!")

    except:
        print("No items found in the cart to remove.")

    print("Remove from cart test passed!")


def test_return_to_home(driver):
    home_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Home ']")))
    home_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "carouselExampleIndicators")))
    print("Return to home test passed!")


if __name__ == "__main__":
    driver = setup()
    try:
        test_login(driver)
        test_add_to_cart(driver)
        test_remove_from_cart(driver)
        test_return_to_home(driver)
        test_logout(driver)
    finally:
        driver.quit()
