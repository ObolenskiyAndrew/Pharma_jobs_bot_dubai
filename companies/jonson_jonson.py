from .basic_company import BasicCompany
import re


class JonsonJonson(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Jonson Jonson'
        self.link = 'https://jobs.jnj.com/en/jobs/?search=&location=Dubai&pagesize=20#results'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/39.0.2171.95 Safari/537.36'}

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        strings = re.findall('<a class="stretched-link js-view-job"(.*?)</a>', response.text)

        titles = [i.split('>')[-1] for i in strings]
        links = ["https://jobs.jnj.com/" + re.search('href="(.*?)">', i)[1] for i in strings]
        ids = [re.search('jobs/(.*?)/', i)[1] for i in strings]

        return titles, links, ids
