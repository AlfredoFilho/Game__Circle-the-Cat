'''
*******************Developed by:********************************
    
Alfredo Albelis Batista Filho - https://github.com/AlfredoFilho
Brenda Alexsandra Januario - https://github.com/brendajanuario
Cleofas Peres Santos -

**************************************************************** 
'''

import sys
import random
from math import sqrt

cat    = eval(sys.argv[1])
blocks = eval(sys.argv[2])
exits  = eval(sys.argv[3])

catInTuple = tuple(cat)
startPosition = cat
positionsVisited = [] #positions that have already been visited
expandedStates = [] #positions that have been visited that have formed other positions in the list
exitCloser=0

'''************ Initializing Hexagons **************'''
#Open the image "hexagons.png" in folder to know the hexagons according to the colors

hexBlue = []
hexPink = []
hexYellow = []
'''**************************************************'''

'''*************************************Blue Hexagon***********************************************'''

vertBlue_all = [(5, 0), (10, 3), (10, 8), (5, 10), (0, 8), (0, 3)]#all vertices blue hexagon

#all blue hexagon coordinates
hexBlue = [(5, 0), (6, 1), (7, 1), (8, 2), (9, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), 
(10, 8), (9, 8), (8, 9), (7, 9), (6, 10), (5, 10), (4, 10), (3, 9), (2, 9), (1, 8), 
(0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (1, 2), (2, 2), (3, 1), (4, 1)]
'''*************************************************************************************************'''

'''*************************************Pink Hexagon***********************************************'''

vertPink_all = [(4, 0), (10, 3), (10, 9), (7, 10), (0, 7), (0, 2)]#all pink blue hexagon

#all pink hexagon coordinates
hexPink = [(4, 0), (5, 0), (6, 1), (7, 1), (8, 2), (9, 2), (10, 3), (10, 4), (10, 5), (10, 6), 
(10, 7), (10, 8), (10, 9), (9, 9), (8, 10), (7, 10), (6, 10), (5, 9), (4, 9), (3, 8), 
(2, 8), (1, 7), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (1, 1), (2, 1), (3, 0)]

'''*************************************************************************************************'''

'''*************************************Yellow Hexagon********************************************'''

vertYellow_all = [(6, 0), (10, 2), (10, 7), (3, 10), (0, 9), (0, 3)]#all vertices yellow hexagon

#all yellow hexagon coordinates
hexYellow = [(6, 0), (7, 0), (8, 1), (9, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), 
(9, 7), (8, 8), (7, 8), (6, 9), (5, 9), (4, 10), (3, 10), (2, 10), (1, 9), (0, 9), 
(0, 8), (0, 7), (0, 6), (0, 5), (0, 4), (0, 3), (1, 2), (2, 2), (3, 1), (4, 1), (5, 0)]

'''*************************************************************************************************'''

#generates a random coordinate near the cat - this function is used after it has no more outputs
def generate_random(used) :
    candidate = (random.randint(cat[0]-1, cat[0]+1)), random.randint(cat[1]-1, cat[1]+1)
    while (candidate in used) or (cat[0] < 0 or cat[0] > 10 or cat[1] < 0 or cat[1] > 10 or cat in candidate) :
        candidate = (random.randint(cat[0]-1, cat[0]+1)), random.randint(cat[1]-1, cat[1]+1) 
    return candidate

def printVertice(available, blocks, cat, catInTuple, vertices_All, menorCoordenada):
        
        result = all(element in blocks for element in available)
        
        if result:
            controle = 0
            while controle == 0:
                print(generate_random(blocks + [tuple(cat)]))
                controle = 1
    
        DisTVertSemBlocks = []
        for el in vertices_All:
            if el not in blocks and el not in catInTuple:
                DisTVertSemBlocks.append(el)

        dist = 100
        for el in available:
            if (el not in blocks and el not in catInTuple):       
                a = sqrt(((cat[0]-el[0])**2 + (cat[1] - el[1])**2))
                if(a < dist):
                    dist=a
        
        MenorVert = (11, 11)
        
        distVertice = 100
        for el in vertices_All:
            if (el not in blocks and el not in catInTuple):       
                a = sqrt(((cat[0]-el[0])**2 + (cat[1] - el[1])**2))
                if(a < distVertice):
                    distVertice=a
                    MenorVert=el
                 
        if (dist >= 2 and distVertice >= 3.1622776601683795):
            
            if MenorVert != (11, 11):
                print(MenorVert)
            
            else:
                print(menorCoordenada)
                
        else:
            print(menorCoordenada)
                    
cAzul = 0
cRosa = 0
cAmarelo = 0

for el in blocks:
    if (el in vertBlue_all):
        cAzul = cAzul + 1

for el in blocks:
    if (el in vertPink_all):
            cRosa = cRosa + 1

for el in blocks:
    if (el in vertYellow_all):
            cAmarelo = cAmarelo + 1

'''**********************************************************************************'''
if (cAzul > cRosa and cAzul > cAmarelo):
        available = []  
        available = hexBlue
        allVerticesOfTheChosenHexagon = vertBlue_all

elif (cRosa > cAzul and cRosa > cAmarelo):
        available = []  
        available = hexPink
        allVerticesOfTheChosenHexagon = vertPink_all
                        
elif (cAmarelo > cRosa and cAmarelo > cAzul):
        available = []      
        available = hexYellow
        allVerticesOfTheChosenHexagon = vertYellow_all
                                        
else:
    available = []  
    available = hexBlue
    allVerticesOfTheChosenHexagon = vertBlue_all
        
##########################################################################
    
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


def BreadthFirstSearch (cat, chosen_exit,blocks):

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
        return movimento
    
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
    return listPositions

caminho = BreadthFirstSearch(catInTuple, available, blocks)

result = all(element in blocks for element in available)
    
if result:
    print(generate_random(blocks + [tuple(cat)]))

else:
    for el in available: 
        if el in caminho and el not in blocks:
            for way in caminho:
                if (el == way):
                    printVertice(available, blocks, cat, catInTuple, allVerticesOfTheChosenHexagon, el)
        
