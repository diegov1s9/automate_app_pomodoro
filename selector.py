"""
This file contains the selectors for the elements in the Pomodoro App.
"""
from selenium.webdriver.common.by import By

button_start = (By.ID, "btn-start")
button_pause = (By.ID, "btn-pause")
button_reset = (By.ID, "btn-reset")
input_task = (By.ID, "input-task")
button_add_task = (By.ID, "btn-add-task")
text_timer_display = (By.ID, "timer-display")
pomodoro_component = (By.ID, "pomodoro-component")
div_error_message_task = (By.ID, "error-message-task")
ul_added_task = (By.ID, "ul-added-task")
tag_name_li = (By.TAG_NAME, "li")
tag_name_span = (By.TAG_NAME, "span")
tag_name_input = (By.TAG_NAME, "input")
btn_edit = (By.CSS_SELECTOR, '[id*="btn-edit"]')
btn_save = (By.CSS_SELECTOR, '[id*="btn-save"]')
btn_delete = (By.CSS_SELECTOR, '[id*="btn-delete"]')

