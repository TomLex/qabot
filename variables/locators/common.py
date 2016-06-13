BROWSER = 'chrome'

class XPATH:
    LANGUAGE_BUTTON = "//*[contains(@class, 'language-name')]"
    LANGUAGE_TEXT = None
    LANGUAGE_POPUP = "//*[@class='Popup NavbarLanguage-popup _shown']"
    CURRENCY_BUTTON = "//*[@class='currency-selected']"
    CURRENCY_POPUP = "//*[@class='Popup NavbarCurrency-popup _shown']"
    MENU = "//*[@class='SideNav _visible']"
    MENU_OPEN_BUTTON = "//*[@class='toggle-icon md-menu']"
    MENU_CLOSE_BUTTON = "//*[@class='SideNav-hide']"
    PASSENGERS_FIELD = "//*[@class='PassengersField']"
    PASSENGERS_NUMBER = PASSENGERS_FIELD + "//*[@class='PassengersPopup-value']"
    PASSENGERS_POPUP = PASSENGERS_FIELD + "//*[@class='Popup-content']"
    PASSENGERS_BUTTON_ADD = PASSENGERS_FIELD + "//*[@class='PassengersPopup-add']"
    PASSENGERS_BUTTON_REMOVE = PASSENGERS_FIELD + "//*[@class='PassengersPopup-remove']"
    CHECKBOX_ONEWAY_RETURN = "//*[@class='RadioButtons-option-radio-outer']"
    CHECKBOX_ONEWAY = 'xpath=({0})[1]'.format(CHECKBOX_ONEWAY_RETURN)
    CHECKBOX_RETURN = 'xpath=({0})[2]'.format(CHECKBOX_ONEWAY_RETURN)
    FLY_FROM_INPUT = "//*[@name='search-origin']"
    FLY_TO_INPUT = "//*[@name='search-destination']"
    FLY_FROM_OPTIONS = "//*[@class='ModalPicker spPicker origin']"
    FLY_TO_OPTIONS = "//*[@class='ModalPicker spPicker destination']"
    FLY_FROM_TO_OPTIONS_TEXT = "//td[@class='name']/span[contains(., '{0}')]"
    FLY_FROM_SELECT = FLY_FROM_OPTIONS + FLY_FROM_TO_OPTIONS_TEXT
    FLY_TO_SELECT = FLY_TO_OPTIONS + FLY_FROM_TO_OPTIONS_TEXT
    FILTERS = "//*[@class='Filters']"
    FILTER_DATE_OUTBOUND_BUTTON = "//*[contains(@class, 'outboundDate')]//*[contains(@class, 'head spCard')][1]"
    FILTER_DATE_OUTBOUND_POPUP = "//*[@class='ModalPicker spPicker outboundDate']"
    FILTER_DATE_INBOUND_BUTTON = "//*[contains(@class, 'outboundDate')]//*[contains(@class, 'head spCard'][2]"
    FILTER_DATE_INBOUND_POPUP = "//*[@class='ModalPicker spPicker inboundDate']"
    FILTER_DATE_MENU_CONCRETE = "//*[contains(@class, 'mode-single')]"
    FILTER_DATE_MENU_INTERVAL = "//*[contains(@class, 'mode-interval')]"
    FILTER_DATE_MENU_ANY = "//*[contains(@class, 'mode-anytime')]"
    FILTER_DATE_MENU_NIGHTS_TO_STAY = "//*[contains(@class, 'mode-timeToStay')]"
    FILTER_DATE_MENU_NO_RETURN = "//*[contains(@class, 'mode-noReturn')]"
    FILTER_DATE_NIGHTS_TO_STAY = "//*[@class='time-to-stay']"
    FILTER_DATE_NIGHTS_TO_STAY_LOW_HANDLE = FILTER_DATE_NIGHTS_TO_STAY + "//*[contains(@class, 'Slider low')]//*[@class='handle']"
    FILTER_DATE_NIGHTS_TO_STAY_HIGH_HANDLE = FILTER_DATE_NIGHTS_TO_STAY + "//*[contains(@class, 'Slider high')]//*[@class='handle']"
    FILTER_DATE_NIGHTS_TO_STAY_HANDLE_TEXT = FILTER_DATE_NIGHTS_TO_STAY + "//*[@class='content-headline']"
    FILTER_DATE_NIGHTS_TO_STAY_CONFIRM = FILTER_DATE_NIGHTS_TO_STAY + "//*[contains(@class, 'confirm-time-to-stay-button')]"
    FILTER_DAYTIMES_BUTTON = FILTERS + "//*[contains(@class, 'Filters-link') and contains(@class, 'dayTimes')]"
    FILTER_DAYTIMES_POPUP = FILTERS + "//*[@class='Popup _dayTimes _shown']"
    FILTER_DAYTIMES_DEPARTURE_ARRIVAL = FILTER_DAYTIMES_POPUP + "//div[contains(@class, 'SwitchButtons-option')"
    FILTER_DAYTIMES_CHECKBOX = FILTERS + "//*[@class='DayTimesPopup-direction-days']"
    FILTER_DAYTIMES_HOURS_LOW_HANDLE = FILTER_DAYTIMES_POPUP + "//*[@class='Slider low']//*[@class='handle']"
    FILTER_DAYTIMES_HOURS_HIGH_HANDLE = FILTER_DAYTIMES_POPUP + "//*[@class='Slider high']//*[@class='handle']"
    FILTER_DAYTIMES_OUTBOUND_DEPARTURE = FILTER_DAYTIMES_DEPARTURE_ARRIVAL + '[1]'
    FILTER_DAYTIMES_OUTBOUND_ARRIVAL = FILTER_DAYTIMES_DEPARTURE_ARRIVAL + '[2]'
    FILTER_DAYTIMES_OUTBOUND_CHECKBOX = FILTER_DAYTIMES_CHECKBOX + '[1]'
    FILTER_DAYTIMES_OUTBOUND_HOURS_LOW_HANDLE = FILTER_DAYTIMES_HOURS_LOW_HANDLE + '[1]'
    FILTER_DAYTIMES_OUTBOUND_HOURS_HIGH_HANDLE = FILTER_DAYTIMES_HOURS_HIGH_HANDLE + '[1]'
    FILTER_DAYTIMES_INBOUND_DEPARTURE = FILTER_DAYTIMES_DEPARTURE_ARRIVAL + '[3]'
    FILTER_DAYTIMES_INBOUND_ARRIVAL = FILTER_DAYTIMES_DEPARTURE_ARRIVAL + '[4]'
    FILTER_DAYTIMES_INBOUND_CHECKBOX = FILTER_DAYTIMES_CHECKBOX + '[2]'
    FILTER_DAYTIMES_INBOUND_HOURS_LOW_HANDLE = FILTER_DAYTIMES_HOURS_LOW_HANDLE + '[2]'
    FILTER_DAYTIMES_INBOUND_HOURS_HIGH_HANDLE = FILTER_DAYTIMES_HOURS_HIGH_HANDLE + '[2]'
    FILTER_PRICE_BUTTON = FILTERS + "//*[contains(@class, 'Filters-link') and contains(@class, 'price')]"
    FILTER_PRICE_POPUP = FILTERS + "//*[@class='Popup _price _shown']"
    FILTER_PRICE_RESET = FILTER_PRICE_POPUP + "//*[@class='spResetDarkBtn']"
    FILTER_PRICE_LOW_HANDLE = FILTER_PRICE_POPUP + "//*[@class='Slider low']//*[@class='handle']"
    FILTER_PRICE_HIGH_HANDLE = FILTER_PRICE_POPUP + "//*[@class='Slider high']//*[@class='handle']"
    FILTER_PRICE_HANDLE_TEXT = FILTER_PRICE_POPUP + '//*[contains(@class, PricePopup)]/span'
    FILTER_DURATION = FILTERS + "//*[contains(@class, 'Filters-link') and contains(@class, 'durations')]"
    FILTER_DURATION_POPUP = FILTERS + "//*[@class='Popup _durations _shown']"
    FILTER_DURATION_MAX_HOURS_HANDLE = FILTER_DURATION_POPUP + "//*[@class='SimpleSlider']//*[@class='handle']"
    FILTER_DURATION_TRANSFER_HOURS_LOW_HANDLE = FILTER_DURATION_POPUP + "//*[@class='Slider low']//*[@class='handle']"
    FILTER_DURATION_TRANSFER_HOURS_HIGH_HANDLE = FILTER_DURATION_POPUP + "//*[@class='Slider high']//*[@class='handle']"
    FILTER_OTHERS = FILTERS + "//*[contains(@class, 'Filters-link') and contains(@class, 'others')]"
    FILTER_OTHERS_CHECKBOX = FILTERS + "//*[@class='spCheckbox-wrapper']"
    FILTER_OTHERS_DIRECT_FLIGHTS = FILTER_OTHERS_CHECKBOX + "//input[@type='checkbox'][1]"
    FILTER_DATE_CHANGE_DAY = "//*[contains(@class, 'CalendarDay') and contains(@data-reactid, '{0}')]"
    FILTER_DATE_CHANGE_MONTH_OLD = "//*[contains(@class, 'prev ') and not(contains(@class, 'disabled'))]"
    FILTER_DATE_CHANGE_MONTH_NEW = "//*[contains(@class, 'next') and not(contains(@class, 'month')) and not(contains(@class, 'disabled'))]"
    FLIGHTS_AGGREGATE = "//*[contains(@class, 'AggregateResults')]"
    FLIGHTS_AGGREGATE_BUTTONS = FLIGHTS_AGGREGATE + "//*[contains(@class, 'photos')]"
    FLIGHTS_SEARCH_DETAIL = "//*[@class='SearchDetail']"
    FLIGHTS_JOURNEYS = "//*[contains(@class, 'Journey')]"


