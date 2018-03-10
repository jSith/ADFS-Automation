import csv
import datetime
from GeneratedReportItem import GeneratedReportItem
import os


def read_report():
    # Output: a dictionary mapping uid strings to GeneratedReportItems
    # Have your report saved as Splunk_Alerts_Intl_Logins.csv in a folder called data next to this script

    report = {}
    path = os.getcwd() + '\data'
    file_name = 'Splunk_Alerts_Intl_Logins.csv'
    path_file = os.path.join(path, file_name)

    with open(path_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in range(0,4):
            next(csv_reader)  # Skipping the header and legend

        for line in csv_reader:
            first_seen = line[0]
            if first_seen:
                first_seen = datetime.datetime.strptime(first_seen, '%m/%d/%Y')
            else:
                first_seen = None

            last_seen = line[1]
            if last_seen:
                last_seen = datetime.datetime.strptime(line[1], '%m/%d/%Y')
            else:
                last_seen = None

            uid = line[2]
            country = line[3]
            status = line[4]
            notes = line[5]

            report[uid] = GeneratedReportItem(uid, first_seen, last_seen, country, status, notes)

    return report


def main():
    report = read_report()
    for item in report.values():
        print(item.to_string())


if __name__ == '__main__':
    main()
