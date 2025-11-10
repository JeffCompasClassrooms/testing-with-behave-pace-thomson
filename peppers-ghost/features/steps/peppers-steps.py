from behave import Given, When, Then
from selenium.webdriver import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@Given("I open the instructables peppers ghost page")
def step_open_page(context):
    context.behave_driver.get("https://www.instructables.com/Peppers-Ghost-Illusion-in-a-Small-Space/")


@Then("I expect that there is at least one picture there")
def step_check_for_picture(context):
    wait = WebDriverWait(context.behave_driver, 10) 
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img")))
    images = context.behave_driver.find_elements(By.CSS_SELECTOR, "img") 
    assert images != []