from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import time

# Define a function to check appointment availability
def check_appointment():
    # Create a webdriver instance
    driver = webdriver.Chrome()

    # Open the website / Change the URL for other passport offices.
    driver.get("https://australianpassportofficesydney.setmore.com/")
    time.sleep(5)

    # Wait and then Click OK on popup window
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, 
            "//*[@id='root']/div/main/section[1]/div[1]/div/button")))
    element.click()

    # Click on the service "Authentication or Apostille"
    service = driver.find_element(By.XPATH, 
            "//div[@class='service-infoholder']/div/h5[text()='Authentication or Apostille']")
    service.click()

    # Wait for the calendar to load
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//*[@id='root']/div/main/section[1]/div[3]/div[1]/div/div/div[1]/div/div/select")))
    select_element = Select(driver.find_element(
        By.XPATH, "//*[@id='root']/div/main/section[1]/div[3]/div[1]/div/div/div[1]/div/div/select")).first_selected_option
    time_slots_available = driver.find_element(By.XPATH, 
        "//*[@id='root']/div/main/section[1]/div[3]/div[2]/ul")
    all_li = time_slots_available.find_elements(By.TAG_NAME, "li")

    # Print out the findings
    print("First available date is: ")
    print(select_element.text, end=" ")
    print(driver.find_element(By.XPATH, "//*[@class='flatpickr-day selected']").text)
    print("Available timeslots: ")
    for li in all_li: 
        print(li.text)

# Run the function every 5 mins using a while loop and time.sleep()
while True:
    print("  ")
    print("**** Checking Availability ****")
    # Check availability in Sydney Passport Office
    check_appointment()

    # Wait for 5 mins
    time.sleep(300)
