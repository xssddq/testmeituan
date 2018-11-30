from libs.Main_class_app import *


logging.basicConfig(#filename='log_filename.txt',
                    format='[%(asctime)s] %(levelname)s - %(message)s',
                    level=logging.INFO)
log = logging.getLogger('Meituan')

params_for_driver = {
    'appium_port' : '4722',
    'language'    : 'cn',
    'locale'      : 'en',
    'app_file_apk': 'com.sankuai.meituan_2018-04-11.apk',
    'appPackage'  : 'com.sankuai.meituan',
    'appActivity' : 'com.meituan.android.hotel.reuse.homepage.HotelPoiListFrontActivity'
}

driver = setUp(**params_for_driver)


class Meituan(MainAppClass):

    LOCATION = 'korea'
    HOTEL = 'JW Marriott Hotel Seoul'

    def start_app_and_enter_to_start_page(self):

        self.driver.implicitly_wait(20)
        log.info("Start enter to app...")
        # sleep(10)
        # try:
        #     sleep(5)
        #     self.driver.find_element_by_id('android.widget.ImageButton').click()
        #     sleep(5)

        # except NoSuchElementException:
        #     pass
        log.info("Choose_location...")
        # try:
        #     choose_location = self.driver.find_element_by_id("com.sankuai.meituan:id/city_button")
        #     choose_location.click()
        # except NoSuchElementException:
        #     pass

        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(self.LOCATION)
        sleep(3)
        ok_btn = self.driver.find_element_by_id("com.sankuai.meituan:id/citylist_textview")
        print(ok_btn.text)
        ok_btn.click()
        log.info("Press on search place...")

        self.driver.find_element_by_id("com.sankuai.meituan:id/search_edit").click()
        log.info("Enter needed Hotel...")

        # def test_1(hotel):
        self.driver.implicitly_wait(5)

        self.driver.find_element_by_id("com.sankuai.meituan:id/search_edit").set_text(self.HOTEL)

        log.info("Confirm needed Hotel...")

        self.driver.find_element_by_id('com.sankuai.meituan:id/title').click()

        search_place = self.driver.find_elements_by_id('com.sankuai.meituan:id/search_edit')

        if search_place:
            log.info("Choose hotel...")
            self.driver.find_element_by_id('com.sankuai.meituan:id/title').click()

        name_hotel = False
        name_hotel1 = False
        try:
            log.info('Try find hotel name')
            name_hotel = self.driver.find_element_by_id('com.sankuai.meituan:id/title')
            name_hotel1 = self.driver.find_element_by_id('com.sankuai.meituan:id/addr')
        except NoSuchElementException:
            print('Error')
            pass
        # name_hotel = False
        # toggle = False
        # while not name_hotel:
        #     try:
        #         self.driver.implicitly_wait(5)
        #         log.info("Start find visibility...")
        #
        #         # wait = WebDriverWait(self.driver, 10)
        #         # name_hotel = self.driver.find_elements_by_xpath("//android.widget.TextViewt[@resource-id='com.sankuai.meituan:id/poi_title']")
        #         name_hotel = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.sankuai.meituan:id/poi_title")')
        #         log.info("Finish find visibility...")
        #         if not name_hotel:
        #             raise WebDriverException
        #         # print("search icon")
        #         # self.driver.implicitly_wait(5)
        #         # name_hotel = self.driver.find_element_by_id('com.sankuai.meituan:id/poi_title').implicitly_wait(5)
        #         # toggle = self.driver.find_elements_by_id('com.sankuai.meituan:id/toggle_icon')
        #
        #     except WebDriverException:
        #         print("back WebDriverException")
        #         self.driver.back()
        #         self.driver.find_element_by_id('com.sankuai.meituan:id/title').click()

            # finally:
            #     print("start again!!")

        # toggle[0].click()

        # name_hotel = self.driver.find_element_by_xpath("//*[@resource-id='com.sankuai.meituan:id/poi_title']")
        print(name_hotel)
        print(name_hotel1.text)
        name_hotel_text = name_hotel.text
        print(type(name_hotel_text))
        print(name_hotel_text)

        if name_hotel_text.find(self.HOTEL) != -1 or \
                set(name_hotel_text) >= set(self.HOTEL):
            print('Hotel correct!!!')
        else:
            print('Hotel not correct!!!')
        self.driver.back()

        print(len(self.HOTEL))

        for i in self.HOTEL:
            log.info("start test")
            test_1(i)
            log.info("finish test")





        # data_in = self.driver.find_element_by_id('com.sankuai.meituan:id/check_in_date').text
        # print(data_in)
        # self.driver.find_element_by_id("com.sankuai.meituan:id/check_in_date").click()

        # log.info("Find section Hotels...")
        # self.driver.find_element_by_xpath("//*[@index='2' and @class='android.view.View']").click()
        # sleep(5)
        # log.info("Come back to general page...")
        # sleep(5)
        # self.driver.find_element_by_class_name('android.widget.ImageButton').click()
        # sleep(5)
        # self.driver.find_element_by_xpath("//*[@index='2']").click()

        # try:
        #     log.info("Come back to general page...")
        #     sleep(5)
        #     self.driver.find_element_by_class_name('android.widget.ImageButton').click()
        #     sleep(5)
        #
        # except NoSuchElementException:
        #     pass
        #
        # log.info("Find section International Hotels...")
        # self.driver.find_element_by_id('com.sankuai.meituan:id/tab_middle').click()
        # # sleep(10)
        # log.info("Find section Domestic Hotels...")
        # self.driver.find_element_by_id('com.sankuai.meituan:id/tab_left').click()
        # sleep(5)

        # log.info("Find error")

        # try:
        #     self.driver.find_element_by_id('android:id/button1').click()
        #
        # except NoSuchElementException:
        #     pass

        # log.info("Find search place...")
        # try:
        #     # select_search = self.driver.find_element_by_id('com.sankuai.meituan:id/img_arrow')
        #     select_search = self.driver.find_element_by_xpath("//*[@index='2' and @id='com.sankuai.meituan:id/img_arrow']").click()
        #     select_search.click()
        # except NoSuchElementException:
        #     # self.driver.find_element_by_id('com.sankuai.meituan:id/search_clear').click()
        #     # self.driver.find_element_by_id('com.sankuai.meituan:id/select_search_text').click()
        #     pass

        # try:
        #     search_place = self.driver.find_element_by_id('com.sankuai.meituan:id/search_text_hint')
        #     # sleep(5)
        #     search_place.click()
        # except NoSuchElementException:
        #     self.driver.find_element_by_id('android:id/button1').click()
        #
        #     search_place = self.driver.find_element_by_id('com.sankuai.meituan:id/search_text_hint')
        #     search_place.click()

        return self

    def getResults(self):

        meta_details = self.driver.find_element_by_id("com.tripadvisor.tripadvisor:id/meta_details")
        sleep(2)
        top_price = meta_details.find_element_by_id("com.tripadvisor.tripadvisor:id/price")
        self.TOP_PRICE = int((top_price.text[1:]))
        print("Top price on site is {} $".format(self.TOP_PRICE))
        self.driver.find_element_by_id("com.tripadvisor.tripadvisor:id/text_links_revealer_button").click()
        self.driver.get_screenshot_as_file('img_tripadvisor/screenshot_{0}_{time}.png'.format(unidecode(self.HOTEL), time=strftime("%Y-%m-%d_%H-%M", gmtime())))
        print('Screenshot saved in img_tripadvisor/.')

        site_price = self.driver.find_elements_by_id("com.tripadvisor.tripadvisor:id/title_and_price_container")
        number_of_hotel = 0
        results = {}
        for i in site_price:
            if number_of_hotel <= 4:
                try:
                    name_site = i.find_element_by_id('com.tripadvisor.tripadvisor:id/title').text
                    price = i.find_element_by_id('com.tripadvisor.tripadvisor:id/price').text
                    results[unidecode(name_site)] = price
                except NoSuchElementException:
                    pass
                number_of_hotel += 1

        return results
