*** Settings ***
Documentation  Suite description
Library  ../Resources/CustomSeleniumLibrary.py
Library  XvfbRobot

Test Setup  Begin Test
Test Teardown  End Test

*** Test Cases ***
Light Search on Kiwi.com
    go to  https://kiwi.com
    go to booking easy
