def getLowestCommonManager(topManager, reportOne, reportTwo):
    return helper(topManager, reportOne, reportTwo).manager


def helper(manager, report_one, report_two):
    reports_count = 0
    for report in manager.directReports:
        org_info = helper(report, report_one, report_two)
        if org_info.manager:  # manager != None if we found 2 target reports
            return org_info
        reports_count += org_info.reports_count
    if manager == report_one or manager == report_two:
        reports_count += 1
    return OrgInfo(manager if reports_count == 2 else None, reports_count)


class OrgInfo:
    def __init__(self, manager, reports_count):
        self.manager = manager
        self.reports_count = reports_count


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
