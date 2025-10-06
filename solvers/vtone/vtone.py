from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from loguru import logger

from solvers.vtone.vtone_base import VtoneBase


class VtoneAnswers:

    def __init__(self, course_name):
        self.course_name = course_name
        self.vtone = VtoneBase()
        self.course_link = self.vtone.get_courses_list()[course_name] \
            if self.course_name in self.vtone.get_courses_list() else None


    def check_course_is_exist(self):
        return True if self.course_name in self.vtone.get_courses_list() else False

    def get_answer(self, question: str, answer: list):

        question_links_list = []
        question = question.lower().replace(' ', '')

        for item in self.get_list_question(self.course_link):
            if question == item['title']:
                question_links_list.append(item['url'])


        new_answer = [s.lower().replace(' ', '') for s in answer]

        question_true = ""
        if len(question_links_list) != 0:
            if len(question_links_list) > 1:
                for question_link in question_links_list:
                    if set(new_answer) == set(self.get_all_answers(question_link)):
                        question_true = question_link
            else:
                question_true = question_links_list[0]



        true_answer = self.get_true_answers(question_true)


        result = []
        for index, item in enumerate(new_answer):
            if item in true_answer:
                result.append(index)

        return result


    def get_all_answers(self, question_link) -> set:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            response = requests.get(question_link, headers=headers)
            response.raise_for_status()  # Проверяем статус ответа

            soup = BeautifulSoup(response.text, 'html.parser')

            answer_list = []

            answers = soup.select('.answers .answer', href=True)

            for answer in answers:
                text = answer.get_text(strip=True).lower()
                answer_list.append(text)

            answer_list = [s.lower().replace(' ', '') for s in answer_list]


            return set(answer_list)

        except requests.RequestException as e:
            print(f"Ошибка при запросе к сайту: {e}")
            return []
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return []

    def get_true_answers(self, question_link) -> list:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            response = requests.get(question_link, headers=headers)
            response.raise_for_status()  # Проверяем статус ответа

            soup = BeautifulSoup(response.text, 'html.parser')

            answer_list = []

            answers = soup.select('.answer.true', href=True)

            for answer in answers:
                text = answer.get_text(strip=True)
                answer_list.append(text)

            logger.info(f"Верные ответы: {answer_list}")


            answer_list = [s.lower().replace(' ', '') for s in answer_list]

            return answer_list

        except requests.RequestException as e:
            print(f"Ошибка при запросе к сайту: {e}")
            return []
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return []

    def get_list_question(self, course_link) -> list:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            response = requests.get(course_link, headers=headers)
            response.raise_for_status()  # Проверяем статус ответа

            soup = BeautifulSoup(response.text, 'html.parser')

            question_links = []

            links = soup.select('li a', href=True)

            for link in links:
                href = link['href']
                text = link.get_text(strip=True).lower()
                full_url = urljoin(course_link, href)

                # Проверяем, что ссылка ведет на тот же домен
                if 'vtone.ru' in full_url and full_url not in question_links:
                    question_links.append({
                        'title': link.get_text(strip=True).lower().replace(' ', ''),
                        'url': full_url
                    })

            return question_links

        except requests.RequestException as e:
            print(f"Ошибка при запросе к сайту: {e}")
            return []
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return []


if __name__ == '__main__':
    vtone = VtoneAnswers("Язык программирования Python")
    # print(vtone.get_list_question(vtone.course_link))

    # print(vtone.get_courses_list()[self.course_name])
    # print(vtone.get_list_question(vtone.course_link))
    # print(vtone.get_answer("Какие ошибки (и погрешности) допущены в следующем примере? fromaddr = \"tetja@abcde.ru\" toaddr = \"ktoto@edcba.ru\" message = \"\"\"Здравствуйте! Я ваша тетя. \"\"\" connect = SMTP('mail.abcde.ru') connect.sendmail(fromaddr, toaddr, message) connect.quit()",
    #                        [
    #                            "не обрабатываются исключения",
    #                            "в сообщении (message) не заданы поля",
    #                            "ошибок и существенных погрешностей нет', 'отсутствует указание порта SMTP (25)'",
    #                        ]))
