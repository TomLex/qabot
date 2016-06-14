# -*- coding: utf-8 -*-
import re
from datetime import datetime

# TODO remove logger
from robot.api import logger
from Selenium2Library import Selenium2Library
from XvfbRobot import XvfbRobot

import config
import variables.locators as V


class CustomSeleniumLibrary(Selenium2Library):
    """ COMMON METHODS """
    def begin_test(self):
        if config.xvfb['enabled']:
            XvfbRobot().start_virtual_display(config.xvfb['width'], config.xvfb['height'])
        self.open_browser('about:blank', browser=config.default_browser)
        #self.maximize_browser_window()

    def end_test(self):
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
        self.execute_javascript("document.evaluate('{0}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE , null).singleNodeValue.scrollIntoView(true);".format(location))

    def is_visible(self, element):
        return self._is_visible(element)

    """ TOP NAVBAR """
    def change_currency(self, currency):
        currency = currency.lower()
        #actual_currency = self.get_text(V.XPATH.CURRENCY_CODE)
        #if actual_currency != currency:
        self.click_element(V.XPATH.CURRENCY_BUTTON)
        self.wait_until_page_contains_element(V.XPATH.CURRENCY_POPUP)
        self.click_element("//*[contains(@class, 'currency-code') and contains(text(), '{0}')]".format(currency))

    def change_language(self, language_code):
        language_code = language_code.lower()
        self.click_element(V.XPATH.LANGUAGE_BUTTON)
        self.wait_until_page_contains_element(V.XPATH.LANGUAGE_POPUP)
        self.click_element("//*[@class='flag __locale-{0}']".format(language_code))

    def show_menu(self):
        self.click_element(V.XPATH.MENU_OPEN_BUTTON)
        self.wait_until_page_contains_element(V.XPATH.MENU)

    def hide_menu(self):
        self.click_element(V.XPATH.MENU_CLOSE_BUTTON)

    """ SEARCH PAGE """
    def search(self, flight_type, fly_from, fly_to, passengers_num, price_from, price_to):
        self.change_flight_type(flight_type)
        self.fill_fly_from(fly_from)
        self.fill_fly_to(fly_to)
        self.change_passengers_number(passengers_num)
        self.filter_price(price_from, price_to)
        self.click_element("xpath=//*[@class='SearchForm-multicity-wrapper']")
        self.choose_flight(1)

    def choose_aggregate(self):
        self.wait_until_page_contains_element(V.CSS.FLIGHTS_AGGREGATE)
        self.click_element(V.CSS.FLIGHTS_AGGREGATE)

    def choose_journey(self):
        self.wait_until_page_contains_element(V.CSS.FLIGHTS_JOURNEY)
        self.click_element(V.CSS.FLIGHTS_JOURNEY)

    def go_to_booking_easy(self):
        self.choose_aggregate()
        self.choose_journey()
        self.go_to_booking()

    def go_to_booking(self):
        self.wait_until_page_contains_element("css=a[href*='booking']")
        self.click_element("css=a[href*='booking']")

    # TODO
    def search_sort(self, sort_type):
        pass

    def change_flight_type(self, flight_type):
        if flight_type == 'oneway':
            self.click_element(V.XPATH.CHECKBOX_ONEWAY)
        elif flight_type == 'return':
            self.click_element(V.XPATH.CHECKBOX_RETURN)
        else:
            raise Exception("Unknown flight type!")

    def change_passengers_number(self, passengers_num):
        if not self.is_visible(V.XPATH.PASSENGERS_POPUP):
            self.click_element(V.XPATH.PASSENGERS_FIELD)
        actual_passengers = self.get_text(V.XPATH.PASSENGERS_NUMBER)
        if actual_passengers < passengers_num:
            self.click_element(V.XPATH.PASSENGERS_BUTTON_ADD)
            self.change_passengers_number(passengers_num)
        if actual_passengers > passengers_num:
            self.click_element(V.XPATH.PASSENGERS_BUTTON_REMOVE)
            self.change_passengers_number(passengers_num)

    def fill_fly_from(self, fly_from):
        self.wait_until_page_contains_element(V.XPATH.FLY_FROM_INPUT)
        self.input_text(V.XPATH.FLY_FROM_INPUT, fly_from)
        # TODO compare input text with fly_from
        self.wait_until_page_contains_element(V.XPATH.FLY_FROM_SELECT.format(fly_from))
        self.click_element(V.XPATH.FLY_FROM_SELECT.format(fly_from, fly_from))

    def fill_fly_to(self, fly_to):
        self.wait_until_page_contains_element(V.XPATH.FLY_TO_INPUT)
        self.input_text(V.XPATH.FLY_TO_INPUT, fly_to)
        self.wait_until_page_contains_element(V.XPATH.FLY_TO_SELECT.format(fly_to, fly_to))
        self.click_element(V.XPATH.FLY_TO_SELECT.format(fly_to, fly_to))

    '''FILTERS'''

    def filter_get_first_last_visible_dates(self):
        ids = self.get_webelements("//*[contains(@class, 'CalendarDay') "
                                        "and not(contains('prev-month')) "
                                        "and not(contains('next-month'))]/@data-reactid")
        first_date = ids[0].split('$')[-1]
        last_date = ids[-1].split('$')[-1]
        return first_date, last_date

    def filter_get_last_visible_date(self):
        pass

    def filter_change_outbound_date(self, date_from=None, date_to=None):
        self.show_element(V.XPATH.FILTER_DATE_OUTBOUND_POPUP, V.XPATH.FILTER_DATE_OUTBOUND_BUTTON)
        self.wait_until_page_contains_element("//*[@class='Calendar-month']")
        if date_from and date_to is None:
            date_from_object = datetime.strptime(date_from, '%Y-%m-%d')
            # TODO - day choose logic
            pass
        elif date_from and date_to:
            date_from_object = datetime.strptime(date_from, '%Y-%m-%d')
            date_to_object = datetime.strptime(date_to, '%Y-%m-%d')
            # TODO - interval choose logic
            pass
        else:
            self.click_element(V.XPATH.FILTER_DATE_MENU_ANY)

    def filter_change_inbound_date(self, date_from=None, date_to=None, nights_to_stay=None, only_inbound=False):
        self.show_element(V.XPATH.FILTER_DATE_INBOUND_POPUP, V.XPATH.FILTER_DATE_INBOUND_BUTTON)
        self.wait_until_page_contains_element("//*[@class='Calendar-month']")
        if only_inbound:
            self.click_element(V.XPATH.FILTER_DATE_MENU_NO_RETURN)
        elif nights_to_stay:
            self.click_element(V.XPATH.FILTER_DATE_MENU_NIGHTS_TO_STAY)
            self._filter_change_nights_to_stay(int(nights_to_stay.split(',')[0]), int(nights_to_stay.split(',')[1]))
        elif date_from and date_to is None:
            pass # # konkretny datum
        elif date_from and date_to:
            pass # interval
        else:
            self.click_element(V.XPATH.FILTER_DATE_MENU_ANY)

    def _filter_change_nights_to_stay(self, nights_from, nights_to):
        actual_nights_from, actual_nights_to = self._get_actual_nights_to_stay()
        if actual_nights_from == nights_from and actual_nights_to == nights_to:
            self.click_element(V.XPATH.FILTER_DATE_NIGHTS_TO_STAY_CONFIRM)
            return
        if actual_nights_from > nights_from:
            self.move_slider(V.XPATH.FILTER_DATE_NIGHTS_TO_STAY_LOW_HANDLE, -20, 0)
        elif actual_nights_from < nights_from:
            self.move_slider(V.XPATH.FILTER_DATE_NIGHTS_TO_STAY_LOW_HANDLE, 20, 0)
        if actual_nights_to > nights_to:
            self.move_slider(V.XPATH.FILTER_DATE_NIGHTS_TO_STAY_HIGH_HANDLE, -20, 0)
        elif actual_nights_to < nights_to:
            self.move_slider(V.XPATH.FILTER_DATE_NIGHTS_TO_STAY_HIGH_HANDLE, 20, 0)
        self._filter_change_nights_to_stay(nights_from, nights_to)

    def _get_actual_nights_to_stay(self):
        return [int(s) for s in self.get_text(V.XPATH.FILTER_DATE_NIGHTS_TO_STAY_HANDLE_TEXT).split() if s.isdigit()]

    def choose_flight(self, index):
        self.wait_until_page_contains_element("//div[@class='Journey spCard _no-radius spShadow-half-2 _one-way']")
        self.click_element("//div[@class='Journey spCard _no-radius spShadow-half-2 _one-way']")

    def filter_price(self, price_from, price_to):
        self.show_element(V.XPATH.FILTER_PRICE_POPUP, V.XPATH.FILTER_PRICE_BUTTON)
        actual_price_from, actual_price_to = self._get_actual_price()
        if actual_price_from > price_from:
            self.move_slider(V.XPATH.FILTER_PRICE_LOW_HANDLE, -20, 0)
            updated_actual_price_from, _ = self._get_actual_price()
        elif actual_price_from < price_from:
            self.move_slider(V.XPATH.FILTER_PRICE_LOW_HANDLE, 20, 0)
        if actual_price_to > price_to:
            self.move_slider(V.XPATH.FILTER_PRICE_HIGH_HANDLE, -20, 0)
        elif actual_price_to < price_to:
            self.move_slider(V.XPATH.FILTER_PRICE_HIGH_HANDLE, 20, 0)
        self.filter_price(price_from, price_to)

    def _get_actual_price(self):
        logger.info(self.get_text(V.XPATH.FILTER_PRICE_HANDLE_TEXT))
        prices = [0, sys.maxint]
        prices_text = [s for s in self.get_text(V.XPATH.FILTER_PRICE_HANDLE_TEXT).split() if s.isdigit() or s == '-']
        if len(prices_text) == 2:
            if prices_text[0] == '-':
                prices[1] = prices_text[1]
            else:
                prices[0] = prices_text[0]
        elif len(prices_text) == 3:
            prices = (prices_text[0], prices_text[2])
        logger.info(prices)
        return prices

    def filter_daytime_outbound_set_type(self, filter_type):
        self.show_element(V.XPATH.FILTER_DAYTIMES_POPUP, V.XPATH.FILTER_DAYTIMES_BUTTON)
        if filter_type == 'departure':
            self.click_element(V.XPATH.FILTER_DAYTIMES_OUTBOUND_DEPARTURE)
        elif filter_type == 'arrival':
            self.click_element(V.XPATH.FILTER_DAYTIMES_OUTBOUND_ARRIVAL)
        else:
            raise Exception("Unknown filter type!")

    def filter_daytime_inbound_set_type(self, filter_type):
        self.show_element(V.XPATH.FILTER_DAYTIMES_POPUP, V.XPATH.FILTER_DAYTIMES_BUTTON)
        if filter_type == 'departure':
            self.click_element(V.XPATH.FILTER_DAYTIMES_INBOUND_DEPARTURE)
        elif filter_type == 'arrival':
            self.click_element(V.XPATH.FILTER_DAYTIMES_INBOUND_ARRIVAL)
        else:
            raise Exception("Unknown filter type!")

    def filter_daytime_outbound_set_hour_from_adapter(self, hour_from):
        self.show_element(V.XPATH.FILTER_DAYTIMES_POPUP, V.XPATH.FILTER_DAYTIMES_BUTTON)
        self.filter_daytime_outbound_set_hour_from_adapter(hour_from)
        #${actual_hours}=  get text  xpath=//*[@class="DayTimesPopup-value"][1]
        #${actual_hour_from}=  get regexp matches  ${actual_hours}  (\\d+)\:\\d+  1
        #${actual_hour_from}=  get from list  ${actual_hour_from}  0
        #log  ${actual_hours}
        #run keyword if  ${actual_hour_from} < ${hour_from}  move slider  xpath=${V.XPATH.FILTER_DAYTIMES_OUTBOUND_HOURS_LOW_HANDLE}  20  0
        #run keyword if  ${actual_hour_from} < ${hour_from}  filter daytime outbound set hour from  ${hour_from}
        #run keyword if  ${actual_hour_from} > ${hour_from}  move slider  xpath=${V.XPATH.FILTER_DAYTIMES_OUTBOUND_HOURS_LOW_HANDLE}  -20  0
        #un keyword if  ${actual_hour_from} > ${hour_from}  filter daytime outbound set hour from  ${hour_from}

    def filter_duration(self, max_hours, transfer_hours):
        self.click_element(V.XPATH.FILTER_DURATION)
        self.wait_until_page_contains_element(V.XPATH.FILTER_DURATION_POPUP)
        self.move_slider(V.XPATH.FILTER_DURATION_MAX_HOURS_HANDLE, -50, 0)
        self.move_slider(V.XPATH.FILTER_DURATION_TRANSFER_HOURS_LOW_HANDLE, 50, 0)
        self.move_slider(V.XPATH.FILTER_DURATION_TRANSFER_HOURS_HIGH_HANDLE, -50, 0)

    def filter_only_direct_flights(self):
        # TODO only if it is visible
        self.click_element(V.XPATH.FILTER_OTHERS)
        self.select_checkbox(V.XPATH.FILTER_OTHERS)

    def filter_daytime_outbound_set_hour_from(self, hour_from):
        self.show_element(V.XPATH.FILTER_DAYTIMES_POPUP, V.XPATH.FILTER_DAYTIMES_BUTTON)
        hour_from = int(hour_from)
        actual_hours = self.get_text('//*[@class="DayTimesPopup-value"][1]')
        actual_outbound_hour_from = int(re.findall(r'(\d+):\d+', actual_hours)[0])
        if actual_outbound_hour_from < hour_from:
            self.move_slider(V.XPATH.FILTER_DAYTIMES_OUTBOUND_HOURS_LOW_HANDLE, 10, 0)
            self.filter_daytime_outbound_set_hour_from(hour_from)
        elif actual_outbound_hour_from > hour_from:
            self.move_slider(V.XPATH.FILTER_DAYTIMES_HOURS_LOW_HANDLE, -10, 0)
            self.filter_daytime_outbound_set_hour_from(hour_from)

    def filter_daytime_outbound_set_hour_to(self, hour_to):
        self.show_element(V.XPATH.FILTER_DAYTIMES_POPUP, V.XPATH.FILTER_DAYTIMES_BUTTON)
        hour_to = int(hour_to)
        actual_hours = self.get_text('//*[@class="DayTimesPopup-value"][1]')
        actual_outbound_hour_to = int(re.findall(r'(\d+):\d+', actual_hours)[1])
        if actual_outbound_hour_to < hour_to:
            self.move_slider(V.XPATH.FILTER_DAYTIMES_OUTBOUND_HOURS_HIGH_HANDLE, 10, 0)
            self.filter_daytime_outbound_set_hour_from(hour_to)
        elif actual_outbound_hour_to > hour_to:
            self.move_slider(V.XPATH.FILTER_DAYTIMES_OUTBOUND_HOURS_HIGH_HANDLE, -10, 0)
            self.filter_daytime_outbound_set_hour_to(hour_to)

    def filter_daytime_outbound_set_hour_range(self, hour_from, hour_to):
        self.filter_daytime_outbound_set_hour_from(hour_from)
        self.filter_daytime_outbound_set_hour_to(hour_to)

    def filter_daytime_outbound_set_days(self, days=''):
        days = days.split(',')
        self.show_element(V.XPATH.FILTER_DAYTIMES_POPUP, V.XPATH.FILTER_DAYTIMES_BUTTON)
        for element in self.get_webelements(V.CSS.FILTER_DAYTIMES_OUTBOUND_CHECKED_CHECKBOX):
            element_id = element.get_attribute('data-reactid')
            checked_id = element_id.split('$')[1].split('.')[0]
            if checked_id not in days:
                self.click_element("//*[@data-reactid='%s']" % element_id)
        for element in self.get_webelements(V.CSS.FILTER_DAYTIMES_OUTBOUND_UNCHECKED_CHECKBOX):
            element_id = element.get_attribute('data-reactid')
            unchecked_id = element_id.split('$')[1].split('.')[0]
            if unchecked_id in days:
                self.click_element("//*[@data-reactid='%s']" % element_id)

