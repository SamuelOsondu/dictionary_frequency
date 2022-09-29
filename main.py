words = "The little red fox jumped over a fence and bit a python"

# Remove the spaces
letters = words.replace(" ", "")

# create a dict with all frequencies
number_appeared = {}
for each_letter in letters:

    if each_letter in number_appeared:
        number_appeared[each_letter] += 1
    else:
        number_appeared[each_letter] = 1

# Create a function to order the frequencie
# s
def frequencies_ordered(my_dict):
    if len(my_dict) != 0:

        highest = 0
        highest_letter = None
        for letter, frequency in my_dict.items():
            if frequency > highest:
                highest = frequency
                highest_letter = letter
        print(f"{highest_letter} : {highest}", end=" ")
        new_dict = {key: val for key, val in my_dict.items() if key != highest_letter}
        frequencies_ordered(new_dict)


frequencies_ordered(number_appeared)

