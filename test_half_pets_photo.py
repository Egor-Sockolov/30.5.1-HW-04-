import pytest
from conftest import my_pets
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

def test_half_pets_photo(my_pets):
    """ У половины питомцев есть фото """

    # Количество карточек питомцев в статистике пользователя
    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    cards = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

    cards_pets = cards[0].text.split("\n")
    cards_pets = cards_pets[1].split(": ")
    cards_pets = int(cards_pets[1])

    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.table-hover img")))
    img = pytest.driver.find_elements(By.CSS_SELECTOR, "table.table-hover img")

    cards_with_photo = 0
    for i in range(len(img)):
        if img[i].get_attribute("scr") != "":
            cards_with_photo += 1

    assert cards_with_photo >= cards_pets // 2