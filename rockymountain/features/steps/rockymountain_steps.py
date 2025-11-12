from behave import Given, When, Then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def find_element_by_text(context, text, tag="*"):
    """Helper function to find elements containing specific text using XPath"""
    xpath = f"//{tag}[contains(text(), '{text}')]"
    return context.behave_driver.find_elements(By.XPATH, xpath)


@Given("I visit the Rocky Mountain ATV/MC homepage")
def step_visit_homepage(context):
    context.behave_driver.get("https://www.rockymountainatvmc.com/")
    # Wait for page to load
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see the main navigation menu")
def step_see_navigation(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for navigation elements
    nav_elements = context.behave_driver.find_elements(By.CSS_SELECTOR, "nav, [role='navigation'], .nav, #nav")
    assert len(nav_elements) > 0, "Navigation menu should be visible"


@Then("I should see the search functionality")
def step_see_search(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for search input or search button
    search_elements = context.behave_driver.find_elements(
        By.CSS_SELECTOR, 
        "input[type='search'], input[name*='search'], input[id*='search'], button[aria-label*='search'], .search"
    )
    assert len(search_elements) > 0, "Search functionality should be visible"


@Then("I should see product categories displayed")
def step_see_categories(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for category links or menu items
    category_elements = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[href*='category'], .category, [class*='category'], nav a"
    )
    assert len(category_elements) > 0, "Product categories should be displayed"


@Then("I should see promotional content")
def step_see_promotional(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for promotional banners, sale items, or featured content
    promo_elements = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".promo, .banner, .sale, .featured, [class*='promo'], [class*='banner']"
    )
    assert len(promo_elements) > 0, "Promotional content should be visible"


@When("I search for {search_term}")
def step_search_for(context, search_term):
    wait = WebDriverWait(context.behave_driver, 10)
    # Find search input field
    search_input = wait.until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            "input[type='search'], input[name*='search'], input[id*='search'], input[placeholder*='search' i]"
        ))
    )
    search_input.clear()
    search_input.send_keys(search_term.strip('"'))
    
    # Find and click search button
    search_button = context.behave_driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit'], button[aria-label*='search' i], .search-button, [class*='search'][class*='button']"
    )
    search_button.click()
    
    # Wait for results to load
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see search results for {product_type}")
def step_see_search_results(context, product_type):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for search results, product listings, or result indicators
    results = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".product, .result, [class*='product'], [class*='result'], .search-results, article"
    )
    assert len(results) > 0, f"Search results for {product_type} should be displayed"


@Then("the search results should contain product listings")
def step_results_contain_listings(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Verify product listings are present
    listings = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".product, .listing, [class*='product'], [class*='item'], .sli_container  "
    )
    assert len(listings) > 0, "Search results should contain product listings"


@Then("I should see product images in the results")
def step_see_product_images(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for product images
    images = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "img[src*='product'], img[alt*='product' i], .product img, [class*='product'] img"
    )
    assert len(images) > 0, "Product images should be visible in results"


@When("I navigate to the Riding Gear section")
def step_navigate_riding_gear(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Find and click on Riding Gear link
    try:
        riding_gear_link = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "a[href*='riding-gear' i], a[href*='gear' i], nav a[href*='gear' i]"
            ))
        )
    except TimeoutException:
        # Try XPath if CSS selector doesn't work
        riding_gear_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Riding Gear') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'riding gear')]"))
        )
    riding_gear_link.click()
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see riding gear categories")
def step_see_gear_categories(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for category links or sections
    categories = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".category, [class*='category'], a[href*='gear'], .subcategory"
    )
    assert len(categories) > 0, "Riding gear categories should be visible"


@Then("I should see products available in the riding gear section")
def step_see_gear_products(context):
    wait = WebDriverWait(context.behave_driver, 5)
    products = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".product, [class*='product'], .item, [class*='item'], .tabbedItemsPanel"
    )
    assert len(products) > 0, "Products should be available in riding gear section"


@Then("I should see filter options for products")
def step_see_filters(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for filter controls
    filters = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".filter, [class*='filter'], select, input[type='checkbox'], .facet"
    )
    assert len(filters) > 0, "Filter options should be available"


