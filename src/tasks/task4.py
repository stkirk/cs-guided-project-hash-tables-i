# given an array on integers:
# find and return the integer that only appears once in the array

def areYouTheOne(nums):
    # initialize an empty dictionary to map nums to
    num_dict = {}
    # map the array to a dictionary with num as key and a counter as teh value
    for num in nums:
        # if the num already exists as a key:
        if num in num_dict:
            # increment the value by 1
            num_dict[num] += 1
        # if it doesn't already exist in the dict
        else:
            # add it as a new key with a value of 1
            num_dict[num] = 1

    # loop through the array
    for num in nums:
        # check each num against the dictionary
        # if the num has a value of 1 in the dictionary
        if num_dict[num] == 1:
            # return the number
            return num
    return "no unique integer in list"

print(areYouTheOne([1,1,2,1])) #--> 2
print(areYouTheOne([1,2,1,2,1,2,80])) #--> 80
print(areYouTheOne([1,2,1,2,1,2])) #--> "no unique integer in list"

# ternary
age = 18
message = "Eligible" if age >= 18 else "Not eligible"
print("ternary message:", message)
