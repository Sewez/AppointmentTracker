from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException

import time
import os

# Define a function to check appointment availability
def check_appointment(driver):

    # Open the website / Change the URL for other passport offices.
    driver.get("https://australianpassportofficesydney.setmore.com/")
    # time.sleep(3)

    # # Wait and then Click OK on popup window
    
    
    # Wait for the element to be visible
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, 
            "//*[@id='products-list']/div[1]/div[1]/div[2]/div/h3/a")))

    # Find and dismiss the cookie notice
    cookie_notice = driver.find_element(By.XPATH,
            "//*[@id='brand-provider']/div[1]/main/div[2]/div/div[1]/div/div/div[3]/div[1]/button")

    cookie_notice.click()
    # Scroll to the element
    driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Click on the element
    element.click()

    # Click on the service "Authentication or Apostille"
    # service = driver.find_element(By.XPATH, 
    #         "//*[@id='products-list']/div[1]/div[1]/div[2]/div/h3/a")
    # service.click()

    # driver.get("https://australianpassportofficesydney.setmore.com/beta/book?step=time-slot&products=s1e7e4f603b866e2c8fb1315a7fcd3132be57a05a&type=service&staff=SKIP&staffSelected=false")
    # Wait for the calendar to load


    try: 
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//*[@id='brand-provider']/main/div[2]/div/div[1]/div/div/div/div[2]/ul")))
        select_element = driver.find_element(
            By.XPATH, "//*[@id='brand-provider']/main/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/table/tbody/tr[4]/td[4]/span/button/span[1]")
        time_slots_available = driver.find_element(By.XPATH, 
            "//*[@id='brand-provider']/main/div[2]/div/div[1]/div/div/div/div[2]/ul")
        all_li = time_slots_available.find_elements(By.TAG_NAME, "li")

        # Display a popup window with the first_date
        first_date = int(select_element.text)

        if first_date < 24:
            os.system(f"osascript -e 'display dialog \"{first_date}\" with title \"First Available Date\"'")

        # Print out the findings
        # print("First available date is: ")
        # print(select_element.text, end=" ")
        print()
        available_date = driver.find_element(By.XPATH, "//*[@id='heading-slot-date']")

        # Convert available_date to a datetime object

        available_date_str = available_date.text
        available_date_obj = datetime.strptime(available_date_str, "%A %d %B %Y")

        if available_date_obj < datetime(2024, 7, 18) and available_date_obj > datetime(2024, 7, 16):
            os.system(f"osascript -e 'display dialog \"{available_date_obj}\" with title \"First Available Date\"'")

        # print("Available date as datetime object: ", available_date_obj)
        print(available_date.text)
        print()
        print("Available timeslots: ")
        for li in all_li: 
            print(li.text)

    except TimeoutException:
        print("No available date found")

if __name__ == "__main__":
    # Create a webdriver instance
    driver = webdriver.Chrome()
    # Run the function every 5 mins using a while loop and time.sleep()
    while True:
        print("  ")
        print("**** Checking Availability ****")
        # Check availability in Sydney Passport Office

        check_appointment(driver)

        print("\n\n")
        # Wait for 1 mins
        time.sleep(60)
