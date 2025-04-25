''' This program will create the list , Extract the selective elements and then reverse the selected list '''

# created list using list comprehension

original_list = [x for x in range(1,11)]

#Taking out first 5 element
first_five = reversed_list = original_list[0:5]
#Reversing the list
reversed_list.reverse()

print(f"Original list: {original_list}")
print(f"Extracted first five elements: {first_five}")
print(f"Reversed extracted elements: {reversed_list}")