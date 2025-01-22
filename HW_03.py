# 1. You have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop.
# The element with an odd index is put into a new list of tuples where the first element is the index and the second
# is the value. [(index, value)]. accordingly, elements with an even index are placed in another list of tuples
# with the same format as in the case with odd indices.

list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_index_values = []  # %2 != 0
even_index_values = []  # %2 == 0

# indexed_tuples = list(enumerate(my_list))

for tuple_index_value in enumerate(list_of_elements):
    if tuple_index_value[0] % 2 != 0:
        odd_index_values.append(tuple_index_value)
    else:
        even_index_values.append(tuple_index_value)

print(f'The new list with odd indexes and its values {odd_index_values}')
print(f'The new list with even indexes and its values {even_index_values}')


# 2. You have the number 2 as a variable. Multiply it by 2 in two ways.
# Accordingly, you need to divide it in 2 different ways by 2.

var_two = 2

multiply_way_1 = var_two * 2
var_two *= 2
print(multiply_way_1, var_two)

divide_way_1 = var_two / 2
var_two /= 2
print(divide_way_1, var_two)


# 3. You have 2 lists of names friends = ["John", "Marta", "James"] and enemies = ["John", "Johnathan", "Artur"].
# Loop through the names of friends and write the message f"{friend} we are the best friends" if
# the friend is not in the list of enemy names. And display the message f"{friend} we are not friends anymore"
# if the friend is on the list of enemies. If the friend's name is James, we don't check him because he is the best friend.

list_of_friends = ["John", "Marta", "James"]
list_of_enemies = ["John", "Johnathan", "Artur"]

for friend in list_of_friends:
    if friend == 'James':
        continue
    elif friend not in list_of_enemies:
        print(f"{friend} we are the best friends")
    else:
        print(f"{friend} we are not friends anymore")
