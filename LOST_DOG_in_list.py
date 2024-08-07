# Find the Lost Dog
# 0 represents the dog.
# Each list represents a house and each 1 represents an empty room.
# Return the house and the room where it is located, there can be only one dog lost per building.
# Examples
# lost_dog([1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
# ➞ "Dog not found!"
#
# lost_dog([1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
# ➞ {"Dog1": "House (2) and Room (1)", "Dog2": "House (3) and Room (2)"}
#
# lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1])
# ➞ {"Dog1": "House (1) and Room (6)", "Dog2": "House (2) and Room (1)", "Dog3": "House (3) and Room (2)", "Dog4": "House (4) and Room (3)"}

def lost_dog(*args):
    dog_dict = {}
    c = 0
    for ith in range(len(args)):
        s = ""
        for jth in range(len(args[ith])):
            if args[ith][jth] == 0:
                c +=1
                s+="dog{}".format(c)
                dog_dict[s] = "House({}) and Room({})".format(ith+1 , jth+1)

    return dog_dict if dog_dict else "Dog Not found"


print(lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1]))