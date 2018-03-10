from enum import Enum
import re


class Status(Enum):
    UNVERIFIED = 1
    VERIFIED_BY_TRAVEL_REPORT = 2
    VERIFIED_BY_RESEARCH_REPORT = 3
    TRIP_EXPIRED = 4
    COUNTRY_UNEXPECTED = 5
    ADJUNCT = 6
    AFFILIATE = 7
    RETIREE = 8
    STUDENT = 9
    TEMP_WORKER = 10
    VOLUNTEER = 11


def string_to_enum(string):
    if re.search('verified by travel report', string):
        return parse_travel_status(string)
    elif re.search('verified by research report', string):
        return parse_travel_status(string)
    elif re.search('adjunct faculty - unable to verify', string):
        return Status.ADJUNCT
    elif re.search('(retiree|emeritus) - unable to verify', string):
        return Status.RETIREE
    elif re.search('student - unable to verify', string):
        return Status.STUDENT
    elif re.search('volunteer - unable to verify', string):
        return Status.VOLUNTEER
    else:
        return Status.UNVERIFIED


def parse_travel_status(string):
    location = re.search('in .+ until', string)
    return_date = re.search('until [0-9]{1,2}/{0-9]{1,2}/[0-9]{2,4}', string)
