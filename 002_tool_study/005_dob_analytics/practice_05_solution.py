"""
Date of birth analytics
Given: a csv data with studentId and DoB of IU student
Expect: give some summary about IU student date of birth
- DoB month distribution: how many student born in Jan, Feb, ...?
"""
import csv
from datetime import datetime
import matplotlib.pyplot as plt


def year_birth_analytics(data):
    analytic_result = {}

    for line in data:
        try:
            dob = datetime.strptime(line[1], '%d/%m/%Y')
            if str(dob.year) not in analytic_result:
                analytic_result[str(dob.year)] = 0
            analytic_result[str(dob.year)] += 1
        except ValueError:
            print('data error - {}'.format(line))
    return analytic_result


def month_birth_analytics(data):
    analytic_result = [0 for _ in range(12)]

    for line in data:
        try:
            dob = datetime.strptime(line[1], '%d/%m/%Y')
            analytic_result[dob.month-1] += 1
        except ValueError:
            print('data error - {}'.format(line))
    return analytic_result


def main():
    csv_file = open('iu_data.csv', encoding="utf8")

    student_data = csv.reader(csv_file, delimiter=",")
    # Ignore header row
    next(student_data)
    student_data = list(student_data)

    month_analytic_result = month_birth_analytics(student_data)
    year_analytic_result = year_birth_analytics(student_data)

    f1 = plt.figure()
    ax1 = f1.add_subplot()
    ax1.plot(range(1, 13), month_analytic_result)

    f2 = plt.figure()
    ax2 = f2.add_subplot()
    ax2.plot(year_analytic_result.keys(), year_analytic_result.values())
    plt.show()


main()