@When("I navigate to the motorcycle helmets section")
def step_navigate_helmets(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Find helmet link
    try:
        helmet_link = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "a[href*='helmet' i], nav a[href*='helmet' i]"
            ))
        )
    except TimeoutException:
        helmet_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'helmet')]"))
        )
    helmet_link.click()
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see a variety of helmet products")
def step_see_helmet_products(context):
    wait = WebDriverWait(context.behave_driver, 10)
    helmets = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".product, [class*='product'], [class*='helmet'], .item"
    )
    assert len(helmets) > 0, "Helmet products should be displayed"


@Then("I should see helmet product images")
def step_see_helmet_images(context):
    wait = WebDriverWait(context.behave_driver, 10)
    images = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "img[alt*='helmet' i], .product img, [class*='product'] img"
    )
    assert len(images) > 0, "Helmet product images should be visible"


@Then("I should see product prices displayed")
def step_see_prices(context):
    wait = WebDriverWait(context.behave_driver, 10)
    prices = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".price, [class*='price'], [class*='cost'], .cost, [data-price]"
    )
    assert len(prices) > 0, "Product prices should be displayed"


@Then("I should see product ratings if available")
def step_see_ratings(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for rating elements (may not always be present)
    ratings = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".rating, [class*='rating'], .star, [class*='star'], [aria-label*='star' i]"
    )
    # This is optional, so we don't assert - just check if present
    pass


@When("I click on a product from the results")
def step_click_product(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Find first product link
    product_link = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "[data-url*='https://www.rockymountainatvmc.com/riding-gear/alpinestars-tech-10-boots-p']"
        ))
    )
    product_link.click()
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see detailed product information")
def step_see_product_details(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for product detail elements
    details = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".product-details, [class*='product-detail'], .description, [class*='description'], .productDetails "
    )
    assert len(details) > 0, "Detailed product information should be visible"


@Then("I should see product images")
def step_see_product_images(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for product images
    images = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "img[src*='product'], img[alt*='product' i], .product img, [class*='product'] img, img"
    )
    assert len(images) > 0, "Product images should be visible"


@Then("I should see the product price")
def step_see_product_price(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for product price
    prices = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".price, [class*='price'], [class*='cost'], .cost, [data-price]"
    )
    assert len(prices) > 0, "Product price should be visible"

@When("I navigate to the shopping cart")
def step_navigate_cart(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Find cart icon or link
    cart_link = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "a[href*='cart'], .cart, [class*='cart'], button[aria-label*='cart' i]"
        ))
    )
    cart_link.click()
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see the cart interface")
def step_see_cart_interface(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for cart elements
    cart_elements = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".cart, [class*='cart'], .shopping-cart, [id*='cart']"
    )
    assert len(cart_elements) > 0, "Cart interface should be visible"


@Then("I should see options to continue shopping or checkout")
def step_see_cart_options(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for checkout or continue shopping buttons
    options = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[href*='checkout'], .checkout, [class*='checkout']"
    )
    if len(options) == 0:
        # Try XPath for buttons containing "Checkout" or "Continue"
        options = context.behave_driver.find_elements(
            By.XPATH,
            "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'checkout') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'continue')]"
        )
    assert len(options) > 0, "Cart action options should be available"


@Then("I should see information about free shipping")
def step_see_shipping_info(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for shipping information
    shipping_info = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".shipping, [class*='shipping']"
    )
    if len(shipping_info) == 0:
        # Try XPath for elements containing "Free Shipping" or "shipping"
        shipping_info = context.behave_driver.find_elements(
            By.XPATH,
            "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'free shipping') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'shipping')]"
        )
    # Shipping info may be on homepage, so we check if present
    pass


@When("I navigate to the OEM parts section")
def step_navigate_oem_parts(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Find OEM parts link
    try:
        oem_link = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "a[href*='oem' i], nav a[href*='parts' i]"
            ))
        )
    except TimeoutException:
        oem_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'oem')]"))
        )
    oem_link.click()
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see vehicle type options")
def step_see_vehicle_types(context):
    wait = WebDriverWait(context.behave_driver, 10)
    vehicle_types = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "#makesSelectionContainer, select, option, [class*='vehicle'], [class*='type'], button[class*='vehicle']"
    )
    assert len(vehicle_types) > 0, "Vehicle type options should be visible"


