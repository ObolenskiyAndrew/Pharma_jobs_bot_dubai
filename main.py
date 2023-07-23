import pandas as pd
from datetime import datetime
from companies import *
import passwords


class CurrentJobs:
    def __init__(self):
        self.day = datetime.today().strftime('%Y-%m-%d')
        self.data = pd.DataFrame(columns=['title', 'company', 'link', 'id'])
        self.errors = []
        self.get_all_current_jobs_data()
        self.data_all = pd.read_csv("data/jobs_database_dubai.csv").reset_index(drop=True)

    def __repr__(self):
        return f"{self.data.shape[0]} current jobs on {self.day}"

    def get_all_current_jobs_data(self):
        self.add_jobs_and_errors(Sanofi())
        self.add_jobs_and_errors(Novartis())
        self.add_jobs_and_errors(Gsk())
        self.add_jobs_and_errors(Astrazeneca())

        self.data['upload_date'] = self.day

    def add_jobs_and_errors(self, company):
        self.data = self.data.append(company.job_data)
        self.errors += company.job_errors
        print(f'{company.name} {company.job_data.shape[0]} jobs')

    def update_data(self):
        """
        input dataframe columns: [title, company, link, id, upload_date, purge_date, status]

        status can be:

        new - job was first found today
        current - job was first found before today and is still in the list of current jobs
        expired - job was can no longer be found in the list of current jobs
        """

        self.data_all = self.data_all.append(self.data)
        self.data_all.reset_index(drop=True, inplace=True)

        # expired
        self.data_all.status = 'expired'

        # current
        self.data_all.loc[
            (self.data_all.duplicated(subset=['company', 'id'], keep='last')) &
            (self.data_all.upload_date != self.day),
            'status'
        ] = 'current'

        # new
        self.data_all.drop_duplicates(
            subset=['company', 'id'],
            keep='first',
            inplace=True
        )
        self.data_all.loc[self.data_all.upload_date == self.day, 'status'] = 'new'

        # add missing purge_date to expired jobs
        self.data_all.loc[
            (self.data_all.status == 'expired') &
            (self.data_all.purge_date.isnull()),
            'purge_date'
        ] = self.day

        # write data to csv
        self.data_all.to_csv("data/jobs_database_dubai.csv", index=False)

    def make_log(self):
        pass

    def send_results_to_bot(self, chat_id):
        pass


if __name__ == '__main__':
    current_jobs = CurrentJobs()
    current_jobs.update_data()
    # current_jobs.make_log()
    # current_jobs.send_results_to_bot()
