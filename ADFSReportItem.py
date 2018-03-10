import datetime
import data_abstraction


class AdfsReportItem(data_abstraction.IReportItem):
    def __init__(self, uid, date, country, ip):
        self.uid = uid
        self.date = date
        self.country = country
        self.ip = ip

    def uid(self):
        return self.uid

    def date(self):
        return self.date

    def country(self):
        return self.country

    def to_string(self):
        try:
            date_string = datetime.datetime.strftime(self.date, '%Y-%m-%d')
        except ValueError:
            date_string = datetime.datetime.strftime(self.date, '%d/%m/%Y')
        return date_string + ',' + self.uid + ',' + self.country + ',' + self.ip