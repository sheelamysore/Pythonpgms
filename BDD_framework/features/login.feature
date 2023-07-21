#Author: your.email@your.domain.com
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template
@tag
Feature: Login feature of Orange HRM website

  Background: Set-up for orange HRM
    Given User has launched Chrome Browser
    When the User has navigate to the Orange HRM login page

  Scenario: Navigation to Orange HRM web page
    Then the User should see the login options
    And the browser should close

  Scenario: Login to Orange HRM web page
    When the User enters valid username and password
    Then the User should successfully login

  @runfirst
  Scenario: Login to Orange HRM web page with parameters
    When the User enters valid "Admin" and "admin123"
    Then the User should successfully login
  
  @runsecond  
  Scenario Outline: Login to Orange HRM web page with parameters
    When the User enters valid "<username>" and "<password>"
    Then verify the "<webpage_URL>" for valid and invalid login
    Examples: 
    |username|password|webpage_URL|
    |Admin|admin123|/dashboard/index|
    |Admin|shjsdd|index.php/auth/login|
    |dfdsf|admin123|index.php/auth/login|
    |sdmfn|dfsbnn|index.php/auth/login|
    
    
