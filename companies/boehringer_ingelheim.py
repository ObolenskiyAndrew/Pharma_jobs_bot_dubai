from .basic_compnay import BasicCompany
import re


class BoehringerIngelheim(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Boehringer Ingelheim'
        self.link = 'https://tas-boehringer.taleo.net/careersection/rest/jobboard/searchjobs'
        self.method = "post"
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://tas-boehringer.taleo.net',
            'Referer': 'https://tas-boehringer.taleo.net/careersection/global+template+career+section+28external29/jobsearch.ftl?lang=en',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'X-KL-Ajax-Request': 'Ajax_Request',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'tz': 'GMT+03:00',
            'tzname': 'Europe/Moscow',
        }
        self.params = {
            'lang': 'en',
            'portal': '14105022295',
        }
        self.json_data = {
            'multilineEnabled': False,
            'sortingSelection': {
                'sortBySelectionParam': '1',
                'ascendingSortingOrder': 'false',
            },
            'fieldData': {
                'fields': {
                    'KEYWORD': '',
                    'LOCATION': '1090205022295',
                    'CATEGORY': '',
                },
                'valid': True,
            },
            'filterSelectionParam': {
                'searchFilterSelections': [
                    {
                        'id': 'JOB_FIELD',
                        'selectedValues': [],
                    },
                    {
                        'id': 'JOB_SCHEDULE',
                        'selectedValues': [],
                    },
                    {
                        'id': 'POSTING_DATE',
                        'selectedValues': [],
                    },
                ],
            },
            'advancedSearchFiltersSelectionParam': {
                'searchFilterSelections': [
                    {
                        'id': 'ORGANIZATION',
                        'selectedValues': [],
                    },
                    {
                        'id': 'LOCATION',
                        'selectedValues': [],
                    },
                    {
                        'id': 'JOB_FIELD',
                        'selectedValues': [],
                    },
                    {
                        'id': 'JOB_NUMBER',
                        'selectedValues': [],
                    },
                    {
                        'id': 'URGENT_JOB',
                        'selectedValues': [],
                    },
                    {
                        'id': 'EMPLOYEE_STATUS',
                        'selectedValues': [],
                    },
                    {
                        'id': 'JOB_SHIFT',
                        'selectedValues': [],
                    },
                ],
            },
            'pageNo': 1,
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        titles = [i['column'][0] for i in response.json()['requisitionList']]
        ids = [str(i['contestNo']) for i in response.json()['requisitionList']]
        links = [
            'https://tas-boehringer.taleo.net/careersection/global+template+career+section+28external29/jobdetail.ftl' \
            '?job=' + i
            for i in ids]

        return titles, links, ids


