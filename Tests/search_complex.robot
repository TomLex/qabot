*** Settings ***
Library   ../Resources/CustomSeleniumLibrary.py

Test Setup  Begin FE Test
Test Teardown  End FE Test

*** Variable ***
${FLY_FROM}  STN
${FLY_TO}  PRG
${TYPE}  return
${PASSENGERS}  5
${PRICE_FROM}  100
${PRICE_TO}  200


*** Test Cases ***
Search on SkyPicker
    go to  http://www.skypicker.com
    ##search  ${TYPE}  ${FLY_FROM}  ${FLY_TO}  ${PASSENGERS}  ${PRICE_FROM}  ${PRICE_TO}
    fill fly from  STN
    fill fly to  PRG
    click element  xpath=//*[@class="SearchForm-multicity-wrapper"]
    #filter daytime outbound set hour from  10
    change flight type  return
    change passengers number  4
    filter price  5  5
    filter daytime outbound set days  4

