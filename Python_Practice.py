
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")

print(" ")
print("breaK")
print(" ")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):

      print(voting_data[i]['county'])

print(" ")

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print(" ")
#Retrieve the number of reg voters from dictionary
for county_dict in voting_data:

     print(county_dict['registered_voters'])

#F String Example
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Multiline F-Strings
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
 #   f"You received {candidate_votes} number of votes. "
  #  f"The total number of votes in the election was {total_votes}. "
   # f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

print(" ")

#3.2.11 Skill Drill
for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")

print(" ")

#for county, registered_voters in voting_data.items():
 #   print(county, "county has", str(registered_voters), "registered voters.")

for county_something in voting_data:
    print(county_something["county"], " county has ", county_something["registered_voters"], " registered voters. ")
