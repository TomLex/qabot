# -*- coding: utf-8 -*-

BROWSER = "chrome"
XPATH_CURRENCY_BUTTON = "//*[@class='currency-selected']"
XPATH_CURRENCY_TEXT = XPATH_CURRENCY_BUTTON + "//*[contains(@class, 'currency-code')]/span[1]"
XPATH_CURRENCY_POPUP = "//*[@class='Popup NavbarCurrency-popup _shown']"
XPATH_LANGUAGE_BUTTON = "//*[contains(@class, 'language-name')]"
XPATH_LANGUAGE_TEXT = None
XPATH_LANGUAGE_POPUP = "//*[@class='Popup NavbarLanguage-popup _shown']"
XPATH_MENU = "//*[@class='SideNav _visible']"
XPATH_MENU_OPEN_BUTTON = "//*[@class='toggle-icon md-menu']"
XPATH_MENU_CLOSE_BUTTON = XPATH_MENU + "//*[@class='SideNav-hide']"


XPATH_FILTERS = "//*[@class='Filters']"

XPATH_FILTER_DAYTIMES_BUTTON = XPATH_FILTERS + "//*[contains(@class, 'Filters-link') " \
                                                  " and contains(@class, 'dayTimes')]"
XPATH_FILTER_DAYTIMES_POPUP = XPATH_FILTERS + "//*[@class='Popup _dayTimes _shown']"
XPATH_FILTER_DAYTIMES_DEPARTURE = XPATH_FILTER_DAYTIMES_POPUP + "//div[contains(@class, 'SwitchButtons-option') " \
                                                                "and contains(@data-reactid, 'departure')]"
XPATH_FILTER_DAYTIMES_ARRIVAL = XPATH_FILTER_DAYTIMES_POPUP + "//div[contains(@class, 'SwitchButtons-option') " \
                                                                "and contains(@data-reactid, 'arrival')]"
XPATH_FILTER_DAYTIMES_CHECKBOX = XPATH_FILTERS + "//*[@class='DayTimesPopup-direction-days']"
XPATH_FILTER_DAYTIMES_HOURS_LEFT_HANDLE = XPATH_FILTER_DAYTIMES_POPUP + "//*[@class='Slider low']//*[@class='handle']"
XPATH_FILTER_DAYTIMES_HOURS_RIGHT_HANDLE = XPATH_FILTER_DAYTIMES_POPUP + "//*[@class='Slider high']//*[@class='handle']"


XPATH_FILTER_DAYTIMES_OUTBOUND_DEPARTURE = XPATH_FILTER_DAYTIMES_DEPARTURE + "[1]"
XPATH_FILTER_DAYTIMES_OUTBOUND_ARRIVAL = XPATH_FILTER_DAYTIMES_ARRIVAL + "[1]"
XPATH_FILTER_DAYTIMES_OUTBOUND_CHECKBOX = XPATH_FILTER_DAYTIMES_CHECKBOX + "[1]"
XPATH_FILTER_DAYTIMES_OUTBOUND_HOURS_LEFT_HANDLE = XPATH_FILTER_DAYTIMES_HOURS_LEFT_HANDLE + "[1]"
XPATH_FILTER_DAYTIMES_OUTBOUND_HOURS_RIGHT_HANDLE = XPATH_FILTER_DAYTIMES_HOURS_RIGHT_HANDLE + "[1]"
XPATH_FILTER_DAYTIMES_INBOUND_DEPARTURE = XPATH_FILTER_DAYTIMES_DEPARTURE + "[2]"
XPATH_FILTER_DAYTIMES_INBOUND_ARRIVAL = XPATH_FILTER_DAYTIMES_ARRIVAL + "[2]"
XPATH_FILTER_DAYTIMES_INBOUND_CHECKBOX = XPATH_FILTER_DAYTIMES_CHECKBOX + "[2]"
XPATH_FILTER_DAYTIMES_INBOUND_HOURS_LEFT_HANDLE = XPATH_FILTER_DAYTIMES_HOURS_LEFT_HANDLE + "[2]"
XPATH_FILTER_DAYTIMES_INBOUND_HOURS_RIGHT_HANDLE = XPATH_FILTER_DAYTIMES_HOURS_RIGHT_HANDLE + "[2]"


CSS_FILTER_DAYTIMES_DIRECTIONS = "css=div[class~='DayTimesPopup'] div[class~='DayTimesPopup-direction']"
CSS_FILTER_DAYTIMES_OUTBOUND = CSS_FILTER_DAYTIMES_DIRECTIONS + ":nth-child(2)"
CSS_FILTER_DAYTIMES_INBOUND = CSS_FILTER_DAYTIMES_DIRECTIONS + ":nth-child(4)"
CSS_FILTER_DAYTIMES_OUTBOUND_CHECKED_CHECKBOX = CSS_FILTER_DAYTIMES_OUTBOUND\
                                                + " input[type='checkbox'].spCheckbox:checked"
