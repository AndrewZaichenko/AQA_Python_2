# task_2
# You have 2 companies with people. One of the companies, let it be Eleks, was taken over by Toshiba. Show it in code.
# Keep in mind that people with the same name can be in both companies """

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


