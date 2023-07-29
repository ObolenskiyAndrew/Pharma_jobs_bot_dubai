from .basic_company import BasicCompany
import re


class Astrazeneca(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Astrazeneca'
        self.link = 'https://careers.astrazeneca.com/search-jobs/results?ActiveFacetID=290557-292224-292223' \
                    '&CurrentPage=1&RecordsPerPage=15&Distance=100&RadiusUnitType=0&Keywords=&Location=Dubai^%^2C' \
                    '+Dubai&Latitude=25.07725&Longitude=55.30927&ShowRadius=True&IsPagination=False&CustomFacetName' \
                    '=&FacetTerm=&FacetType=0&FacetFilters^%^5B0^%^5D.ID=290557-292224-292223&FacetFilters^%^5B0^%^5D' \
                    '.FacetType=4&FacetFilters^%^5B0^%^5D.Count=3&FacetFilters^%^5B0^%^5D.Display=Dubai^%^2C+Dubai' \
                    '^%^2C+United+Arab+Emirates&FacetFilters^%^5B0^%^5D.IsApplied=true&FacetFilters^%^5B0^%^5D' \
                    '.FieldName=&SearchResultsModuleName=Search+Results&SearchFiltersModuleName=Search+Filters' \
                    '&SortCriteria=0&SortDirection=0&SearchType=1&LocationType=4&LocationPath=290557-292224-292223' \
                    '&OrganizationIds=7684&PostalCode=&fc=&fl=&fcf=&afc=&afl=&afcf= '

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        titles = re.findall('<h2>(.*?)</h2>', response.text)
        links = re.findall('<a href=\\\\"(.*?)\\\\" data-job-id=\\\\"', response.text)[::2]
        links = ['https://careers.astrazeneca.com/' + i for i in links]
        ids = [i.split('/')[-1] for i in links]

        return titles, links, ids
