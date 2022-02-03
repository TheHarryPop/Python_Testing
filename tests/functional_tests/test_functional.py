from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as ec

url = 'http://127.0.0.1:5000/'


def launch_service():
    service = Service(GeckoDriverManager().install(), log_path='tests/functional_tests/geckodriver.exe')
    driver = webdriver.Firefox(service=service)
    driver.get(url)
    return driver


def test_display_board():
    driver = launch_service()
    driver.get(url + 'displayBoard')
    driver.implicitly_wait(5)
    assert driver.find_element(By.ID, 'table')
    driver.quit()


def test_authentication():
    driver = launch_service()
    form = driver.find_element(By.NAME, "email")
    form.send_keys("kate@shelifts.co.uk")
    form.submit()
    WebDriverWait(driver, 5).until(ec.url_to_be(url + 'showSummary'))
    assert driver.find_element(By.LINK_TEXT, 'Logout')
    driver.quit()


def test_booking_places():
    driver = launch_service()
    form = driver.find_element(By.NAME, "email")
    form.send_keys("kate@shelifts.co.uk")
    form.submit()
    driver.implicitly_wait(5)
    link = driver.find_element(By.LINK_TEXT, 'Book Places')
    link.click()
    driver.implicitly_wait(5)
    form = driver.find_element(By.NAME, 'places')
    form.send_keys("10")
    form.submit()
    WebDriverWait(driver, 5).until(ec.url_to_be(url + 'purchasePlaces'))
    assert driver.find_element(By.LINK_TEXT, 'Logout')
    driver.quit()



