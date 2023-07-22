import pandas as pd
import requests


class BasicCompany:
    def __init__(self):
        self.link = None
        self.headers = None
        self.params = None
        self.cookies = None
        self.json_data = None

        self.response = None
        self.job_errors = []
        self.job_data = pd.DataFrame(columns=['title', 'link', 'id', 'company'])

    def get_company_jobs_data(self):
        try:
            self.get_response()
            self.job_data = self.convert_response_to_job_data()
        except:
            self.job_errors += [f'{self.name} fatal error']

    def get_response(self):
        self.response = requests.get(
            'https://en.jobs.sanofi.com/search-jobs/results',
            params=self.params,
            headers=self.headers,
            cookies=self.cookies,
            json=self.json_data
        )

        if self.response.status_code != 200:
            self.job_errors = [f'{self.name} !=200 error']

    def convert_response_to_job_data(self):
        titles, links, ids = self.convert_response(self.response)

        data = pd.DataFrame({'title': titles, 'link': links, "id": ids})
        data['company'] = self.name
        return data
