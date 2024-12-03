"""
This module contains the test cases for the Pomodoro app
"""
import time  # Imports from the standard library
from selenium import webdriver  # Imports from third-party libraries
from selenium.webdriver.chrome.options import Options
import data  # Local imports
from utils import utils
from pages.home_page import HomePage


class TestAppPomodoro:
    """ Class to test the Pomodoro App """
    driver = None

    @classmethod
    def setup_class(cls):
        """ Setup the webdriver """
        capabilities = Options()
        capabilities.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        capabilities.add_argument("--headless")
        capabilities.add_argument("window-size=1920x1080")
        capabilities.add_argument("--incognito")
        capabilities.add_argument("--disable-cache")
        capabilities.add_argument("--disable-extensions")
        capabilities.add_argument("--no-sandbox")
        capabilities.add_argument("--disable-dev-shm-usage")
        capabilities.add_argument("--remote-debugging-port=9222")
        capabilities.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.popups": 2,
            "profile.default_content_setting_values.automatic_downloads": 1
        })
        cls.driver = webdriver.Chrome(options=capabilities)


    def test_timer_runs_time_of_twenty_five_minutes(self):
        """ ID 1 Test to verify that the timer runs for 25 minutes """
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        assert home_page.start_timer() is not False, "start_timer failed"
        # time.sleep(1500)
        assert home_page.simulate_time_passage(5), \
                "simulate_time_passage failed, Possibly the APP is in production mode"
        time.sleep(5)
        timer_display = home_page.get_timer_display()
        assert timer_display.text == "5:00", "The timer did not run for 25 minutes"

    def test_timer_shows_five_minutes_rest(self):
        """ 
        ID 2 Test to verify that the timer shows 5 minutes rest,
        except for the fourth cycle.
        """
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        time.sleep(5)
        assert home_page.start_timer() is not False, "start_timer failed"
        # time.sleep(1500)
        assert home_page.simulate_time_passage(5), \
                "simulate_time_passage failed, Possibly the APP is in production mode"
        time.sleep(5)
        timer_display = home_page.get_timer_display()
        assert timer_display.text == "5:00", "The timer does not show the 5 minutes rest"

    def test_timer_runs_time_of_five_minutes_correctly(self):
        """ ID 3 Test to verify that the timer runs for 5 minutes """
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        time.sleep(5)
        assert home_page.start_timer() is not False, "start_timer failed"
        # time.sleep(1500)
        assert home_page.simulate_time_passage(5), \
                "simulate_time_passage failed, Possibly the APP is in production mode"
        time.sleep(5)
        timer_display = home_page.get_timer_display()
        assert timer_display.text == "5:00", "The timer does not show the 5 minutes"
        assert home_page.start_timer() is not False, "start_timer failed"
        # time.sleep(300)
        assert home_page.simulate_time_passage(5), \
                "simulate_time_passage failed, Possibly the APP is in production mode"
        time.sleep(5)
        timer_display = home_page.get_timer_display()
        assert timer_display.text == "25:00", "The timer did not run for 5 minutes"

    def test_timer_shows_rest_time_of_twenty_minutes_correctly(self):
        """ ID 4 Test to verify that the timer shows 20 minutes rest """
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        # Define the 4 cycles with their expected times
        cycles = [
            ("5:00", "25:00"),
            ("5:00", "25:00"),
            ("5:00", "25:00"),
            ("20:00", None)
        ]
        time.sleep(5)
        for rest_time, work_time in cycles:
            # Work cycle
            assert home_page.start_timer() is not False, "start_timer failed"
            time.sleep(2)
            assert home_page.simulate_time_passage(5), \
                "simulate_time_passage failed, Possibly the APP is in production mode"
            time.sleep(5)
            timer_display = home_page.get_timer_display()
            assert timer_display.text == rest_time, f"The timer does not show the {rest_time} rest"
            if work_time:
                # Rest cycle
                assert home_page.start_timer() is not False, "start_timer failed"
                time.sleep(2)
                assert home_page.simulate_time_passage(5), \
                    "simulate_time_passage failed, Possibly the APP is in production mode"
                time.sleep(5)
                timer_display = home_page.get_timer_display()
                assert timer_display.text == work_time, \
                f"The timer does not show the {work_time} work period"

    def test_timer_runs_the_twenty_minutes_correctly(self):
        """ ID 5 Test verifies that the timer runs the 20 minutes correctly """
        new_time = data.NEW_TIME
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        # Define the 4 cycles with their expected times
        cycles = [
            ("5:00", "25:00"),
            ("5:00", "25:00"),
            ("5:00", "25:00"),
            ("20:00", "25:00")
        ]
        for rest_time, work_time in cycles:
            # Work cycle
            time.sleep(5)
            assert home_page.start_timer() is not False, "start_timer failed"
            assert home_page.simulate_time_passage(new_time), \
                "simulate_time_passage failed, Possibly the APP is in production mode"
            time.sleep(new_time)
            timer_display = home_page.get_timer_display()
            assert timer_display.text == rest_time, f"The timer does not show the {rest_time} rest"
            # Rest cycle
            time.sleep(5)
            assert home_page.start_timer() is not False, "start_timer failed"
            assert home_page.simulate_time_passage(new_time), \
                "simulate_time_passage failed, Possibly the APP is in production mode"
            time.sleep(new_time)
            timer_display = home_page.get_timer_display()
            assert timer_display.text == work_time, \
            f"The timer does not show the {work_time} work period"

    def test_save_the_timer_time_after_closing_the_application(self):
        """ ID 6 Test for save the timer time after closing the application. """
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        assert home_page.start_timer() is not False, "start_timer failed"
        time.sleep(5)
        utils.open_new_tab(self.driver)
        utils.switch_to_new_tab(self.driver)
        utils.switch_to_tab(self.driver, 0)
        utils.close_current_tab(self.driver)
        utils.switch_to_tab(self.driver, 0)
        self.driver.get(data.BASE_URL)
        time.sleep(5)
        timer_display = home_page.get_timer_display()
        assert timer_display.text != "25:00", \
        "El temporizador no mantuvo el tiempo después de cerrar y abrir la aplicación"

    def test_add_a_task(self):
        """ ID 7 Test to add a task """
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        text_task = data.TEXT_NEW_TASK
        assert home_page.add_task(text_task), \
            "The task was not added correctly add_task"
        error_message_task = home_page.get_div_error_message_task()
        assert error_message_task.text == "", \
            "The task was not added correctly get_div_error_message_task"

    def test_view_added_task(self):
        """ ID 8 Test to view the added task """
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        text_task = data.TEXT_NEW_TASK
        assert home_page.add_task(text_task), \
            "The task was not added correctly add_task"
        error_message_task = home_page.get_div_error_message_task()
        assert error_message_task.text == "", \
            "The task was not added correctly"
        last_task = home_page.get_last_text_added_task()
        assert last_task == text_task, "The task was not displayed correctly"

    def test_edit_task(self):
        """ ID 9 Test to edit a task """
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        text_task = data.TEXT_NEW_TASK
        assert home_page.add_task(text_task), \
            "The task was not added correctly add_task"
        error_message_task = home_page.get_div_error_message_task()
        assert error_message_task.text == "", \
            "The task was not added correctly"
        time.sleep(5)
        assert home_page.click_edit_button_last_task(), \
            "The edit button was not clicked correctly"
        new_text_task = data.NEW_TEXT_TASK
        time.sleep(5)
        assert home_page.edit_last_task(new_text_task), \
            "The task was not edited correctly"
        time.sleep(5)
        last_task = home_page.get_last_text_added_task()
        assert last_task == new_text_task, "The task was not displayed correctly"

    def test_delete_task(self):
        """ ID 10 Test to delete a task """
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        text_task = data.TEXT_NEW_TASK
        assert home_page.add_task(text_task), \
            "The task was not added correctly add_task"
        error_message_task = home_page.get_div_error_message_task()
        assert error_message_task.text == "", \
            "The task was not added correctly"
        assert home_page.delete_last_task(), \
            "The task was not deleted correctly"

    def test_save_task_after_closing_the_application(self):
        """ ID 11 Test to save tasks after closing the application """
        self.driver.get(data.BASE_URL)
        home_page = HomePage(self.driver)
        text_task_one = data.TEXT_TASK_ONE
        assert home_page.add_task(text_task_one), \
            "The task one was not added correctly add_task"
        error_message_task = home_page.get_div_error_message_task()
        assert error_message_task.text == "", \
            "The task one was not added correctly"
        text_task_two = data.TEXT_TASK_TWO
        assert home_page.add_task(text_task_two), \
            "The task two was not added correctly add_task"
        error_message_task = home_page.get_div_error_message_task()
        assert error_message_task.text == "", \
            "The task two was not added correctly"
        utils.open_new_tab(self.driver)
        utils.switch_to_new_tab(self.driver)
        utils.switch_to_tab(self.driver, 0)
        utils.close_current_tab(self.driver)
        utils.switch_to_tab(self.driver, 0)
        self.driver.get(data.BASE_URL)
        time.sleep(5)
        last_task = home_page.get_last_text_added_task()
        assert last_task == text_task_two, \
            "The task was not saved correctly after closing the application"
        time.sleep(5)

    @classmethod
    def teardown_class(cls):
        """ Quit the webdriver """
        cls.driver.quit()