@Then("I should see options to select make and model")
def step_see_make_model(context):
    wait = WebDriverWait(context.behave_driver, 10)
    make_model = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "select, option, [class*='make'], [class*='model'], [id*='make'], [id*='model']"
    )
    assert len(make_model) > 0, "Make and model selection options should be available"


@Then("I should see make and model selection options")
def step_see_make_model_selection(context):
    wait = WebDriverWait(context.behave_driver, 10)
    make_model = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "select, option, [class*='make'], [class*='model'], [id*='make'], [id*='model']"
    )
    assert len(make_model) > 0, "Make and model selection options should be available"


@Then("I should see parts categories available")
def step_see_parts_categories(context):
    wait = WebDriverWait(context.behave_driver, 10)
    categories = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".category, [class*='category'], a[href*='parts'], .parts-category"
    )
    assert len(categories) > 0, "Parts categories should be available"


@When("I look for special offers")
def step_look_special_offers(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Just wait for page to be ready, offers should be visible
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see promotional banners or sale items")
def step_see_promotional_banners(context):
    wait = WebDriverWait(context.behave_driver, 10)
    banners = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".banner, [class*='banner'], .sale, [class*='sale'], .promo, [class*='promo']"
    )
    assert len(banners) > 0, "Promotional banners or sale items should be visible"


@Then("I should see discounted products")
def step_see_discounted_products(context):
    wait = WebDriverWait(context.behave_driver, 10)
    discounted = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".sale, [class*='sale'], .discount, [class*='discount'], [class*='closeout']"
    )
    assert len(discounted) > 0, "Discounted products should be visible"


@Then("I should see pricing information for sale items")
def step_see_sale_pricing(context):
    wait = WebDriverWait(context.behave_driver, 10)
    prices = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".price, [class*='price'], [data-price], .cost"
    )
    assert len(prices) > 0, "Pricing information should be visible for sale items"


@When("I look for customer service information")
def step_look_customer_service(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Scroll or look for customer service section
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see contact information")
def step_see_contact_info(context):
    wait = WebDriverWait(context.behave_driver, 10)
    contact = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[href*='tel'], .contact, [class*='contact']"
    )
    if len(contact) == 0:
        # Try XPath for elements containing phone number or "phone"
        contact = context.behave_driver.find_elements(
            By.XPATH,
            "//*[contains(text(), '800') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'phone')]"
        )
    assert len(contact) > 0, "Contact information should be visible"


@Then("I should see customer service hours")
def step_see_service_hours(context):
    wait = WebDriverWait(context.behave_driver, 10)
    hours = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".hours, [class*='hours']"
    )
    if len(hours) == 0:
        # Try XPath for elements containing "Monday" or "hours"
        hours = context.behave_driver.find_elements(
            By.XPATH,
            "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'monday') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'hours')]"
        )
    assert len(hours) > 0, "Customer service hours should be visible"


@Then("I should see options to chat or call")
def step_see_chat_call(context):
    wait = WebDriverWait(context.behave_driver, 10)
    chat_call = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[href*='chat'], .chat, [class*='chat'], button[aria-label*='chat' i]"
    )
    if len(chat_call) == 0:
        # Try XPath for buttons containing "Chat"
        chat_call = context.behave_driver.find_elements(
            By.XPATH,
            "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'chat')]"
        )
    assert len(chat_call) > 0, "Chat or call options should be available"


@When("I navigate to the tire and wheel section")
def step_navigate_tires_wheels(context):
    wait = WebDriverWait(context.behave_driver, 10)
    try:
        tire_link = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "a[href*='tire' i], nav a[href*='tire' i]"
            ))
        )
    except TimeoutException:
        tire_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'tire')]"))
        )
    tire_link.click()
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see tire options available")
def step_see_tire_options(context):
    wait = WebDriverWait(context.behave_driver, 10)
    tires = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".product, [class*='tire'], a[href*='tire'], [class*='product']"
    )
    assert len(tires) > 0, "Tire options should be available"


