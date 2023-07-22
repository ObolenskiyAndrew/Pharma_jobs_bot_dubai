import pandas as pd
from datetime import datetime
from companies import *
import passwords


class CurrentJobs:
    def __init__(self):
        self.data = pd.DataFrame(columns=['title', 'company', 'link', 'id'])
        self.errors = []
        self.get_all_current_jobs_data()

    def __repr__(self):
        return f"{self.data.shape[0]} current jobs on {datetime.today().strftime('%Y-%m-%d')}"

    def get_all_current_jobs_data(self):
        self.add_jobs_and_errors(Sanofi())
        self.add_jobs_and_errors(Novartis())
        self.add_jobs_and_errors(Gsk())
        self.add_jobs_and_errors(Astrazeneca())

    def add_jobs_and_errors(self, company):
        self.data = self.data.append(company.job_data)
        self.errors += company.job_errors
        print(f'{company.name} {company.job_data.shape[0]} jobs')

    def update_data(self, jobs_current, errors_current):
        pass

    def make_log(self, jobs_database, update_date, errors_current):
        pass

    def send_results_to_bot(self, chat_id, data, errors):
        pass


if __name__ == '__main__':
    current_jobs = CurrentJobs()
    # current_jobs.update_data()
    # current_jobs.make_log()
    # current_jobs.send_results_to_bot()
