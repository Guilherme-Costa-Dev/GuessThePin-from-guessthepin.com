from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://www.guessthepin.com")

numStr = ""
for i in range(10000):
    try:
        campo_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "pin")))
        if i < 10:
            numStr = f"000{i}"
        elif i < 100:
            numStr = f"00{i}"
        elif i < 1000:
            numStr = f"0{i}"
        else:
            numStr = str(i)

        campo_input.send_keys(numStr)
        campo_input.send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.staleness_of(campo_input))

    except TimeoutException:
        print(f"Voce acertou o pin: {numStr}")
        break
