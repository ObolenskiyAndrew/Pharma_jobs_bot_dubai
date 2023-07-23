from .basic_compnay import BasicCompany
import re


class Roche(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Roche'
        self.link = 'https://careers.roche.com/widgets'
        self.method = "post"
        self.headers = {
            'authority': 'careers.roche.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://careers.roche.com',
            'referer': 'https://careers.roche.com/global/en/c/access-jobs',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-csrf-token': 'ff7bb6d8bc884f6cbf7fc5f1526601c8',
            'x-kl-ajax-request': 'Ajax_Request',
        }
        self.json_data = {
            'lang': 'en_global',
            'deviceType': 'desktop',
            'country': 'global',
            'pageName': 'search-results',
            'ddoKey': 'refineSearch',
            'sortBy': '',
            'subsearch': '',
            'from': 0,
            'jobs': True,
            'counts': True,
            'all_fields': [
                'category',
                'subCategory',
                'country',
                'state',
                'city',
                'type',
                'jobLevel',
                'jobType',
            ],
            'size': 10,
            'clearAll': False,
            'jdsource': 'facets',
            'isSliderEnable': False,
            'pageId': 'page11',
            'siteType': 'external',
            'keywords': '',
            'global': True,
            'selected_fields': {
                'state': [
                    'Dubai',
                ],
            },
            'locationData': {},
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        titles = [i['title'] for i in response.json()['refineSearch']['data']['jobs']]
        ids = [i['jobSeqNo'] for i in response.json()['refineSearch']['data']['jobs']]
        links = ['https://careers.roche.com/global/en/job/' + i for i in ids]

        return titles, links, ids
