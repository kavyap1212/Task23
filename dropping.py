from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://jqueryui.com/droppable/")

    # Switch to the frame containing the drag and drop elements
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".demo-frame"))

    # Explicit wait for the draggable element to be present
    wait = WebDriverWait(driver, 10)
    draggable = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
    droppable = wait.until(EC.presence_of_element_located((By.ID, "droppable")))

    # Perform the drag and drop operation
    actions = ActionChains(driver)
    actions.drag_and_drop(draggable, droppable).perform()

    # Print a success message
    print("Drag and drop operation was successful.")

except TimeoutException:
    print("The operation timed out. The elements were not found in time.")
except NoSuchElementException:
    print("One of the elements was not found on the page.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the driver
    driver.quit()