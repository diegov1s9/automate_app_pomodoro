"""
This module contains utility functions for manipulating browser windows
using Selenium WebDriver. Includes functions to open, close and change
between browser tabs.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def open_new_tab(driver):
    """
    Opens a new blank tab.
    """
    driver.execute_script("window.open('about:blank');")
    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > 1
    )

def switch_to_new_tab(driver):
    """
    Switch to the new tab open.
    """
    driver.switch_to.window(driver.window_handles[-1])

def close_current_tab(driver):
    """
    Close the current tab.
    """
    driver.close()
    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) == 1
    )

def switch_to_tab(driver, index):
    """
    Switch to the tab specified by the index.
    Args:
        driver (WebDriver): The instance of the WebDriver.
        index (int): The index of the tab you want to change to.
    """
    driver.switch_to.window(driver.window_handles[index])


def scroll_to_element(driver, by_locator):
    """
    Scroll to the element specified by the locator.
    Args:
        driver (WebDriver): The instance of the WebDriver.
        by_locator (tuple): The locator of the element to scroll to.
    """
    actions = ActionChains(driver)
    actions.move_to_element(by_locator)
    actions.perform()
