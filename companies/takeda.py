from .basic_company import BasicCompany
import re


class Takeda(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Takeda'
        self.link = 'https://www.takedajobs.com/search-jobs/results'
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=utf-8',
            'Referer': 'https://www.takedajobs.com/search-jobs?k=&l=Berlin%2C+Land+Berlin&r=25&orgIds=1113',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'X-KL-Ajax-Request': 'Ajax_Request',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="109", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.json_data = {
            'ActiveFacetID': '3996063',
            'CurrentPage': '1',
            'RecordsPerPage': '15',
            'Distance': '25',
            'RadiusUnitType': '0',
            'Keywords': '',
            'Location': '',
            'ShowRadius': 'False',
            'IsPagination': 'False',
            'CustomFacetName': '',
            'FacetTerm': '',
            'FacetType': '0',
            'FacetFilters[0].ID': '290557',
            'FacetFilters[0].FacetType': '2',
            'FacetFilters[0].Count': '4',
            'FacetFilters[0].Display': 'United Arab Emirates',
            'FacetFilters[0].IsApplied': 'true',
            'FacetFilters[0].FieldName': '',
            'SearchResultsModuleName': 'Search Results',
            'SearchFiltersModuleName': 'Search Filters',
            'SortCriteria': '0',
            'SortDirection': '0',
            'SearchType': '1',
            'OrganizationIds': '1113',
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
        titles = [i['title'] for i in response.json()['refineSearch']['data']['jobs']]
        ids = [i['jobSeqNo'] for i in response.json()['refineSearch']['data']['jobs']]
        links = ['https://careers.roche.com/global/en/job/' + i for i in ids]

        return titles, links, ids
