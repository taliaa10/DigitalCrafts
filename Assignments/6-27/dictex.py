
# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-3841234',
#     'Elizabeth': '484-584-2923'
# }

# print(phonebook_dict['Alice'])

# phonebook_dict['Kareem'] = '938-489-1234'


# print(phonebook_dict)

# del phonebook_dict['Alice']

# print(phonebook_dict)

# phonebook_dict['Bob'] = '968-345-2345'

# print(phonebook_dict)


ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interest': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interest': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interest': ['movies', 'tv']
        }
    ]
}

print(ramit['email'])

print(ramit['interest'][0] + " - " + ramit['email'])

# print(ramit['friends']['name'])