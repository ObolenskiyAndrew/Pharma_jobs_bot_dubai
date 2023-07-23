from .basic_compnay import BasicCompany
import re


class EliLilly(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Eli Lilly'
        self.link = 'https://careers.lilly.com/widgets'
        self.method = "post"
        self.headers = {
            'authority': 'careers.lilly.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://careers.lilly.com',
            'referer': 'https://careers.lilly.com/us/en/search-results',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'x-csrf-token': '9d897353df4443e493df90353c6f0e9d',
            'x-kl-ajax-request': 'Ajax_Request',
        }
        self.json_data = {
            'lang': 'en_us',
            'deviceType': 'desktop',
            'country': 'us',
            'pageName': 'search-results',
            'ddoKey': 'eagerLoadRefineSearch',
            'sortBy': '',
            'subsearch': '',
            'from': 0,
            'jobs': True,
            'counts': True,
            'all_fields': [
                'category',
                'country',
                'state',
                'city',
                'postalCode',
                'type',
                'phLocSlider',
            ],
            'size': 10,
            'clearAll': False,
            'jdsource': 'facets',
            'isSliderEnable': True,
            'pageId': 'page11',
            'siteType': 'external',
            'keywords': '',
            'global': True,
            'selected_fields': {
                'country': [
                    'United Arab Emirates',
                ],
            },
            'locationData': {
                'sliderRadius': 50,
                'aboveMaxRadius': True,
                'LocationUnit': 'miles',
            },
            's': '1',
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        titles = [i['title'] for i in response.json()['eagerLoadRefineSearch']['data']['jobs']]
        links = [i['applyUrl'].replace('/apply', '') for i in response.json()['eagerLoadRefineSearch']['data']['jobs']]
        ids = [i['jobId'] for i in response.json()['eagerLoadRefineSearch']['data']['jobs']]

        return titles, links, ids


