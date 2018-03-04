daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:           
                return False
        return True
    else:
        return False

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    initial_date = "%s/%s/%s" % (m1, d1, y1)
    final_date = "%s/%s/%s" % (m2, d2, y2)
    yrs_in_days = 0
    mo_in_days = 0

    # calculates the number of days from m1/d1/y1 to end of y1
    # EX: July 2, 1992 to December 31, 1992
    i = m1
    while i <= 12:
        if i == m1:
            mo_in_days += (daysOfMonths[i-1] - d1)
        else:
            mo_in_days += daysOfMonths[i-1]
        i += 1

    # calculates the number of days between beginning of y1+1 to end of y2-1
    # EX: January 1, 1993 to December 31, 2017
    while (y1+1) < y2:
        if isLeapYear(y1):
            yrs_in_days += 366
        else:
            yrs_in_days += 365
        y1 += 1

    # calculates the number of days from beginning of y2 to m2/d2/y2
    # EX: January 1st, 2018 to March 4th, 2018
    i = 1
    while i <= m2:
        if i == m2:
            mo_in_days += d2
        else:
            mo_in_days += daysOfMonths[i-1]
        i += 1
        
    total_days = yrs_in_days + mo_in_days
    print("The number of days between " + initial_date + " and " + final_date + " is: " + str(total_days))
        
daysBetweenDates(1992, 7, 2, 2018, 3, 4)
daysBetweenDates(2012, 12, 7, 2012, 12, 7)
daysBetweenDates(2012, 12, 7, 2012, 12, 8)
daysBetweenDates(2012, 12, 8, 2012, 12, 7)
daysBetweenDates(2012, 6, 29, 2013, 6, 29)
daysBetweenDates(2012, 6, 29, 2013, 6, 31)
