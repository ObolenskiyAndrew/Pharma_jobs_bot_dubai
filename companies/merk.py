from .basic_compnay import BasicCompany
import re


class Merk(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Merk'
        self.link = 'https://jobs.merck.com/widgets'
        self.method = "post"
        self.headers = {
            'authority': 'jobs.merck.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://jobs.merck.com',
            'referer': 'https://jobs.merck.com/us/en/c/research-development-jobs',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-csrf-token': '621d88de0e064da88183d07723498c6d',
        }
        self.json_data = {
            'lang': 'en_us',
            'deviceType': 'desktop',
            'country': 'us',
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
                'divisionList',
                'locationType',
            ],
            'size': 10,
            'clearAll': False,
            'jdsource': 'facets',
            'isSliderEnable': False,
            'pageId': 'page2',
            'siteType': 'external',
            'keywords': '',
            'global': True,
            'selected_fields': {
                'country': [
                    'United Arab Emirates',
                ],
            },
            'locationData': {},
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        titles = [i['title'].replace('&', '-') for i in response.json()['refineSearch']['data']['jobs']]
        links = [i['applyUrl'].replace('/apply', '') for i in response.json()['refineSearch']['data']['jobs']]
        ids = [str(i['reqId']) for i in response.json()['refineSearch']['data']['jobs']]

        return titles, links, ids

