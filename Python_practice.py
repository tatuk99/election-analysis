counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if "El Paso" in counties:
    print("El Paso is in the counties list")
else:
    print ("El Paso is not in the list")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are part of the list")
else:
    print("Arapahoe or El Paso are not in the list")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])


counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(str(county) + " county has " + str(voters) + " registered voters")
    print(f"{county} county has {voters:,} registered voters")

