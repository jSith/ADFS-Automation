from ADFSReportItem import AdfsReportItem
import csv
import datetime
import os
import re


def read_report(day):
    # Input: a datetime object with the desired date
    # Output: an array of AdfsReportItems for that date
    # Make sure that you have your ADFS Logins report saved as a csv in a folder called data next to this script

    report = []
    path = os.getcwd() + '\data'
    file_name = 'New_Intl_ADFS_Logins-' + day.strftime('%Y-%m-%d') + '.csv'
    path_file = os.path.join(path, file_name)

    with open(path_file) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skipping the header
        for line in csv_reader:
            date = line[0]
            date = re.sub(' [0-9]{1,2}:[0-9]{2}', '', date)
            date = re.sub(' [0-9]{1,2}:[0-9]{2}:[0-9]{2}', '', date)
            try:
                date = datetime.datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                date = datetime.datetime.strptime(date, '%m/%d/%Y')
            uid = line[1]
            country = line[2]
            ip = line[3]
            report.append(AdfsReportItem(uid, date, country, ip))

    return report


def main():
    report = read_report(datetime.datetime.now())
    for item in report:
        print(item.to_string())


if __name__ == '__main__':
    main()
