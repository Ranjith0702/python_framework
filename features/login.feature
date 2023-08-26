

Feature: Purchase a product
  Scenario: Search a product
    Given I am on homepage
    When I search a product
    Then I should see the product page
#    When  I need to logout from Amazon