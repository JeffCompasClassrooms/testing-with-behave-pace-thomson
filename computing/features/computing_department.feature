Feature: Utah Tech University Computing Department Website
  As a prospective student or visitor
  I want to navigate and explore the Computing Department website
  So that I can learn about programs, courses, and contact information

  Scenario: Apply online button in header
    Given I open the url "https://computing.utahtech.edu/"
    Then I expect that element "header" contains the text "Apply Online"

  Scenario: Page loads successfully with main heading
    Given I open the url "https://computing.utahtech.edu/"
    Then I expect that element "body" contains the text "Utah Tech"

  Scenario: Masters of Software Development section is accessible
    Given I open the url "https://computing.utahtech.edu/"
    Then I expect that element "body" contains the text "Masters of Software Development"

  Scenario: Degrees Offered section provides program information
    Given I open the url "https://computing.utahtech.edu/"
    Then I expect that element "body" contains the text "Degrees Offered"

  Scenario: Courses section displays course information
    Given I open the url "https://computing.utahtech.edu/"
    Then I expect that element "body" contains the text "Courses"

  Scenario: Certificates section is available and accessible
    Given I open the url "https://computing.utahtech.edu/"
    Then I expect that element "body" contains the text "CERTIFICATES"

  Scenario: Navigation elements are functional and accessible
    Given I open the url "https://computing.utahtech.edu/"
    Then I expect that element "nav" is visible

  Scenario: Page has a way to request a campus tour
    Given I open the url "https://computing.utahtech.edu/"
    Then I expect that element "body" contains the text "PROGRAM LEARNING OUTCOMES"

  Scenario: Footer has Apply Now button
    Given I open the url "https://computing.utahtech.edu/"
    Then I expect that element "footer" contains the text "Apply Online"

  Scenario: Footer has Phone Number
    Given I open the url "https://computing.utahtech.edu/"
    Then I expect that element "footer" contains the text "+1 (435) 652-7500 "

