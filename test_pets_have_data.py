import pytest
from conftest import my_pets
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WDW

def test_pets_have_all_data(my_pets):
    """ У всех питомцев есть имя, порода и возраст """

    WDW(pytest.driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    name = pytest.driver.find_elements(By.CSS_SELECTOR, ".table.table-hover tbody tr")

    for i in range(len(name)):
        data = name[i].text.replace("\n", "").replace("×", "").split(" ")
        print(data)
        res = len(data)

        assert res == 3
