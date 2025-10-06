from dotenv import load_dotenv
import os

load_dotenv()

INTUIT_LOGIN = os.environ.get("INTUIT_LOGIN")
INTUIT_PASSWORD = os.environ.get("INTUIT_PASSWORD")
EXAM_EXTERN_COURSE_LINK = os.environ.get("EXAM_EXTERN_COURSE_LINK")
ABSOLUT_PATH = os.environ.get("ABSOLUT_PATH")
STUDENT_NAME = os.environ.get("STUDENT_NAME")
GROUP_NAME = os.environ.get("GROUP_NAME")
