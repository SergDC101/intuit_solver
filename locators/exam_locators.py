import unittest

from selenium.webdriver.common.by import By


class ExamLocators:
    COURSE_NAME = (By.CSS_SELECTOR, ".spelling-content-entity h1")
    CONFIRM_CHECKBOX = (By.NAME, "rules_confirm")
    CONFIRM_BUTTON = (By.CLASS_NAME, "continue-button")
    COUNT_QUESTIONS = (By.CLASS_NAME, "title-ex")
    QUESTION = (By.CLASS_NAME, "question")
    ANSWERS = (By.CSS_SELECTOR, ".answer .right")
    ANSWER_CHECKBOX = (By.CSS_SELECTOR, ".answer .left input")
    ANSWER_BUTTON = (By.CSS_SELECTOR, '#test-task-form .command-buttons a[destination_block_id="course-test-dialog"]')