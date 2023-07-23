import pandas as pd
from datetime import datetime
import requests
from companies import *
from passwords import TELEGRAM_BOT_TOKEN, CHAT_ID1, CHAT_ID2


class CurrentJobs:
    def __init__(self):
        self.day = datetime.today().strftime('%Y-%m-%d')
        self.data = pd.DataFrame(columns=['title', 'company', 'link', 'id'])
        self.errors = []
        self.get_all_current_jobs_data()

        self.data_all = pd.read_csv("data/jobs_database_dubai.csv").reset_index(drop=True)
        self.log = pd.read_csv("data/log_table_dubai.csv")

    def __repr__(self):
        return f"{self.data.shape[0]} current jobs on {self.day}"

    def get_all_current_jobs_data(self):
        self.add_jobs_and_errors(Sanofi())
        self.add_jobs_and_errors(Novartis())
        self.add_jobs_and_errors(Gsk())
        self.add_jobs_and_errors(Astrazeneca())
        self.add_jobs_and_errors(Pfizer())
        self.add_jobs_and_errors(Roche())
        # self.add_jobs_and_errors(Takeda())
        self.add_jobs_and_errors(JonsonJonson())
        self.add_jobs_and_errors(Merk())
        self.add_jobs_and_errors(Bayer())
        self.add_jobs_and_errors(BoehringerIngelheim())
        self.add_jobs_and_errors(Iqvia())
        self.add_jobs_and_errors(NovoNordisk())
        # self.add_jobs_and_errors(AbbVie())
        self.add_jobs_and_errors(EliLilly())
        self.add_jobs_and_errors(Stada())

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
        """
        input dataframe columns: [date, new_jobs, overall_jobs, expired_jobs, errors]

        """

        log_row = [
            self.day,
            len(self.data_all[self.data_all.status == 'new']),
            len(self.data_all[self.data_all.status.isin(['new', 'current'])]),
            len(self.data_all[self.data_all.purge_date == self.day]),
            ' | '.join(self.errors)
        ]

        self.log.loc[len(self.log)] = log_row
        self.log.to_csv("data/log_table_dubai.csv", index=False)

        print(
            f'New jobs {log_row[1]}\n'
            f'Expired jobs {log_row[3]}\n'
            f'Overall jobs {log_row[2]}\n\n'
            f'Errors: {len(self.errors)}')

    def send_results_to_bot(self, chat_id):
        data_new = self.data_all[self.data_all.status == 'new']
        bot_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={chat_id}&parse_mode" \
                  f"=markdown&disable_web_page_preview=true&text="

        if len(data_new) > 0:
            bot_message = '*НОВЫЕ ВАКАНСИИ ДУБАЯ НА ' + datetime.today().strftime('%d-%m-%Y') + '*'
        else:
            bot_message = '*НОВЫХ ВАКАНСИЙ ДУБАЯ НА ' + datetime.today().strftime('%d-%m-%Y') + ' НЕТ*'

        requests.get(bot_url + bot_message)

        for company_name in data_new.company.unique().tolist():
            bot_message = f'*{company_name}*\n'

            for i in data_new[data_new.company == company_name].index:
                bot_message += f'\n• [{data_new.loc[i, "title"].replace("&", "-").replace("#", "")}]' \
                               f'({data_new.loc[i, "link"]})'

                if len(bot_message) > 3000:
                    requests.get(bot_url + bot_message)
                    bot_message = ''

            requests.get(bot_url + bot_message)

        if self.errors:
            bot_message = "*bot errors*\n\n" + '\n'.join(self.errors)
            requests.get(bot_url + bot_message)


if __name__ == '__main__':
    current_jobs = CurrentJobs()
    current_jobs.update_data()
    current_jobs.make_log()
    current_jobs.send_results_to_bot(CHAT_ID1)
