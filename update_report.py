import csv
import datetime
from GeneratedReportItem import GeneratedReportItem
import read_adfs_report
import read_generated_report


def update_report(date):
    adfs_report = read_adfs_report.read_report(date)
    generated_report = read_generated_report.read_report()
    updated_report = []

    for adfs_item in adfs_report:
        generated_item = generated_report.get(adfs_item.uid)
        if generated_item:
            new_item = update_date(adfs_item, generated_item)
        else:
            new_item = GeneratedReportItem(adfs_item.uid, adfs_item.date, adfs_item.date, adfs_item.country)
        updated_report.append(new_item)

    return updated_report


def update_date(adfs_item, generated_item):
    if adfs_item.date > generated_item.date:
        generated_item.date = adfs_item.date
    return generated_item


def main():
    updated_report = update_report(datetime.datetime.now())

    with open('data/Splunk_Alerts_Intl_Logins_Test.csv', 'w') as new_report:
        writer = csv.writer(new_report)
        for item in updated_report:
            writable = [item.first_seen, item.date, item.uid, item.country, str(item.status), item.notes, str(item.need_to_check)]
            writer.writerow(writable)

if __name__ == '__main__':
    main()
