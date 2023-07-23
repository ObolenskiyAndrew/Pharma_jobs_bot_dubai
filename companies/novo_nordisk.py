from .basic_compnay import BasicCompany
import re


class NovoNordisk(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Novo Nordisk'
        self.link = 'https://www.novonordisk.com/bin/nncorp/careersearch'
        self.headers = {
            'authority': 'www.novonordisk.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': '',
            'referer': 'https://www.novonordisk.com/careers/find-a-job/career-search-results.html?searchText=&countries=Australia&categories=',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-kl-ajax-request': 'Ajax_Request',
        }
        self.params = {
            'keyword': '',
            'country': 'United Arab Emirates',
            'category': '',
            'locale': 'en',
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        titles = [i['jobTitle'] for i in response.json()['data']['jobs']]
        ids = [str(i['jobId']) for i in response.json()['data']['jobs']]
        links = [f'https://www.novonordisk.com/content/nncorp/global/en/careers/find-a-job/job-ad.{i}.html' for i in
                 ids]

        return titles, links, ids


