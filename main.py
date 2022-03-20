import random

#Board set and 8 Queens Positions start = (1,1) end = (8,8)
queens2 = [(1,1),(2,2)]
queens3 = [(2,1),(1,5),(3,6),(4,4),(5,2),(7,3),(6,7),(8,8)]
queens4 = [(1,1),(5,5),(4,6),(2,4),(2,7),(2,1),(8,7),(8,8)]
queens1 = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)]


#Maximum steps to solve else return Failure
MAX_STEPS = 70000
#Defining a render function for visual representation of board
def render(queen_pos):
    for i in range(10):
        for j in range(10):
            if j == 0 or j == 9:
                print('|', end = " ")
            elif i == 0 or i == 9:
                print('-', end = " ")
            elif (i,j) in queen_pos:
                print('Q', end = " ")
            else:
                print('.', end = " ")
        print()


#Function that counts the number of conflict for a test position and a board
def conflicts(test_pos, queen_pos):
    conflict_count = 0
    for (i,j) in queen_pos:
        if (i,j)!=test_pos and validtest((i,j),test_pos):   #Checks the conflict for other positions except it's own
            conflict_count += 1
    return conflict_count

#Gives a list of conflict positions in the current board, later to select one var randomly from this list
def conflicts_list(pos):
    conflict_list = []
    for (x,y) in pos:
        if conflicts((x,y), pos) != 0:
            conflict_list.append((x,y))
    return conflict_list

#Defines the valid steps that Queen can do, used in conflict function to denote conflict
def validtest(new_pos, old_pos):
    if new_pos[0] == old_pos[0] and new_pos[1] != old_pos[1]:
        return True
    if new_pos[1] == old_pos[1] and new_pos[0] != old_pos[0]:
        return True
    if abs(new_pos[0] - old_pos[0]) == abs(new_pos[1] - old_pos[1]):
        return True
    return False

#Check if the board is valid, that the board contains no conflict
def validboard(queens_pos):
    conf = 0
    for (i,j) in queens_pos:
            conf += conflicts((i,j),queens_pos)
    if conf == 0:
        return True
    else:
        return False

#Picks a random position of a Queen form the conflict list, (chooses one of the conflicted queen)
def randomconflictqueen(conflict_list):
    u = random.randint(0, len(conflict_list) - 1)
    var = conflict_list[u]
    return var

#Defines the available positions that the conflicted queen can move (i.e positions in column other that itself, or others)
def availablepos(current, x):
    availableP = []
    for i in range(1,9):
        if (i, x[0]) not in current and (i,x[0]) != x:
            availableP.append((i,x[0]))
    return availableP

#Move the choosen Queen to a new position in the table
def move(queens_pos, old_pos, new_pos):
    if old_pos in queens_pos:
        queens_pos.remove(old_pos)
        queens_pos.append(new_pos)
    return queens_pos


#Min Conflict algorithm, tries to solve in MAX_STEPS else return failure
def minConflict(queen_pos, MAX_STEPS):
    current = queen_pos
    for i in range(MAX_STEPS):
        print(i)
        if validboard(current):
            return current
        minimum = 9                                         #maximum value of conflict that may occur
        c_list = conflicts_list(current)                    #list of conflicted queens in the board
        picked_queen = randomconflictqueen(c_list)          #randomly choosing one of the conflicted queen
        a_positions = availablepos(current, picked_queen)   #available positions for the randomly choose
        #print(a_positions)
        minconflictPosition = (-1,-1)                       #minimum assignment to check against and update
        for pos in a_positions:
            move(current,picked_queen,pos)                  #move the picked queen to new position
            new_conflicts = conflicts(pos, current)         #check conflict on that position
            if new_conflicts < minimum:
                minconflictPosition = pos                   #keep the new position with minimum conflict
                minimum = new_conflicts                     #update the minimum parameter
            move(current,pos,picked_queen)                  #move queen back to original position and repeating this for all available postions

        move(current,picked_queen,minconflictPosition)      #move queen to spot with least conflict
    return 'Failure'

print('Original Chess Board Configuration with 8 Queens')
render(queens1)
print('\n\n')

print('8 Queen Problem solved using Min-Conflict')
#print(minConflict(queens1, MAX_STEPS))
if minConflict(queens1, MAX_STEPS) == 'Failure':
    print('Failure to solve in max steps')
else:
    render(minConflict(queens1, MAX_STEPS))

# print(validboard([(2,2),(3,1)]))
# print(conflicts((3,1),[(2,2),(3,1)]))
# print(validtest((3,1),(2,2)))