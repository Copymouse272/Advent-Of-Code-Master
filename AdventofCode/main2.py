

#open file
santa = open('2015\day 1\input.txt', 'r')
#read file
santa = santa.read()
#set floor level
floor_count = 0
position = 0


for character in santa:
    if floor_count >= 0:
        if character == '(':
            floor_count += 1
            position += 1
        elif character == ')':
            floor_count += -1
            position += 1
    #elif floor_count < 0:

print("Position is:", position)

