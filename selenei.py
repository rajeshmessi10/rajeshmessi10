import select
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

#driver.implicitly_wait(2)
driver.get("https://magento.softwaretestingboard.com/collections/yoga-new.html")
# wait = WebDriverWait(driver, 10)
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#opentab")))
# button.click()
# time.sleep(3)

#driver.switch_to.window(win[0])
# win = driver.window_handles

actions = ActionChains(driver)
time.sleep(3)
actions.move_to_element(driver.find_element(By.XPATH , "(//span[@class='ui-menu-icon ui-icon ui-icon-carat-1-e'])[1]")
).perform()
actions.move_to_element(driver.find_element(By.CSS_SELECTOR,"#ui-id-9")).perform()

driver.find_element(By.ID, "ui-id-11").click()



time.sleep(3)

print(driver.title)

driver.back()
driver.refresh()
driver.forward()
time.sleep(2)

driver.quit()






time.sleep(3)
driver.quit()




















