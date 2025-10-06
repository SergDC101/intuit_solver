import time
from pathlib import Path

from loguru import logger
from base.driver import Driver
from data.env_var import EXAM_EXTERN_COURSE_LINK, ABSOLUT_PATH
from page.exam_page import ExamPage
from reports.docx_reporter import DocxReporter
from scripts.auth_script import AuthScript
from solvers.vtone.vtone import VtoneAnswers

driver = Driver().get_webdriver()

absolut_path = ABSOLUT_PATH
auth_script = AuthScript(driver)
auth_script.login()

driver.get(EXAM_EXTERN_COURSE_LINK)

exam_page = ExamPage(driver)

course_name = exam_page.get_course_name()

screenshot_dir = Path(absolut_path + f"/{course_name}/скриншоты")
screenshot_dir.mkdir(parents=True, exist_ok=True)
vtone = VtoneAnswers(course_name)

driver.save_screenshot(str(screenshot_dir / f"0.png"))

exam_page.click_checkbox_confirm()
exam_page.click_button_confirm()

logger.info("Тест запущен")

count_question = exam_page.get_count_questions()

for i in range(count_question):
    time.sleep(5)
    logger.info(f"Вопрос {i+1}. {exam_page.get_question()}")
    logger.info(f"Набор ответов: {exam_page.get_answers()}")
    true_answers = vtone.get_answer(exam_page.get_question(), exam_page.get_answers())

    logger.info(f"Индекс ответа: {true_answers}")

    for el in true_answers:
        time.sleep(5)
        exam_page.set_answer(el)
        time.sleep(1)
    driver.save_screenshot(str(screenshot_dir / f"{i + 1}.png"))
    exam_page.click_answer_button()
    logger.info("")
    logger.info("")

time.sleep(5)
driver.save_screenshot(str(screenshot_dir / f"{count_question+1}.png"))

time.sleep(20)

driver.quit()

doc_reporter = DocxReporter(course_name)
doc_reporter.create_exam_document()
