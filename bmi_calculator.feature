# Created by jjadh at 17-08-2022
Feature: BMI Calculator functionality

  Scenario: BMI(Body Mass Index)
    Given User is on BMI calculator page
    When User clicks on Age 20
    And User clicks on Gender Male
    And User clicks on Height 180
    And User clicks on Weight 60
    And User clicks on Calculate button
    Then User verify the result 18.5

