import time
import datetime

import jsonlines
import undetected_chromedriver as uc
from undetected_chromedriver import By
from typing import NamedTuple


class ChromeDriver:
    '''создание драйвера'''
    driver: uc.Chrome

    def __init__(self, options):
        driver = uc.Chrome(options=options)
        self.driver = driver

    def set_current_page(self, url: str):
        self.driver.get(url)

    def find_elements_by_class_name(self, class_names: [str]) -> [uc.webelement]:
        all_elements = []

        for class_name in class_names:
            elements = self.driver.find_elements(By.CLASS_NAME, class_name)
            all_elements += elements

        return all_elements


class Page(NamedTuple):
    link: str
    content: str


def _get_links_from_web_elements(elements: [uc.webelement]):
    '''извлечение ссылок с поисковой страницы новостей'''
    links = []
    for element in elements:
        links.append(element.get_attribute('href'))
    return links


def _get_pages_contents(driver, links, class_names) -> [Page]:
    '''извлечение содержимого с конкретной страницы новости'''
    pages = [Page]
    for link in links:
        driver.set_current_page(link)
        div_elements = driver.find_elements_by_class_name(class_names)
        content = ''
        for element in div_elements:
            content += element.text

        pages.append(Page(link, content))
        time.sleep(10)
    return pages


def get_pages_from_Bloomberg(main_url: str, names_classes_web_elements: [str]) -> [Page]:
    options = uc.ChromeOptions()
    options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_driver = ChromeDriver(options)

    chrome_driver.set_current_page(main_url)

    elements_with_links = chrome_driver.find_elements_by_class_name(['thumbnailWrapper__23c201ad78'])

    links = _get_links_from_web_elements(elements_with_links)

    pages = _get_pages_contents(chrome_driver, links, names_classes_web_elements)

    chrome_driver.driver.quit()
    return pages


if __name__ == '__main__':

    #создание jnonl фаила
    def create_jsonl(outputfile, pages: [Page]):
        with open(outputfile, 'w') as output_file:
            json_writer = jsonlines.Writer(output_file)

            for page in pages:
                s = f"link: {page.link} " \
                    f"content: {page.content}"
                json_writer.write({"page_content": s})


    t1 = datetime.datetime.now()

    #опции для бразузера
    options = uc.ChromeOptions()
    options.add_argument('--blink-settings=imagesEnabled=false')

    #создаем броаузер
    chrome_driver = ChromeDriver(options)
    #начальная страница
    chrome_driver.set_current_page('https://www.bloomberg.com/search?query=Tesla')

    #элементы на начальной странице, которые содержат ссылки
    elements_with_links = chrome_driver.find_elements_by_class_name(['thumbnailWrapper__23c201ad78'])

    #получаем ссылки из элементов
    links = _get_links_from_web_elements(elements_with_links)

    #элементы в которых находится текст страниц
    class_names = ['media-ui-Paragraph_text-SqIsdNjh0t0-', 'media-ui-Paragraph_text-SqIsdNjh0t0- paywall']

    #получаем текст со страниц, первые 2 ссылки(для примера)
    for page in _get_pages_contents(chrome_driver, links[:2], class_names):
        print(page)

    create_jsonl('pages_content.jsonl', _get_pages_contents(chrome_driver, links[:2], class_names))

    t2 = datetime.datetime.now()
    print('time', t2 - t1)

    chrome_driver.driver.quit()
