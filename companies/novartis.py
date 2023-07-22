from .basic_compnay import BasicCompany
import re


class Novartis(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Novartis'
        self.link = 'https://www.novartis.com/careers/career-search'
        self.headers = {
            'authority': 'www.novartis.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://www.novartis.com/careers/career-search?search_api_fulltext=&early_talent=All',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="109", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }
        self.params = {
            'search_api_fulltext': '',
            'country[]': 'LOC_AE',
            'field_alternative_country[]': 'LOC_AE',
            'early_talent': 'All',
            'items_per_page': '10',
            'field_job_posted_date': 'All',
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        strings = re.findall('<a href="/careers/career-search/job-details.*?</a>', response.text)

        titles = [i.replace('&amp;', '-') for i in re.findall('>(.*?)</a>', '\n'.join(strings))]
        ids = re.findall('/careers/career-search/job-details/(.*?)/', '\n'.join(strings))
        links = ['https://www.novartis.com' + i for i in re.findall('href="(.*?)"', '\n'.join(strings))]

        return titles, links, ids