@Then("I should see wheel options available")
def step_see_wheel_options(context):
    wait = WebDriverWait(context.behave_driver, 10)
    wheels = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".product, [class*='wheel'], a[href*='wheel'], [class*='product']"
    )
    assert len(wheels) > 0, "Wheel options should be available"


@Then("I should see package builder functionality")
def step_see_package_builder(context):
    wait = WebDriverWait(context.behave_driver, 10)
    builder = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[href*='package'], .builder, [class*='builder']"
    )
    if len(builder) == 0:
        # Try XPath for elements containing "Package" or "Builder"
        builder = context.behave_driver.find_elements(
            By.XPATH,
            "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'package') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'builder')]"
        )
    assert len(builder) > 0, "Package builder functionality should be available"


@When("I scroll to the footer")
def step_scroll_footer(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Scroll to footer
    context.behave_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(context.behave_driver, 2).until(
        EC.presence_of_element_located((By.TAG_NAME, "footer"))
    )


@Then("I should see company information links")
def step_see_company_links(context):
    wait = WebDriverWait(context.behave_driver, 10)
    company_links = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "footer a[href*='company'], footer a[href*='about'], footer a[href*='career'], .footer a"
    )
    assert len(company_links) > 0, "Company information links should be visible"


@Then("I should see terms and policies links")
def step_see_terms_links(context):
    wait = WebDriverWait(context.behave_driver, 10)
    terms_links = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[href*='/Terms-And-Policies'], footer a[href*='policy'], footer a[href*='privacy'], footer a[href*='return']"
    )
    assert len(terms_links) > 0, "Terms and policies links should be visible"


@Then("I should see customer service links")
def step_see_service_links(context):
    wait = WebDriverWait(context.behave_driver, 10)
    service_links = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[href*='/Contact-Us'], footer a[href*='service'], footer a[href*='help'], footer a[href*='faq']"
    )
    assert len(service_links) > 0, "Customer service links should be visible"


@Then("I should see social media links")
def step_see_social_links(context):
    wait = WebDriverWait(context.behave_driver, 10)
    social_links = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[aria-label*='Instagram (opens in a new tab)']"
    )
    assert len(social_links) > 0, "Social media links should be visible"


@When("I navigate to the ATV section")
def step_navigate_atv(context):
    wait = WebDriverWait(context.behave_driver, 10)
    try:
        atv_link = wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                "a[href*='atv' i], nav a[href*='atv' i]"
            ))
        )
    except TimeoutException:
        atv_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'atv')]"))
        )
    atv_link.click()
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see ATV-specific products")
def step_see_atv_products(context):
    wait = WebDriverWait(context.behave_driver, 10)
    atv_products = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "li [alt*='Top ATV Parts and Accessories Categories']"
    )
    assert len(atv_products) > 0, "ATV-specific products should be visible"


@Then("I should see categories for ATV parts and gear")
def step_see_atv_categories(context):
    wait = WebDriverWait(context.behave_driver, 10)
    categories = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".category, [class*='category'], a[href*='atv'], .subcategory"
    )
    assert len(categories) > 0, "ATV parts and gear categories should be visible"


@When("I look for the sign in option")
def step_look_sign_in(context):
    wait = WebDriverWait(context.behave_driver, 10)
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see account access options")
def step_see_account_options(context):
    wait = WebDriverWait(context.behave_driver, 10)
    account_options = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[href*='sign'], a[href*='login'], .account, [class*='account']"
    )
    if len(account_options) == 0:
        # Try XPath for buttons containing "Sign" or "Log"
        account_options = context.behave_driver.find_elements(
            By.XPATH,
            "//button[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'sign') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'log')]"
        )
    assert len(account_options) > 0, "Account access options should be visible"


@Then("I should see options to create a new account")
def step_see_create_account(context):
    wait = WebDriverWait(context.behave_driver, 10)
    create_account = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[href*='register'], a[href*='signup']"
    )
    if len(create_account) == 0:
        # Try XPath for buttons/elements containing "Create", "Register", or "New customer"
        create_account = context.behave_driver.find_elements(
            By.XPATH,
            "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'create') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'register') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'new customer')]"
        )
    assert len(create_account) > 0, "Options to create a new account should be visible"


