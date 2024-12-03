"""
This file contains the class to interact
with the homepage of the website
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, JavascriptException
import selector
from utils.logger import setup_logger
import utils.utils as utils


class HomePage():
    """ Class to interact with the homepage """
    def __init__(self, driver):
        self.driver = driver
        self.logger = setup_logger(self.__class__.__name__)

    def start_timer(self):
        """ Function to start the timer """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(selector.button_start)
        )
        self.driver.find_element(*selector.button_start).click()

    def pause_timer(self):
        """ Function to pause the timer """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(selector.button_pause)
        )
        self.driver.find_element(*selector.button_pause).click()

    def reset_timer(self):
        """ Function to reset the timer """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(selector.button_reset)
        )
        self.driver.find_element(*selector.button_reset).click()

    def get_timer_display(self):
        """ Function to get the timer display """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(selector.text_timer_display)
        )
        return self.driver.find_element(*selector.text_timer_display)

    def simulate_time_passage(self,seconds):
        """ Function to simulate the passage of time """
        try:
            # Esperar a que el elemento esté presente
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(selector.pomodoro_component)
            )
            script = (
                f"document.getElementById('pomodoro-component').__vueInstance__."
                f"setTotalSeconds({seconds});"
            )
            self.driver.execute_script(script)
            return True
        except JavascriptException as e:
            self.logger.error("simulate_time_passage Possibly the APP is in production mode: %s", e)
            return False
        except WebDriverException as e:
            self.logger.error("simulate_time_passage Error in the WebDriver or Javascript: %s",e)
            return False

    def add_task(self, text):
        """ Function to add a task """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(selector.input_task)
        )
        input_task = self.driver.find_element(*selector.input_task)
        utils.scroll_to_element(self.driver, input_task)
        try:
            input_task.send_keys(text)
            self.driver.find_element(*selector.button_add_task).click()
            return True
        except WebDriverException as e:
            self.logger.error("add_task Error in the WebDriver: %s", e)
            return False

    def get_div_error_message_task(self):
        """ Function that gets the error message when adding a task """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(selector.div_error_message_task)
        )
        return self.driver.find_element(*selector.div_error_message_task)

    def get_last_li_added_task(self):
        """ Function that gets the last element <li> corresponding to the last added task """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(selector.ul_added_task)
        )
        try:
            ul = self.driver.find_element(*selector.ul_added_task)
            li_elements = ul.find_elements(*selector.tag_name_li)
            if li_elements:
                return li_elements[-1]
            return None
        except WebDriverException as e:
            self.logger.error("get_last_li_added_task Error in the WebDriver: %s", e)
            return None

    def get_last_text_added_task(self):
        """ 
        Function that gets the text corresponding to the last added task.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(selector.ul_added_task)
        )
        text_task = ""
        last_li = self.get_last_li_added_task()
        if last_li:
            try:
                text_task = last_li.find_element(*selector.tag_name_span).text
            except WebDriverException as e:
                self.logger.error("get_last_text_added_task Error in the WebDriver: %s", e)
        return text_task

    def click_edit_button_last_task(self):
        """ Function to click the edit button of the last task """
        last_li = self.get_last_li_added_task()
        if last_li:
            try:
                btn_edit = last_li.find_element(*selector.btn_edit)
                btn_edit.click()
                return True
            except WebDriverException as e:
                self.logger.error("click_edit_button_last_task Error in the WebDriver: %s", e)
                return False
        return False

    def edit_last_task(self, new_text):
        """ Function to edit a task """
        last_li = self.get_last_li_added_task()
        if last_li:
            try:
                input_task = last_li.find_element(*selector.tag_name_input)
                input_task.clear()
                input_task.send_keys(new_text)
                btn_save = last_li.find_element(*selector.btn_save)
                btn_save.click()
                return True
            except WebDriverException as e:
                self.logger.error("edit_task Error in the WebDriver: %s", e)
                return False
        return False

    def delete_last_task(self):
        """ Function to delete last task """
        last_li = self.get_last_li_added_task()
        if last_li:
            try:
                btn_delete = last_li.find_element(*selector.btn_delete)
                btn_delete.click()
                return True
            except WebDriverException as e:
                self.logger.error("delete_last_task Error in the WebDriver: %s", e)
                return False
        return False
