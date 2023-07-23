from .basic_compnay import BasicCompany
import re


class Pfizer(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Pfizer'
        self.link = 'https://pfizer.wd1.myworkdayjobs.com/wday/cxs/pfizer/PfizerCareers/jobs'
        self.method = "post"
        self.headers = {
            'Accept': 'application/json',
            'Accept-Language': 'ru-RU',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://pfizer.wd1.myworkdayjobs.com',
            'Referer': 'https://pfizer.wd1.myworkdayjobs.com/ru-RU/PfizerCareers?locations=e2d3979e3af101fe2cbf7566076cae9b',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'X-KL-Ajax-Request': 'Ajax_Request',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="109", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.json_data = {
            'appliedFacets': {
                'locations': [
                    'e2d3979e3af101fe2cbf7566076cae9b',
                ],
            },
            'limit': 20,
            'offset': 0,
            'searchText': '',
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        titles = [i['title'] for i in response.json()['jobPostings']]
        links = ['https://pfizer.wd1.myworkdayjobs.com/ru-RU/PfizerCareers' + i['externalPath'] for i in
                 response.json()['jobPostings']]
        ids = [i['bulletFields'][0] for i in response.json()['jobPostings']]

        return titles, links, ids