class CSS:
    FILTER_DAYTIMES_DIRECTIONS = "css=div[class~='DayTimesPopup'] div[class~='DayTimesPopup-direction']"
    FILTER_DAYTIMES_OUTBOUND = FILTER_DAYTIMES_DIRECTIONS + ':nth-child(2)'
    FILTER_DAYTIMES_INBOUND = FILTER_DAYTIMES_DIRECTIONS + ':nth-child(4)'
    FILTER_DAYTIMES_OUTBOUND_CHECKED_CHECKBOX = FILTER_DAYTIMES_OUTBOUND + " input[type='checkbox'].spCheckbox:checked"
    FILTER_DAYTIMES_OUTBOUND_UNCHECKED_CHECKBOX = FILTER_DAYTIMES_OUTBOUND + " input[type='checkbox'].spCheckbox:not(:checked)"
    FILTER_DAYTIMES_INBOUND_CHECKED_CHECKBOX = FILTER_DAYTIMES_INBOUND + " input[type='checkbox'].spCheckbox:checked"
    FILTER_DAYTIMES_INBOUND_UNCHECKED_CHECKBOX = FILTER_DAYTIMES_INBOUND + " input[type='checkbox'].spCheckbox:not(:unchecked)"
    FLIGHTS_AGGREGATE = 'css=.AggregateResults > div > div > .photos:nth-of-type(1) > .AggregateCard.spCard.spShadow-half.clearfix > img'
    FLIGHTS_JOURNEY = 'css=.SearchDetail > div > .Journey.spCard._no-radius.spShadow-half-2._one-way:nth-of-type(2) > .top-wrap > table.one-way > tbody > tr > td:nth-of-type(2) > table.TripInfo > tbody > tr > td.field-1'
    FLIGHTS_GO_TO_BOOKING = "css=a[href*='booking']"