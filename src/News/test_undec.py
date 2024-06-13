import undetected_chromedriver as uc
import time
from undetected_chromedriver import By


class Driver:
    def __init__(self, options):
        driver = uc.Chrome(options=options)
        self.driver = driver

    def get_page(self, url: str):
        self.driver.get(url)


def create_driver(options):
    driver = uc.Chrome(options=options)
    return driver


def get_page(url: str, driver):
    driver.get(url)


def find_elements_by_class_name(driver, class_names:[]):
    all_blocks = []
    for class_name in class_names:
        blocks = driver.find_elements(By.CLASS_NAME, class_name)
        all_blocks += blocks
    return all_blocks


options = uc.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')

driver = create_driver(options)
get_page('https://www.bloomberg.com/search?query=Tesla', driver)

div_blocks = find_elements_by_class_name(driver, ['thumbnailWrapper__23c201ad78'])

links_from_page = []
for d in div_blocks:
    links_from_page.append(d.get_attribute('href'))

print(links_from_page)
time.sleep(10)

for link in links_from_page:
    get_page(link, driver)
    class_names = ['media-ui-Paragraph_text-SqIsdNjh0t0-', 'media-ui-Paragraph_text-SqIsdNjh0t0- paywall']
    blocks  = find_elements_by_class_name(driver, class_names)
    for block in blocks:
        print('text', block.text)

    print('------------------------')
    time.sleep(10)
