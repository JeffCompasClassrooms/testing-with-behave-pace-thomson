import behave_webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    # chrome_options.binary_location = "/usr/bin/chromium-browser"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    # Use behave-webdriver’s Chrome wrapper
    context.behave_driver = behave_webdriver.Chrome(chrome_options=chrome_options)

def after_all(context):
    if hasattr(context, "behave_driver"):
        context.behave_driver.quit()

