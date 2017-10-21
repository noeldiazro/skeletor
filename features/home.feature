Feature: Home page

    Scenario: Home page request
        When home page is requested
        Then page title contains "Home"
