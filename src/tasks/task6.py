# given a string, text
# return the number of times 'lambda' can be formed from the text using each letter only once

def maxLambdas(text):
    # make a dictionary to hold letters from text as keys and their number of occurences as values
    letters = {}
    # loop through text
    for letter in text:
        # if letter is in dictionary
        if letter in letters:
            # increment letters
            letters[letter] += 1
        else:
            # add letter to dictionary with letter count of 1
            letters[letter] = 1

    # instantiate letter_count list to append to
    letter_count = []
    # loop through 'lambda'
    for letter in 'lambda':
        # if letter in letters
        if letter in letters:
            # append count to letter_count list
            letter_count.append(letters[letter])
        # if the letter isn't in the dictionary, no lambdas can be made, return 0
        else:
            return 0
    return min(letter_count)

print(maxLambdas("mbxcdatlas")) #--> 1
print(maxLambdas("lalaaxcmbdtsumbdav")) #--> 2
print(maxLambdas("sctlamb")) #--> 0