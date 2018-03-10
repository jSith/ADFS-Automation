import datetime
import data_abstraction
from StatusEnum import Status


class GeneratedReportItem(data_abstraction.IReportItem):
    def __init__(self, uid, first_seen, last_seen, country, status=Status.UNVERIFIED, notes='Autogenerated'):
        self.uid = uid
        self.first_seen = first_seen
        self.date = last_seen
        self.country = country
        self.status = status
        self.notes = notes
        self.need_to_check = True

    def uid(self):
        return self.uid

    def date(self):
        return self.date

    def country(self):
        return self.country

    def to_string(self):

        if self.first_seen:
            first_seen_string = datetime.datetime.strftime(self.first_seen, '%d/%m/%Y')
        else:
            first_seen_string = ''

        if self.date:
            date_string = datetime.datetime.strftime(self.date, '%d/%m/%Y')
        else:
            date_string = ''

        return first_seen_string + ',' + date_string + ',' + self.uid + ',' + self.country + ',' + str(self.status) + ',' + self.notes + ',' + str(self.need_to_check)