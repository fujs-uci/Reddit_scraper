import time
import datetime

class unixTimes:
        def __init__(self):
                self.times = []
                self.datetimes = []
                self.fillDict()

        def getTimes(self):
                return self.times

        def getDateTimes(self):
                return self.datetimes

        def fillDict(self):
                years = 12
                leap = [2008, 2012, 2016]
                curr_year = 2006

                for x in range(years):
                        days = 28

                        month = [i+1 for i in range(12)]
                        for y in month:
                                if y <= 7:
                                        if y % 2 == 0:
                                                if y != 2:
                                                        days = 30
                                                else:
                                                        if curr_year in leap:
                                                                days = 29
                                        else:
                                                days = 31
                                else:
                                        if y % 2 == 0:
                                                if y != 2:
                                                        days = 31
                                                else:
                                                        if curr_year in leap:
                                                                days = 29
                                        else:
                                                days = 30

                                first_day = datetime.datetime(curr_year, y, 1, 0, 0, 0, tzinfo=datetime.timezone.utc)
                                sec_day = datetime.datetime(curr_year, y, days, 23, 59, 59, tzinfo=datetime.timezone.utc)
                                self.datetimes.append((first_day, sec_day))
                                self.times.append((first_day.timestamp(), sec_day.timestamp()))
                                days = 28

                        curr_year = curr_year + 1
