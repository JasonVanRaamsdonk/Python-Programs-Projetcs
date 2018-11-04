
locations = {0: "You are sitting in front of a computer",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

vocabulary = {"QUIT": "Q",
              "NORTH":"N",
              "SOUTH": "S",
              "EAST": "W",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}

loc = 1
while True:
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    else:
        allExists = exits[loc].copy()
        allExists.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    # parse user input using vocabulary dictionary

    # if len(direction) > 1:
    #     for word in vocabulary: # does it contain a word we know
    #         direction = vocabulary[word]

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExists: # if valid location
        loc = allExists[direction]
    else:
        print("You cannot go in that direction")

# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))
