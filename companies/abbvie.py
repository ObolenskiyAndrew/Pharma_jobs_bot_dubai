from .basic_compnay import BasicCompany
import re


class AbbVie(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'AbbVie'
        self.link = 'https://careers.abbvie.com/en/search-jobs/results'
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=utf-8',
            'Referer': 'https://careers.abbvie.com/en/search-jobs?k=&l=Dubai%2C+Dubai&orgIds=14',
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
            'ActiveFacetID': '290557',
            'CurrentPage': '1',
            'RecordsPerPage': '15',
            'Distance': '50',
            'RadiusUnitType': '0',
            'Keywords': '',
            'Location': 'Dubai, Dubai',
            'ShowRadius': 'False',
            'IsPagination': 'False',
            'CustomFacetName': '',
            'FacetTerm': '',
            'FacetType': '0',
            'FacetFilters[0].ID': '290557',
            'FacetFilters[0].FacetType': '2',
            'FacetFilters[0].Count': '1',
            'FacetFilters[0].Display': 'United Arab Emirates',
            'FacetFilters[0].IsApplied': 'true',
            'FacetFilters[0].FieldName': '',
            'SearchResultsModuleName': 'Search Results',
            'SearchFiltersModuleName': 'Search Filters',
            'SortCriteria': '0',
            'SortDirection': '0',
            'SearchType': '1',
            'OrganizationIds': '14',
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
        strings = re.findall('/en/job/.*?</a>', response.text.replace('\n', ''))
        strings = [re.sub(' +', ' ', i) for i in strings]

        titles = [re.search('<h2>(.*?)</h2>', i)[1] for i in strings]
        links = ["https://careers.abbvie.com/" + i[:i.find('\\')] for i in strings]
        ids = [i[i.rfind('/') + 1:] for i in links]

        return titles, links, ids
