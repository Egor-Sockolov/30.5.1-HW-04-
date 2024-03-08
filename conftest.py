import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def driver():

    pytest.driver = ChromeService(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    pytest.driver = webdriver.Chrome(options=options)

    # Неявное ожидание
    pytest.driver.implicitly_wait(10)

    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.ID, "email")))

    yield pytest.driver

    pytest.driver.quit()

@pytest.fixture()
def my_pets():

    # Добавить email
    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.ID, "email")))
    pytest.driver.find_element(By.ID, "email").send_keys("qwer123@bk.ru")

    # Добавить password
    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.ID, "pass")))
    pytest.driver.find_element(By.ID, "pass").send_keys("qwer123")

    # Нажимаем на кнопку "Отправить"
    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    pytest.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Нажимаем на кнопку "Мои питомцы"
    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()

