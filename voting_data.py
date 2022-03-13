voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
for i in range(len(voting_data)):
    print(voting_data[i]['county'])


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


for d in voting_data:
    county = d.get('county')
    voters = '{:,}'.format(d.get('registered_voters'))
    print(f'{county} county has {voters} registered voters.')

