"""
Date of birth analytics
Given: a csv data with studentId and DoB of IU student
Expect: give some summary about IU student date of birth
- DoB month distribution: how many student born in Jan, Feb, ...?
"""
import csv
from datetime import datetime
import matplotlib.pyplot as plt


def process_data(data):
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

    analytic_result = process_data(student_data)

    plt.plot(range(1, 13), analytic_result)
    plt.show()


main()
