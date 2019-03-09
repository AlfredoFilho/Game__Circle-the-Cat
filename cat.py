'''
*******************Developed by:********************************
    
Alfredo Albelis Batista Filho - https://github.com/AlfredoFilho
Brenda Alexsandra Januario - https://github.com/brendajanuario
Cleofas Peres Santos -

**************************************************************** 
'''

import sys
cat    = eval(sys.argv[1])
blocks = eval(sys.argv[2])
exits  = eval(sys.argv[3])

startPosition = cat
chosen_exit = exits
catInTuple = tuple(cat)
positionsVisited = []
expandedStates = []

def next_move(direction, cat) :
    candidatos = {
        "NW": [(cat[0]-1, cat[1]-1), (cat[0]-1, cat[1])],
        "NE": [(cat[0] - 1, cat[1]), (cat[0]-1, cat[1] + 1)],
        "W" : [(cat[0], cat[1] - 1), (cat[0], cat[1] - 1)],
        "E" : [(cat[0], cat[1] + 1), (cat[0], cat[1] + 1)],
        "SW": [(cat[0] + 1, cat[1] - 1),(cat[0] + 1, cat[1])],
        "SE": [(cat[0] + 1, cat[1]),(cat[0] + 1, cat[1]+1)]
    }
    return candidatos[direction][cat[0]%2]

def BreadthFirstSearch (cat, chosen_exit, blocks):

    solutionFound = False
    positionsVisited.append(cat) #add cat in list of positions visited
    
    while len(positionsVisited) != 0:
        atual = positionsVisited.pop(0) #remove first of list
        if(atual not in blocks and atual in chosen_exit):
            solutionFound = True
            break
        successorStates = findSuccessorPositions(atual, expandedStates, positionsVisited) #call function to walk with the cat and find the next positions
        expandedStates.append(atual)

        for i in range (0, len(successorStates)): #check the new positions to see if they have already been included
            successor = successorStates[i]
            if successor not in expandedStates and successor not in positionsVisited:
                positionsVisited.append(successorStates[i])
 
    if solutionFound == True:
        movimento = Solution(atual)
        expandedStates.clear()
        positionsVisited.clear()
        successorStates.clear()
        print(movimento[-1])
    return 0
    
predecessorCoordinates={}
predecessorPosition={}

def findSuccessorPositions(cat, expandedStates, positionsVisited):
    coordinates = ["NE","E","SW","SE","W","NW"]
    successorPositions=[]
    for el in coordinates:
        successor = next_move(el, cat)
        if (successor[0]<0 or successor[1]<0 or successor[0]>10 or successor[1]>10):
            continue
        elif(successor in blocks):
            continue
        elif(successor not in expandedStates and successor not in positionsVisited and successor not in blocks):
            successorPositions.append(successor)
            predecessorCoordinates[successor]=el
            predecessorPosition[successor]=cat
    
    return successorPositions
    
def Solution(cat):
    listPositions=[]
    listCoordinates=[]
    aux=cat
    listPositions.append(cat)
    while (aux != tuple(startPosition)):
        listPositions.append(predecessorPosition[aux])
        listCoordinates.append(predecessorCoordinates[aux])
        aux = predecessorPosition[aux]
    return listCoordinates

BreadthFirstSearch(catInTuple, chosen_exit, blocks)