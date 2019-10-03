Feature: Instagram Android App LogIn functionality

  As an application user,
  I should be able to log in to applications using correct credentials.

  Background:
    Given Instagram app is running
    And 'SignedOutActivity' screen is opened

  Scenario: Login with correct credentials
    When I login with "dvg1101@gmail.com" and "q1w2e3r4t5"
    Then I am on main page


  Scenario: Login with incorrect login
    When I login with "werfgsg" and "q1w2e3r4t5"
    Then 'IncorrectCredentials' dialog is shown

  Scenario: Login with incorrect password
    When I login with "dvg1101@gmail.com" and "zdghnm"
    Then 'IncorrectCredentials' dialog is shown