*** Settings ***
Documentation  Suite description
Library  ../Resources/CustomSeleniumLibrary.py

Test Setup  Begin FE Test
Test Teardown  End FE Test

*** Test Cases ***
Light Search on Kiwi.com
    go to  https://kiwi.com
    go to booking easy