CSS_FILTER_DAYTIMES_OUTBOUND_UNCHECKED_CHECKBOX = CSS_FILTER_DAYTIMES_OUTBOUND\
                                                  + " input[type='checkbox'].spCheckbox:not(:checked)"
CSS_FILTER_DAYTIMES_INBOUND_CHECKED_CHECKBOX = CSS_FILTER_DAYTIMES_INBOUND\
                                               + " input[type='checkbox'].spCheckbox:checked"
CSS_FILTER_DAYTIMES_INBOUND_UNCHECKED_CHECKBOX = CSS_FILTER_DAYTIMES_INBOUND\
                                                 + " input[type='checkbox'].spCheckbox:not(:unchecked)"


XPATH_FLY_FROM_INPUT = "//*[@name='search-origin']"
XPATH_FLY_FROM_OPTIONS = "//*[@class='ModalPicker spPicker origin']"
XPATH_FLY_TO_INPUT = "//*[@name='search-destination']"

XPATH_FLY_TO_OPTIONS = "//*[@class='ModalPicker spPicker destination']"
XPATH_FLY_FROM_SELECT = XPATH_FLY_FROM_OPTIONS\
                        + "//tr[@data-reactid['{0}' = substring(., string-length(.) - string-length('{1}') + 1)]]"
XPATH_FLY_TO_SELECT = XPATH_FLY_TO_OPTIONS\
                      + "//tr[@data-reactid['{0}' = substring(., string-length(.) - string-length('{1}') + 1)]]"


XPATH_CHECKBOX_ONEWAY_RETURN = "//*[@class='RadioButtons-option-radio-outer']"
XPATH_CHECKBOX_ONEWAY = "xpath=({0})[1]".format(XPATH_CHECKBOX_ONEWAY_RETURN)
XPATH_CHECKBOX_RETURN = "xpath=({0})[2]".format(XPATH_CHECKBOX_ONEWAY_RETURN)


XPATH_PASSENGERS_FIELD = "//*[@class='PassengersField']"
XPATH_PASSENGERS_NUMBER = XPATH_PASSENGERS_FIELD + "//*[@class='PassengersField-note-value']/span[1]"
XPATH_PASSENGERS_POPUP = XPATH_PASSENGERS_FIELD + "//*[@class='Popup-content']"
XPATH_PASSENGERS_BUTTON_ADD = XPATH_PASSENGERS_FIELD + "//*[@class='PassengersPopup-add']"
XPATH_PASSENGERS_BUTTON_REMOVE = XPATH_PASSENGERS_FIELD + "//*[@class='PassengersPopup-remove']"


XPATH_FILTERS = "//*[@class='Filters']"


XPATH_FILTER_PRICE_BUTTON = XPATH_FILTERS + "//*[contains(@class, 'Filters-link') and contains(@class, 'price')]"
XPATH_FILTER_PRICE_POPUP = XPATH_FILTERS + "//*[@class='Popup _price _shown']"
XPATH_FILTER_PRICE_RESET = XPATH_FILTER_PRICE_POPUP + "//*[@class='spResetDarkBtn']"
XPATH_FILTER_PRICE_LEFT_HANDLE = XPATH_FILTER_PRICE_POPUP + "//*[@class='Slider low']//*[@class='handle']"
XPATH_FILTER_PRICE_RIGHT_HANDLE = XPATH_FILTER_PRICE_POPUP + "//*[@class='Slider high']//*[@class='handle']"


XPATH_FILTER_DURATION = XPATH_FILTERS + "//*[contains(@class, 'Filters-link') and contains(@class, 'durations')]"
XPATH_FILTER_DURATION_POPUP = XPATH_FILTERS + "//*[@class='Popup _durations _shown']"
XPATH_FILTER_DURATION_MAX_HOURS_HANDLE = XPATH_FILTER_DURATION_POPUP\
                                         + "//*[@class='SimpleSlider']//*[@class='handle']"
XPATH_FILTER_DURATION_TRANSFER_HOURS_LEFT_HANDLE = XPATH_FILTER_DURATION_POPUP\
                                                   + "//*[@class='Slider low']//*[@class='handle']"
XPATH_FILTER_DURATION_TRANSFER_HOURS_RIGHT_HANDLE = XPATH_FILTER_DURATION_POPUP\
                                                    + "//*[@class='Slider high']//*[@class='handle']"

XPATH_FILTER_OTHERS = XPATH_FILTERS + "//*[contains(@class, 'Filters-link') and contains(@class, 'others')]"
XPATH_FILTER_OTHERS_CHECKBOX = XPATH_FILTERS + "//*[@class='spCheckbox-wrapper']"
XPATH_FILTER_OTHERS_DIRECT_FLIGHTS = XPATH_FILTER_OTHERS_CHECKBOX + "//input[@type='checkbox'][1]"
