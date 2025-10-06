import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class VtoneBase:

    def __init__(self):
        self.course_list = self._get_courses_links("https://vtone.ru/")


    def _get_courses_links(self, url):
        """
        Парсит ссылки на курсы с сайта vtone.ru
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Проверяем статус ответа


            soup = BeautifulSoup(response.text, 'html.parser')


            course_links = {}

            links = soup.select('.list a', href=True)


            for link in links:
                href = link['href']
                text = link.get_text(strip=True).lower()
                full_url = urljoin(url, href)

                # Фильтруем ссылки, которые могут быть курсами
                # if any(keyword in text for keyword in course_keywords) or any(
                #         keyword in href.lower() for keyword in course_keywords):
                #     # Преобразуем относительные ссылки в абсолютные
                #     full_url = urljoin(url, href)

                    # Проверяем, что ссылка ведет на тот же домен
                if 'vtone.ru' in full_url and full_url not in course_links:
                    course_links[link.get_text(strip=True)] = full_url
            return course_links

        except requests.RequestException as e:
            print(f"Ошибка при запросе к сайту: {e}")
            return []
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return []

    def get_courses_list(self) -> list:
        return self.course_list


if __name__ == '__main__':
    vtone = VtoneBase()
    print(len(vtone.get_courses_list()))
