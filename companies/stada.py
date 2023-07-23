from .basic_compnay import BasicCompany
import re


class Stada(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'STADA'
        self.link = 'https://jobs.stada.com/search/'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Referer': 'https://jobs.stada.com/search/?createNewAlert=false&q=&locationsearch=&optionsFacetsDD_country=AE&optionsFacetsDD_lang=&optionsFacetsDD_customfield5=',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.params = {
            'createNewAlert': 'false',
            'q': '',
            'locationsearch': '',
            'optionsFacetsDD_country': 'AE',
            'optionsFacetsDD_lang': '',
            'optionsFacetsDD_customfield5': '',
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        all_text = re.search('<div class="tiletitle">(.*?)</div>', response.text.replace('\n', ''))[1]
        strings = re.findall('<a class="jobTitle-link.*?</a>', all_text)
        strings = [re.sub(' +', ' ', i) for i in strings]

        titles = [re.search('">(.*?)</a>', i)[1] for i in strings]
        links = ["https://jobs.stada.com" + re.search('href="(.*?)/">', i)[1] for i in strings]
        ids = [i.split('/')[-1] for i in links]

        return titles, links, ids


