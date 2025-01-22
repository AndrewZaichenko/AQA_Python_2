# task_2
# You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba. Show it in code.
# Keep in mind that people with the same name can be in both companies

eleks_personal = {'Erik', 'Michael', 'Ann', 'Olena'}
toshiba_personal = {'Dan', 'Erik', 'Irina', 'Michael', 'Ann', 'Olena', 'Jack'}

if eleks_personal.issubset(toshiba_personal):
    print('Eleks was taken over by Toshiba')
else:
    print('Eleks was not taken over by Toshiba')


# task_3
# You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name. Find those who are on all blacklists.

casino_blacklist = {'John Doe', 'Lara Croft', 'Erik Schrody', 'Mike Tyson'}
poker_blacklist = {'John Down', 'James Brown', 'Mike Tyson'}
alcohol_blacklist = {'John Dow', 'Jack Sparrow', 'Mike Tyson'}

person_in_all_blacklists = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)

print(f'{person_in_all_blacklists} is present in all blacklists')


# task_4
# You have two groups of people. One group consists of omnivores, the other only vegetarians.
# An omnivore is a vegetarian but a vegetarian is not an omnivore.
# Display a list of guests who can eat vegetables and herbs.

omnivore_guests = ['Dan', 'Erik', 'Irina', 'Michael', 'Ann', 'Olena', 'Jack']
vegetarian_guests = ['John', 'Lara Croft', 'Erik Schrody', 'Mike Tyson']

vegetarian_guests.extend(omnivore_guests)

print(f'The list of guests who can eat vegetables and herbs - {vegetarian_guests}')


# task_5
# You have a group of guests for the VIP box.
# The seats in the VIP box are all occupied by these guests and can not be changed.
# There is a group of guests in the common room and there are still places in it. Display 2 groups of guests in code.

guests_in_vip = ('John Dow', 'Jack Sparrow', 'Mike Tyson')
print(f'These guests are VIP: {guests_in_vip}', type(guests_in_vip))
guests_in_common = ['Olena', 'Dan', None, 'Michael', None]
print(f'These guests are in the common room and there are still places in it: {guests_in_common}', type(guests_in_common))

# task_6
# You have a group of people with non-unique names.
# Generate a list of non-duplicate names (you cannot use set for this task. If there are 2 johns in the list,
# you need to take only one of them. "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")

non_unique_list = ['Olena', 'Dan', 'Erik', 'Irina', 'Michael', 'Ann', 'Olena', 'Erik', 'Jack']
unique_list = []

for name in non_unique_list:
    if name not in unique_list:
        unique_list.append(name)

print(unique_list)
