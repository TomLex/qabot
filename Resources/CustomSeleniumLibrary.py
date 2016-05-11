# -*- coding: utf-8 -*-
import re

# TODO remove logger
from robot.api import logger
from Selenium2Library import Selenium2Library

from Variables.Common import *

class CustomSeleniumLibrary(Selenium2Library):
    ### COMMON METHODS
    def begin_fe_test(self):
        self.open_browser('about:blank', browser='chrome')
        self.maximize_browser_window()

    def end_fe_test(self):
        self.close_browser()

    def show_element(self, element, button):
        if not self._is_visible(element):
            self.click_element(button)
        self.wait_until_page_contains_element(element)

    def hide_element(self, element, button):
        if self._is_visible(element):
            self.click_element(button)
        self.wait_until_page_contains_element(element)

    def move_slider(self, slider, x_offset, y_offset):
        self.drag_and_drop_by_offset(slider, x_offset, y_offset)

    def scroll_page_to_element(self, location):
        self.execute_javascript("document.evaluate('${location}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE , null).singleNodeValue.scrollIntoView(true);")

    def is_visible(self, element):
        return self._is_visible(element)

    ### TOP NAVBAR
    def change_currency(self, currency):
        currency = currency.lower()
        actual_currency = self.get_text(XPATH_CURRENCY_TEXT)
        if actual_currency != currency:
            self.click_element(XPATH_CURRENCY_BUTTON)
            self.wait_until_page_contains_element(XPATH_CURRENCY_POPUP)
            self.click_element("//*[contains(@class, 'currency-option ') and contains(@data-reactid, '{0}')]".format(currency))

    def change_language(self, language_code):
        language_code = language_code.lower()
        self.click_element(XPATH_LANGUAGE_BUTTON)
        self.wait_until_page_contains_element(XPATH_LANGUAGE_POPUP)
        self.click_element("//*[contains(@class, 'language _single ') and contains(@data-reactid, '${language_code}')]")

    def show_menu(self):
        self.click_element(XPATH_MENU_OPEN_BUTTON)
        self.wait_until_page_contains_element(XPATH_MENU)

    def hide_menu(self):
        self.click_link(XPATH_MENU_CLOSE_BUTTON)

    ### SEARCH PAGE
    def search(self, flight_type, fly_from, fly_to, passengers_num, price_from, price_to):
        self.change_flight_type(flight_type)
        self.fill_fly_from(fly_from)
        self.fill_fly_to(fly_to)
        self.change_passengers_number(passengers_num)
        self.filter_price(price_from, price_to)
        self.click_element("xpath=//*[@class='SearchForm-multicity-wrapper']")
        self.choose_flight(1)

    def go_to_booking(self):
        self.scroll_page_to_element("xpath=//*[@class='btn-inner']")
        self.click_element("xpath=//*[@class='btn-inner']")

    # TODO
    def search_sort(self, sort_type):
        pass

    def change_flight_type(self, flight_type):
        if flight_type == 'oneway':
            self.click_element(XPATH_CHECKBOX_ONEWAY)
        elif flight_type == 'return':
            self.click_element(XPATH_CHECKBOX_RETURN)
        else:
            raise Exception("Unknown flight type!")

    def change_passengers_number(self, passengers_num):
        if not self.is_visible(XPATH_PASSENGERS_POPUP):
            self.click_element(XPATH_PASSENGERS_FIELD)
        actual_passengers = self.get_text(XPATH_PASSENGERS_NUMBER)
        if actual_passengers < passengers_num:
            self.click_element(XPATH_PASSENGERS_BUTTON_ADD)
            self.change_passengers_number(passengers_num)
        if actual_passengers > passengers_num:
            self.click_element(XPATH_PASSENGERS_BUTTON_REMOVE)
            self.change_passengers_number(passengers_num)

    def fill_fly_from(self, fly_from):
        self.wait_until_page_contains_element(XPATH_FLY_FROM_INPUT)
        self.input_text(XPATH_FLY_FROM_INPUT, fly_from)
        self.wait_until_page_contains_element(XPATH_FLY_FROM_SELECT.format(fly_from, fly_from))
        self.click_element(XPATH_FLY_FROM_SELECT.format(fly_from, fly_from))

    def fill_fly_to(self, fly_to):
        self.wait_until_page_contains_element(XPATH_FLY_TO_INPUT)
        self.input_text(XPATH_FLY_TO_INPUT, fly_to)
        self.wait_until_page_contains_element(XPATH_FLY_TO_SELECT.format(fly_to, fly_to))
        self.click_element(XPATH_FLY_TO_SELECT.format(fly_to, fly_to))

    def choose_flight(self, index):
        self.wait_until_page_contains_element("//div[@class='Journey spCard _no-radius spShadow-half-2 _one-way']")
        self.click_element("//div[@class='Journey spCard _no-radius spShadow-half-2 _one-way']")

    def filter_price(self, price_from, price_to):
        self.click_element(XPATH_FILTER_PRICE_BUTTON)
        self.move_slider(XPATH_FILTER_PRICE_LEFT_HANDLE, 20, 0)
        self.move_slider(XPATH_FILTER_PRICE_RIGHT_HANDLE, -20, 0)
        self.click_element(XPATH_FILTER_PRICE_RESET)

    def filter_daytime_outbound_set_type(self, filter_type):
        self.show_element(XPATH_FILTER_DAYTIMES_POPUP, XPATH_FILTER_DAYTIMES_BUTTON)
        if filter_type == 'departure':
            self.click_element(XPATH_FILTER_DAYTIMES_OUTBOUND_DEPARTURE)
        elif filter_type == 'arrival':
            self.click_element(XPATH_FILTER_DAYTIMES_OUTBOUND_ARRIVAL)
        else:
            raise Exception("Unknown filter type!")

    def filter_daytime_inbound_set_type(self, filter_type):
        self.show_element(XPATH_FILTER_DAYTIMES_POPUP, XPATH_FILTER_DAYTIMES_BUTTON)
        if filter_type == 'departure':
            self.click_element(XPATH_FILTER_DAYTIMES_INBOUND_DEPARTURE)
        elif filter_type == 'arrival':
            self.click_element(XPATH_FILTER_DAYTIMES_INBOUND_ARRIVAL)
        else:
            raise Exception("Unknown filter type!")

    def filter_daytime_outbound_set_hour_from_adapter(self, hour_from):
        self.show_element(XPATH_FILTER_DAYTIMES_POPUP, XPATH_FILTER_DAYTIMES_BUTTON)
        self.filter_daytime_outbound_set_hour_from_adapter(hour_from)
        #${actual_hours}=  get text  xpath=//*[@class="DayTimesPopup-value"][1]
        #${actual_hour_from}=  get regexp matches  ${actual_hours}  (\\d+)\:\\d+  1
        #${actual_hour_from}=  get from list  ${actual_hour_from}  0
        #log  ${actual_hours}
        #run keyword if  ${actual_hour_from} < ${hour_from}  move slider  xpath=${XPATH_FILTER_DAYTIMES_OUTBOUND_HOURS_LEFT_HANDLE}  20  0
        #run keyword if  ${actual_hour_from} < ${hour_from}  filter daytime outbound set hour from  ${hour_from}
        #run keyword if  ${actual_hour_from} > ${hour_from}  move slider  xpath=${XPATH_FILTER_DAYTIMES_OUTBOUND_HOURS_LEFT_HANDLE}  -20  0
        #un keyword if  ${actual_hour_from} > ${hour_from}  filter daytime outbound set hour from  ${hour_from}

    def filter_duration(self, max_hours, transfer_hours):
        self.click_element(XPATH_FILTER_DURATION)
        self.wait_until_page_contains_element(XPATH_FILTER_DURATION_POPUP)
        self.move_slider(XPATH_FILTER_DURATION_MAX_HOURS_HANDLE, -50, 0)
        self.move_slider(XPATH_FILTER_DURATION_TRANSFER_HOURS_LEFT_HANDLE, 50, 0)
        self.move_slider(XPATH_FILTER_DURATION_TRANSFER_HOURS_RIGHT_HANDLE, -50, 0)

    def filter_only_direct_flights(self):
        # TODO only if it is vissible
        self.click_element(XPATH_FILTER_OTHERS)
        self.select_checkbox(XPATH_FILTER_OTHERS)

    def filter_daytime_outbound_set_hour_from(self, hour_from):
        self.show_element(XPATH_FILTER_DAYTIMES_POPUP, XPATH_FILTER_DAYTIMES_BUTTON)
        hour_from = int(hour_from)
        actual_hours = self.get_text('//*[@class="DayTimesPopup-value"][1]')
        actual_outbound_hour_from = int(re.findall(r'(\d+):\d+', actual_hours)[0])
        if actual_outbound_hour_from < hour_from:
            self.move_slider(XPATH_FILTER_DAYTIMES_OUTBOUND_HOURS_LEFT_HANDLE, 10, 0)
            self.filter_daytime_outbound_set_hour_from(hour_from)
        elif actual_outbound_hour_from > hour_from:
            self.move_slider(XPATH_FILTER_DAYTIMES_HOURS_LEFT_HANDLE, -10, 0)
            self.filter_daytime_outbound_set_hour_from(hour_from)

    def filter_daytime_outbound_set_hour_to(self, hour_to):
        self.show_element(XPATH_FILTER_DAYTIMES_POPUP, XPATH_FILTER_DAYTIMES_BUTTON)
        hour_to = int(hour_to)
        actual_hours = self.get_text('//*[@class="DayTimesPopup-value"][1]')
        actual_outbound_hour_to = int(re.findall(r'(\d+):\d+', actual_hours)[1])
        if actual_outbound_hour_to < hour_to:
            self.move_slider(XPATH_FILTER_DAYTIMES_OUTBOUND_HOURS_RIGHT_HANDLE, 10, 0)
            self.filter_daytime_outbound_set_hour_from(hour_to)
        elif actual_outbound_hour_to > hour_to:
            self.move_slider(XPATH_FILTER_DAYTIMES_OUTBOUND_HOURS_RIGHT_HANDLE, -10, 0)
            self.filter_daytime_outbound_set_hour_to(hour_to)

    def filter_daytime_outbound_set_hour_range(self, hour_from, hour_to):
        self.filter_daytime_outbound_set_hour_from(hour_from)
        self.filter_daytime_outbound_set_hour_to(hour_to)

    def filter_daytime_outbound_set_days(self, days=''):
        days = days.split(',')
        self.show_element(XPATH_FILTER_DAYTIMES_POPUP, XPATH_FILTER_DAYTIMES_BUTTON)
        for element in self.get_webelements(CSS_FILTER_DAYTIMES_OUTBOUND_CHECKED_CHECKBOX):
            element_id = element.get_attribute('data-reactid')
            checked_id = element_id.split('$')[1].split('.')[0]
            if checked_id not in days:
                self.click_element("//*[@data-reactid='%s']" % element_id)
        for element in self.get_webelements(CSS_FILTER_DAYTIMES_OUTBOUND_UNCHECKED_CHECKBOX):
            element_id = element.get_attribute('data-reactid')
            unchecked_id = element_id.split('$')[1].split('.')[0]
            if unchecked_id in days:
                self.click_element("//*[@data-reactid='%s']" % element_id)

