# Requirements

Write a behavior test suite for each of two different web applications, using Gherkin-style feature scenarios and step definitions to implement the corresponding contexts, actions, and expectations. Use behave, behave-webdriver, and ChromeDriver to implement your test suites.

- For the first test suite, choose a basic web application to test. Assume the existing behaviors of the application are correct.
    - Implement at least 10 scenarios, using the built-in step definitions provided by behave-webdriver.
  
- For the second test suite, choose a more feature-rich web application to test. Assume the existing behaviors of the application are correct.
    - Implement at least 15 scenarios, using your own custom-written step definitions. Use the built-in step definitions provided by behave-webdriver as a point of reference as you write your custom step definitions.
    - All of your scenario steps should be written contextually to clearly describe the web application under test.
        - A good example: And I search for "shoes"
        - A not-so-good example: And I enter "shoes" into the input element "#search-field", And I click the element "#search-button"

- Intentionally plan and design your scenarios to fully evaluate the feature(s) under test. Strive to find the right balance in the number of steps for each scenario. An average of about 5 steps per scenario is appropriate.
- Your submission will be evaluated according to the quality, variety, coverage, and intentional design of your scenarios and steps. You will be graded according to the completeness and correctness of your test suite.