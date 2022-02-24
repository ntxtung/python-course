"""
Student confirmation - CSV
For this challenge, your target is read the data as json type from a separate csv file (data.csv).
And write out the letters to each file.
"""
import csv


def row_map(row):
    return {
        'studentId': row[0],
        'fullName': row[1],
        'birthday': row[2],
        'birthplace': row[3],
        'schoolYear': '{} - {}'.format(row[4], row[5]),
        'formal': row[6],
        'department': row[7],
        'expiredDate': row[8],
        'reason': row[9],
    }


def write_to_file(template: str, data, filename):
    output_file = open(filename, 'w', encoding="utf8")
    mapped_data = row_map(data)
    output_file.write(template.format(**mapped_data))
    output_file.close()
    print('Processed {sid}'.format(sid=mapped_data['studentId']))


def main():
    csv_file = open('data.csv', encoding="utf8")
    template_file = open('template.txt', encoding="utf8")

    student_data = csv.reader(csv_file, delimiter=",")
    # Ignore header row
    next(student_data)
    template = template_file.read()

    for line in student_data:
        write_to_file(template, line, 'output-{}.txt'.format(line[0]))


main()
