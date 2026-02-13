Feature: Order Transaction

    Scenario: verify order success message shown in details page
        Given Place item order with <username> and <password>
        And the user is on landing page
        When I login to portal with <username> and <password>
        And I navigate to orders page
        And select the orderId
        Then I should see the order details with order success message
        Examples:
      | username                | password    |
      | rahulshetty@gmail.com   | Iamking@000 |
    