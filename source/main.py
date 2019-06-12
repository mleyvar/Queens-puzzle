
# Program:   Solution for Eigth Queens, only one solution
# Referebce: The reference is https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
#            Modify  the program 
from database import  add
import uuid
import os
import time

#---------------------  DEFINITION

NUM=0
xUuid=""
Board=[0][0]



# ------------------  METHODS

# Method:       getEnvironmenVar
# Description:  Get Value from environment variable
# Params:
# Return:       True: Assigne number to cold,rows  False=Error enviroment variable
def getEnvironmenVar():
    global NUM
    try:
        NUM = int(os.environ['NUM_QUEENS'])
        print("Value N:  %s" % NUM)
        return True
    except:
        print("An exception occurred in the N variable")
        return False

# Method:       iniBoard
# Description:  Initialize board in cols and rows
# Params:
# Return:      
def iniBoard():
    global Board
    Board = [ [0 for x in range( NUM )] for y in range( NUM ) ]  

    

# Method:       printBoard
# Description:  Print board cols and rows
# Params:       xUuid = session id
# Return:      
def printBoard(xUuid):
    order=0
    print("-----------------------------")
    for x in range(NUM):
        print (Board[x])
        for y in range(NUM):
            if Board[y][x]==1:
                order +=1
                add(xUuid,order,1,x,y)

# Method:       verifyQueen()
# Description:  Verify that the queen does not cross with another queen on the board
# Params:       posQueenX= position in X,  posQueenY= position in Y
# Return:      

def verifyQueen(posQueenX,posQueenY ):

    # find queen in vector X  
    if sum(Board[posQueenY]) >= 1:
        return False

    # find queen in diagonal left
    j=posQueenX
    for i in range(posQueenY,-1,-1):
        if Board[i][j]==1:
            return False
        else:
            j -=1    

    # find queen in diagonal rigth
    j=posQueenX
    for i in range(posQueenY,NUM,1):
        if Board[i][j]== 1:
            return False
        else:
            j -=1

    return True



# Method:       addQueen()
# Description:  recursive function for evaluate positions of queens
# Params:       col= position X
# Return:      
def addQueen(col):
    if col >= NUM:
        return True; 
    for i in range(NUM):
         if verifyQueen(col,i) == True:
              Board[i][col]=1
              #print("=============================> Add position: X= ",col, " Y=",i)
              #printBoard()
              #time.sleep(.5)
              if addQueen(col+1)==True:
                  return True
              Board[i][col]=0

    return False







# Method:       main()
# Description:  Start and control process
# Params:
# Return:      
def main():

    # Get environment variable
    getEnvironmenVar()
    
    # Create session UUID 
    xUuid = str(uuid.uuid4())
    print("================================================== UUID SESSION > ",xUuid)
    
    # Initialize Board
    iniBoard()

    if addQueen(0) == False:
        print("Solution does not exist") 


    printBoard(xUuid)


   



 
# Start process
if __name__ == "__main__":
   main()
