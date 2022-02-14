your_dear_student_datas = [
    {
        'name': 'Nguyen T.X.T.',
        'gender': 'male',
        'achievement': [
            'nth Vietnam Conference - FAIR 2020, research about something',
            'Student of infinity merits',
        ],
        'desire_university': 'VNU International University'
    },
    {
        'name': 'Duong B.N.L.',
        'gender': 'female',
        'achievement': [
            '100th Vietnam Conference - X, research about anything',
            'Student of infinity merits',
        ],
        'desire_university': 'University of Economics HCMC'
    }
]

# the data transform pipeline is
# raw data -> <transform> -> "letter needed data" -> letter

# this transform
# {name, gender, achievements[], desire_university}
# into
# {name, gender_pronoun, achievements, desire_university} (flattened)
def transform_data(data):
    gender_pronoun = 'He' if data['gender'] == 'male' else 'She'
