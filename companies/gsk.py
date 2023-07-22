from .basic_compnay import BasicCompany
import re


class Gsk(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'GSK'
        self.link = 'https://jobs.gsk.com/api/jobs'
        self.headers = {
            'authority': 'jobs.gsk.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://jobs.gsk.com/en-gb/jobs?keywords=&lang=en-gb&page=1&location=Dubai,%20United%20Arab%20Emirates&woe=7&stretchUnit=MILES&stretch=0',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="109", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-kl-ajax-request': 'Ajax_Request',
        }
        self.params = {
            'keywords': '',
            'lang': 'en-gb',
            'page': '1',
            'location': 'Dubai%2C%20United%20Arab%20Emirates',
            'woe': '7',
            'stretchUnit': 'MILES',
            'stretch': '0',
            'sortBy': 'relevance',
            'descending': 'false',
            'internal': 'false',
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        strings = re.findall('<a href="/careers/career-search/job-details.*?</a>', response.text)

        titles = [i.replace('&amp;', '-') for i in re.findall('>(.*?)</a>', '\n'.join(strings))]
        ids = re.findall('/careers/career-search/job-details/(.*?)/', '\n'.join(strings))
        links = ['https://www.novartis.com' + i for i in re.findall('href="(.*?)"', '\n'.join(strings))]

        return titles, links, ids


