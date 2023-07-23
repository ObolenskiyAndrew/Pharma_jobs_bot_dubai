from .basic_compnay import BasicCompany
import re


class Iqvia(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'IQVIA'
        self.link = 'https://jobs.iqvia.com/search-jobs/results'
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=utf-8',
            'Referer': 'https://jobs.iqvia.com/search-jobs/Dubai%2C%20Dubai/24443/4/290557-292224-292223/25x07725/55x30927/50/2',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'X-KL-Ajax-Request': 'Ajax_Request',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.params = {
            'ActiveFacetID': '290557-292224-292223',
            'CurrentPage': '1',
            'RecordsPerPage': '12',
            'Distance': '50',
            'RadiusUnitType': '0',
            'Keywords': '',
            'Location': 'Dubai, Dubai',
            'Latitude': '25.07725',
            'Longitude': '55.30927',
            'ShowRadius': 'True',
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
            'SortDirection': '1',
            'SearchType': '1',
            'LocationType': '4',
            'LocationPath': '290557-292224-292223',
            'OrganizationIds': '24443',
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

        titles = [re.search('<h2 class=\\\\"job-info job-title js-trim-txt\\\\">(.*?)</h2>', i)[1] for i in strings]
        links = ["https://jobs.iqvia.com/" + i[:i.find('\\')] for i in strings]
        ids = [re.search('\|</span>(.*?)</span>', i)[1] for i in strings]

        return titles, links, ids