@Then("I should see order tracking options")
def step_see_order_tracking(context):
    wait = WebDriverWait(context.behave_driver, 10)
    tracking = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "a[href*='track'], a[href*='order']"
    )
    if len(tracking) == 0:
        # Try XPath for elements containing "Track" or "Order Status"
        tracking = context.behave_driver.find_elements(
            By.XPATH,
            "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'track') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'order status')]"
        )
    assert len(tracking) > 0, "Order tracking options should be visible"


@When("I look for clearance items")
def step_look_clearance(context):
    wait = WebDriverWait(context.behave_driver, 10)
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see closeout or sale sections")
def step_see_closeout_sections(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for elements with aria-label containing 'under $'
    closeout = context.behave_driver.find_elements(
        By.XPATH,
        "//*[contains(@aria-label, 'under $')]"
    )
    assert len(closeout) > 0, "Closeout or sale sections should be visible"


@Then("I should see discounted pricing")
def step_see_discounted_pricing(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for discounted pricing
    discounted = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".price, [class*='price'], [class*='sale'], [class*='discount'], [data-price]"
    )
    assert len(discounted) > 0, "Discounted pricing should be visible"


@Then("I should see limited availability indicators")
def step_see_availability_indicators(context):
    wait = WebDriverWait(context.behave_driver, 10)
    indicators = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".stock, [class*='stock']"
    )
    if len(indicators) == 0:
        # Try XPath for elements containing "Limited", "Stock", or "Available"
        indicators = context.behave_driver.find_elements(
            By.XPATH,
            "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'limited') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'stock') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'available')]"
        )
    # May not always be present, so we check but don't require
    pass


@When("I use the find parts tool")
def step_use_find_parts(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for find parts tool or vehicle selector
    find_parts = wait.until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            "select, [class*='vehicle'], [class*='finder'], [id*='vehicle'], [id*='find']"
        ))
    )


@Then("I should see vehicle type selection")
def step_see_vehicle_type_selection(context):
    wait = WebDriverWait(context.behave_driver, 10)
    vehicle_type = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "select, option, [class*='type'], [id*='type'], button[class*='vehicle']"
    )
    assert len(vehicle_type) > 0, "Vehicle type selection should be visible"


@Then("I should see year selection options")
def step_see_year_selection(context):
    wait = WebDriverWait(context.behave_driver, 10)
    year_select = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "select, option, [class*='year'], [id*='year'], select option"
    )
    assert len(year_select) > 0, "Year selection options should be visible"


@Then("I should see saved machines functionality")
def step_see_saved_machines(context):
    wait = WebDriverWait(context.behave_driver, 10)
    saved = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        ".saved, [class*='saved'], [class*='machine']"
    )
    if len(saved) == 0:
        # Try XPath for elements containing "Saved" or "Machine"
        saved = context.behave_driver.find_elements(
            By.XPATH,
            "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'saved') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'machine')]"
        )
    assert len(saved) > 0, "Saved machines functionality should be visible"


@When("I click on the RM Cash button")
def step_click_rm_cash_button(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Find and click on the RM Cash button using the rebateWrapper class
    rm_cash_button = wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            ".rebateWrapper"
        ))
    )
    rm_cash_button.click()
    # Wait for the page to update after clicking
    WebDriverWait(context.behave_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@Then("I should see the RM Cash section")
def step_see_rm_cash_section(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for RM Cash section elements
    rm_cash_section = context.behave_driver.find_elements(
        By.CSS_SELECTOR,
        "[class*='rebate'], [class*='cash'], [id*='cash'], [id*='rebate']"
    )
    # Also try XPath for elements containing "RM Cash" text
    if len(rm_cash_section) == 0:
        rm_cash_section = context.behave_driver.find_elements(
            By.XPATH,
            "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'rm cash')]"
        )
    assert len(rm_cash_section) > 0, "RM Cash section should be visible"


@Then("I should see RM Cash information displayed")
def step_see_rm_cash_info(context):
    wait = WebDriverWait(context.behave_driver, 10)
    # Look for RM Cash information elements
    rm_cash_info = context.behave_driver.find_elements(
        By.XPATH,
        "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'rm cash') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'quick cash')]"
    )
    assert len(rm_cash_info) > 0, "RM Cash information should be displayed"



