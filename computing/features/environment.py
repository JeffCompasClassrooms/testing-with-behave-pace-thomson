import behave_webdriver
from behave_webdriver.steps import *

def before_all(context):
    options = Options()
    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    context.behave_driver = webdriver.Chrome(options=options)

def after_all(context):
    context.behave_driver.quit()

