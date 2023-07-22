from .basic_compnay import BasicCompany
import re


class Sanofi(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Sanofi'
        self.link = 'https://en.jobs.sanofi.com/search-jobs/results'
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=utf-8',
            'Referer': 'https://en.jobs.sanofi.com/search-jobs',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'X-KL-Ajax-Request': 'Ajax_Request',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.params = {
            'ActiveFacetID': '290557-292224-292223',
            'CurrentPage': '1',
            'RecordsPerPage': '10',
            'Distance': '50',
            'RadiusUnitType': '0',
            'Keywords': '',
            'Location': '',
            'ShowRadius': 'False',
            'IsPagination': 'False',
            'CustomFacetName': '',
            'FacetTerm': '',
            'FacetType': '0',
            'FacetFilters[0].ID': '290557-292224-292223',
            'FacetFilters[0].FacetType': '4',
            'FacetFilters[0].Count': '1',
            'FacetFilters[0].Display': 'Dubai, Dubai, United Arab Emirates',
            'FacetFilters[0].IsApplied': 'true',
            'FacetFilters[0].FieldName': '',
            'SearchResultsModuleName': 'Search Results',
            'SearchFiltersModuleName': 'Search Filters',
            'SortCriteria': '0',
            'SortDirection': '0',
            'SearchType': '5',
            'PostalCode': '',
            'fc': '',
            'fl': '',
            'fcf': '',
            'afc': '',
            'afl': '',
            'afcf': '',
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        strings = re.findall('/job/.*?</a>', response.text.replace('\n', ''))
        strings = [re.sub(' +', ' ', i) for i in strings]

        titles = [re.search('<h2>(.*?)</h2>', i)[1] for i in strings]
        links = ["https://en.jobs.sanofi.com" + i[:i.find('\\')] for i in strings]
        ids = [i.split('/')[-1] for i in links]

        return titles, links, ids


