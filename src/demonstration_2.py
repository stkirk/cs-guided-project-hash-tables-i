"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).

You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.

The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".

Example 1:

```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```

Example 2:

```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```

Example 3:

```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```

Notes:

- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
"""
Inputs:
words: List[str]
alpha_order: str

Output:
bool
"""

# helper function: takes two words and the alphabet we are using to compare them
def compare_two(word_a, word_b, alphabet):
    # go letter by letter until one word is exhausted of letters
    # we want our i to never go past the length of the shorter word
    # pass the two word lengths into the min() function and it will return the shorter of the two lengths
    for i in range(min(len(word_a), len(word_b))):
        # find the index of each letter from alpha_order alphabet
        index_value_a = alphabet[word_a[i]]
        index_value_b = alphabet[word_b[i]]
        # compare the index values
        if index_value_a == index_value_b:
            continue
        # return true or false according to the comparison operator
        return index_value_a < index_value_b
    # if we reach here without a return in the loop, the words were the same to the length of the shorter of the two words
    # check the length
    return len(word_a) <= len(word_b)

def are_words_sorted(words, alpha_order):
    # map the alpha order to a dictionary
    # letters are keys, their index is the value and denotes the order they appear in alpha_order
    # pass this into our comparison helper function
    alphabet = {letter:i for (i, letter) in enumerate(alpha_order)}

    # loop through the array of words, use range len(words)-1 because we don't need to compare the last word to nothing, that would create an out of range issue
    for i in range(len(words) - 1):
        # compare two items at a time: use helper function
        word_a = words[i]
        word_b = words[i + 1]
        if compare_two(word_a, word_b, alphabet):
            # the two items pass the comparison check (true)
            # continue to the next two items
            continue
        # else the words are out of order, return False
        else:
            return False
    # the loop has run through all the words without returning False, the words must be in order
    return True

print(are_words_sorted(["lambda","school"], "hlabcdefgijkmnopqrstuvwxyz")) #--> True
print(are_words_sorted(["were","where","yellow"], "habcdefgijklmnopqrstuvwxyz")) #--> False
print(are_words_sorted(["lambda","lamb"], "abcdefghijklmnopqrstuvwxyz")) #--> False
