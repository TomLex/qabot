*** Settings ***
Library  ../Resources/CustomSeleniumLibrary

#Test Setup  Begin FE Test
#Test Teardown  End FE Test

*** Variable ***
${FLY_FROM}  STN
${FLY_TO}  PRG
${TYPE}  return
${PASSENGERS}  5
${PRICE_FROM}  100
${PRICE_TO}  200


*** Test Cases ***
Search on SkyPicker
    go to  https://kiwi.com
    ##search  ${TYPE}  ${FLY_FROM}  ${FLY_TO}  ${PASSENGERS}  ${PRICE_FROM}  ${PRICE_TO}
    fill fly from  STN
    fill fly to  PRG
    #click element  xpath=//*[@class="SearchForm-multicity-wrapper"]
    change flight type  return
    #change flight type  oneway
    filter change outbound date
    filter change inbound date
    filter change inbound date  nights_to_stay=3,5
    #filter daytime outbound set hour from  10
    change passengers number  4
    #filter price  100  200
    #filter price  5  5
    change language  cz
    change currency  EUR
    show menu
    sleep  3
    hide menu
