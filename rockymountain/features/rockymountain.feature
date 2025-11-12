Feature: Rocky Mountain ATV/MC E-commerce Website
  As a customer shopping for ATV, UTV, and motorcycle parts and gear
  I want to browse, search, and interact with the Rocky Mountain ATV/MC website
  So that I can find and purchase the products I need

  Scenario: Homepage loads with main navigation and content
    Given I visit the Rocky Mountain ATV/MC homepage
    Then I should see the main navigation menu
    And I should see the search functionality
    And I should see product categories displayed
    And I should see promotional content

  Scenario: I can search for products using the search feature
    Given I visit the Rocky Mountain ATV/MC homepage
    When I search for "helmets"
    Then I should see search results for helmets
    And the search results should contain product listings

  Scenario: I can navigate to the Riding Gear section
    Given I visit the Rocky Mountain ATV/MC homepage
    When I navigate to the Riding Gear section
    Then I should see riding gear categories
    And I should see products available in the riding gear section

  Scenario: I can view product details for a specific item
    Given I visit the Rocky Mountain ATV/MC homepage
    When I search for "motocross boots"
    And I click on a product from the results
    Then I should see detailed product information
    And I should see product images
    And I should see the product price

  Scenario: I can access the shopping cart
    Given I visit the Rocky Mountain ATV/MC homepage
    When I navigate to the shopping cart
    Then I should see the cart interface
    And I should see options to continue shopping or checkout
    And I should see information about free shipping

  Scenario: I can browse OEM parts by vehicle type
    Given I visit the Rocky Mountain ATV/MC homepage
    When I navigate to the OEM parts section
    Then I should see vehicle type options
    And I should see options to select make and model
    And I should see parts categories available

  Scenario: I can view special offers and sales
    Given I visit the Rocky Mountain ATV/MC homepage
    When I look for special offers
    Then I should see promotional banners or sale items
    And I should see discounted products
    And I should see pricing information for sale items

  Scenario: I can access customer service information
    Given I visit the Rocky Mountain ATV/MC homepage
    When I look for customer service information
    Then I should see contact information
    And I should see customer service hours
    And I should see options to chat or call

  Scenario: I can browse tire and wheel packages
    Given I visit the Rocky Mountain ATV/MC homepage
    When I navigate to the tire and wheel section
    Then I should see tire options available
    And I should see wheel options available
    And I should see package builder functionality

  Scenario: I can view the company information and policies
    Given I visit the Rocky Mountain ATV/MC homepage
    When I scroll to the footer
    Then I should see company information links
    And I should see terms and policies links
    And I should see customer service links
    And I should see social media links

  Scenario: I can browse products by vehicle category
    Given I visit the Rocky Mountain ATV/MC homepage
    When I navigate to the ATV section
    Then I should see ATV-specific products
    And I should see categories for ATV parts and gear

  Scenario: I can access my account or sign in
    Given I visit the Rocky Mountain ATV/MC homepage
    When I look for the sign in option
    Then I should see account access options
    And I should see options to create a new account
    And I should see order tracking options

  Scenario: I can browse clearance or closeout items
    Given I visit the Rocky Mountain ATV/MC homepage
    When I look for clearance items
    Then I should see closeout or sale sections
    And I should see discounted pricing
    And I should see limited availability indicators

  Scenario: I can use the vehicle finder tool
    Given I visit the Rocky Mountain ATV/MC homepage
    When I use the find parts tool
    Then I should see vehicle type selection
    And I should see year selection options
    And I should see make and model selection options
    And I should see saved machines functionality

  Scenario: I can access the RM Cash section
    Given I visit the Rocky Mountain ATV/MC homepage
    When I click on the RM Cash button
    Then I should see the RM Cash section
    And I should see RM Cash information displayed

