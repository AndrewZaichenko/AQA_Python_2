# 1. You have a list of elements [1, 2, 3, 4, 5, 6, 7, 8]. Loop through the list using the foreach loop.
# The element with an odd index is put into a new list of tuples where the first element is the index and the second
# is the value. [(index, value)]. accordingly, elements with an even index are placed in another list of tuples
# with the same format as in the case with odd indices.

list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_index_values = []  #нечетеные
even_index_values = [] #четеные


# for index, elem in enumerate(list_of_elements):
#     if index % 2 == 0:
#         even_index_list.append(index)
#     elif index % 2 != 0:
#         odd_index_list.append(index)
#
# print(odd_index_list)
# print(even_index_list)

for elem in list_of_elements:
    if list_of_elements.index(elem) % 2 == 0:
        even_index_values.append(elem)
    else:
        odd_index_values.append(elem)


for index, value in enumerate(odd_index_values):
    print(index, value)


print(odd_index_values)
print(even_index_values)





# 2. You have the number 2 as a variable. Multiply it by 2 in two ways.
# Accordingly, you need to divide it in 2 different ways by 2.

var_two = 2

multiply_way_1 = var_two * 2
var_two *= 2
print(multiply_way_1, var_two)

divide_way_1 = var_two / 2
var_two /= 2
print(divide_way_1, var_two)



# 3. You have 2 lists of names friends = ["John", "Marta", "James"] and enemies = ["John", "Johnatan", "Artur"].
# Loop through the names of friends and write the message f"{friend} we are the best friends" if
# the friend is not in the list of enemy names. And display the message f"{friend} we are not friends anymore"
# if the friend is on the list of enemies. If the friend's name is James, we don't check him because he is the best friend.