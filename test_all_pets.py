import pytest
from conftest import my_pets
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

def test_all_pets(my_pets):
    """ На странице пользователя присутствуют все питомцы """


    # Количество визуальных карточек питомцев
    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".table.table-hover tbody tr")

    # Количество карточек питомцев в статистике пользователя
    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    cards = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    cards_pets = cards[0].text.split("\n")
    cards_pets = cards_pets[1].split(": ")
    cards_pets = int(cards_pets[1])

    assert cards_pets == len(pets)