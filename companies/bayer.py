from .basic_compnay import BasicCompany
import re


class Bayer(BasicCompany):
    def __init__(self):
        BasicCompany.__init__(self)
        self.name = 'Bayer'
        self.link = 'https://www.linkedin.com/jobs/search'
        self.headers = {
            'authority': 'www.linkedin.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://www.linkedin.com/jobs/search?keywords=Bayer&location=Germany&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }
        self.params = {
            'keywords': 'Bayer',
            'location': 'Объединённые Арабские Эмираты',
            'locationId': '',
            'geoId': '104305776',
            'f_TPR': '',
            'f_C': '1893',
        }
        self.cookies = {
            'bcookie': '"v=2&a4055848-917b-4b33-876e-374308ab36c4"',
            'lang': 'v=2&lang=ru-ru',
            'li_sugr': '22fb5d1f-ea92-47cd-a047-7059aa4a25e1',
            'JSESSIONID': 'ajax:2712551685155961440',
            'bscookie': '"v=1&202209162222258aa24965-70fb-490c-8920-159ac7eb777fAQH9IyyAKfYvAL8TzbkNKdswfLBs3dF4"',
            'li_alerts': 'e30=',
            'li_gc': 'MTsyMTsxNjYzMzY2OTUxOzI7MDIxrOk8y9pRKP0IxDYS/GNt0nKoJYs/mMxd19sxsfgY6dM=',
            'G_ENABLED_IDPS': 'google',
            '_gcl_au': '1.1.583393403.1667670641',
            'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg': '1',
            'aam_uuid': '48614076084777968060843432622060465049',
            'g_state': '{"i_p":1667998166582,"i_l":2}',
            'UserMatchHistory': 'AQIBhi_iWseLjwAAAYRsxvfYN1g8YRdSvVf1poJlFWMjdLRm4W7oCgFoqkqEsZCJUFbBmVSp2NQWxw',
            'AnalyticsSyncHistory': 'AQLUhHzruA6YZQAAAYRsxvfYwsOiwkR3Bcw93ydYZHjI4G-VkLOuWVJMvQdC7u_XuK5y4-0PJ1clWHXvOQyH8g',
            'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C19332%7CMCMID%7C48796845998710277250827350326185105490%7CMCAAMLH-1668516563%7C6%7CMCAAMB-1670259000%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1670266210s%7CNONE%7CvVersion%7C5.1.1',
            'lidc': '"b=OGST00:s=O:r=O:a=O:p=O:g=2861:u=1:x=1:i=1670259632:t=1670346032:v=2:sig=AQF9h8pdgIfqtSZmunwYaEDOVVYdld7h"',
        }

        self.get_company_jobs_data()

    @staticmethod
    def convert_response(response):
        strings = re.findall('<a class="base-card__full-link.*?</a>', response.text.replace('\n', '').replace('\n', ''))
        strings = [re.sub(' +', ' ', i) for i in strings]

        titles = [re.search('<span class="sr-only">(.*?)</span>', i)[1].strip() for i in strings]
        links = [re.search('href="(.*?)"', i)[1].strip() for i in strings]
        ids = [re.search('bayer-(\d*)', i)[1] for i in links]

        return titles, links, ids

