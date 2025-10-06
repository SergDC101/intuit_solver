import time

from base.selenium_base import SeleniumBase
from locators.exam_locators import ExamLocators


class ExamPage(SeleniumBase):

    def get_course_name(self):
        return self.is_present(ExamLocators.COURSE_NAME).text

    def click_checkbox_confirm(self):
        self.is_present(ExamLocators.CONFIRM_CHECKBOX).click()

    def click_button_confirm(self):
        self.is_present(ExamLocators.CONFIRM_BUTTON).click()

    def get_count_questions(self) -> int:
        return int(self.is_present(ExamLocators.COUNT_QUESTIONS).text.split("из")[-1].replace(")", ""))

    def get_question(self) -> str:
        time.sleep(1)
        return self.is_present(ExamLocators.QUESTION).text

    def get_answers(self) -> list:
        answers = self.are_present(ExamLocators.ANSWERS)
        answers_list = []
        for answer in answers:
            answers_list.append(answer.text)
        return answers_list

    def set_answer(self, answer_index):
        self.are_present(ExamLocators.ANSWER_CHECKBOX)[answer_index].click()

    def click_answer_button(self):
        self.is_present(ExamLocators.ANSWER_BUTTON).click()