import pytest
from conftest import my_pets
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

def test_unique_pets(my_pets):
    """ Карточки питомцев не повторяются """

    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    name = pytest.driver.find_elements(By.CSS_SELECTOR, ".table.table-hover tbody tr")

    all_name = []

    for i in range(len(name)):
        split_name = name[i].text.replace("\n", "").replace("×", "").split(" ")
        all_name.append(split_name)

    print(all_name)

    unique_cards_pets = 0
    for i in range(len(all_name)):
        if all_name.count(all_name[i]) > 1:
            unique_cards_pets += 1

    assert unique_cards_pets == 0




