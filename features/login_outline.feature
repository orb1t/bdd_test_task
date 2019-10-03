Feature: Instagram Android App LogIn functionality

  As an application user,
  I should be able to log in to applications using correct credentials.

  Background:
    Given Instagram app is running
    And 'SignedOutActivity' screen is opened

  Scenario Outline: Login with correct credentials
    When I login with "<EMAIL>" and "<PASSWORD>"
    Then log in was "<EXPECTED OUTCOME>"
    Examples:
      | EMAIL             | PASSWORD    | EXPECTED OUTCOME |
      | dvg1101@gmail.com | q1w2e3r4t5  | successful       |
      | werfgsg           | q1w2e3r4t5  | failed           |
      | dvg1101@gmail.com | zdghnm      | failed           |
