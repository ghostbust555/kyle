'''
Created on Apr 11, 2013

@author: Kyle
'''
import random

def generateMaze():  
  maze = []
  for x in range(10):
    row = [0]*10
    maze.append(row)
    for y in range(10):
      maze[x][y] = '.' if random.randint(0,3) else 'w'     
    print(row)
    
  maze[0][0]='.'
  maze[9][9]='.'
  print()
  return maze

def placeStep(maze,step,cX,cY):
  steps = {}
  
  if(cX + 1 <= 9 and maze[cX + 1][cY] == '.'):
    maze[cX+1][cY] = str(step)
    steps[cX+1]=cY
    
  if(cY + 1 <= 9 and maze[cX][cY + 1] == '.'):
    maze[cX][cY+1] = str(step)
    steps[cX]=cY+1
    
  if(cX - 1 >= 0 and maze[cX - 1][cY] == '.'):
    maze[cX-1][cY] = str(step)
    steps[cX-1]=cY
    
  if(cY - 1 >= 0 and maze[cX][cY - 1] == '.'):
    maze[cX][cY-1] = str(step)
    steps[cX]=cY-1
    
  return steps
  
def solveMaze(): #go from 0,0 to 9,9 if possible
  maze = generateMaze()
  
  xStart = 0
  yStart = 0
  xEnd, cX = 9,9
  yEnd, cY = 9,9  
  
  step = 1
  maze[9][9]=0
  
  allSteps = []
  steps = {xEnd:yEnd}
  allSteps.append(steps)
  print(allSteps)
  exit=False
  pX,pY = -1,-1
  while((cX != 0 or cY != 0) and not exit):
    nextSteps = []
    for steps in allSteps:      
      for cX,cY in steps.items(): 
         nextSteps.append(placeStep(maze,step,cX,cY))
            
      for row in maze:
        print(row)
      print()
      print(allSteps)
    step += 1
    allSteps = nextSteps
    if(pX == cX and pY == cY):
      if(maze[0][0]=='.'):
        print("Unsolvable MAZE")
      exit = True
    pX,pY=cX,cY
  print("DONE")
  
  return maze
  
def tracePath():
  maze = solveMaze()
  