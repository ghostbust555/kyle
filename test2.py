'''
Created on Apr 11, 2013

@author: Kyle
test
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
    maze[cX+1][cY] = step
    steps[cX+1]=cY
    
  if(cY + 1 <= 9 and maze[cX][cY + 1] == '.'):
    maze[cX][cY+1] = step
    steps[cX]=cY+1
    
  if(cX - 1 >= 0 and maze[cX - 1][cY] == '.'):
    maze[cX-1][cY] = step
    steps[cX-1]=cY
    
  if(cY - 1 >= 0 and maze[cX][cY - 1] == '.'):
    maze[cX][cY-1] = step
    steps[cX]=cY-1
    
  return steps
  
def solveMaze(): #go from 0,0 to 9,9 if possible
  maze = generateMaze()
  
  xStart = 0
  yStart = 0
  xEnd, cX = 9,9
  yEnd, cY = 9,9  
  
  step = 1
  maze[9][9]='x'
  
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
  print("Blake has a vag")
  
  return maze
  
def tracePath():
  maze = solveMaze()
  
  x,y = 0,0
  exit = False
  
  while((x!= 9 or y!= 9) and not exit):
    dir = {}
    
    if(x + 1 <= 9 and maze[x + 1][y] != '.' and maze[x + 1][y] != 'w'):
      dir['right'] = maze[x + 1][y]      
      
    if(x - 1 >= 0 and maze[x - 1][y] != '.' and maze[x - 1][y] != 'w'):
      dir['left'] = maze[x - 1][y]
            
    if(y - 1 >= 0 and maze[x][y - 1] != '.' and maze[x][y-1] != 'w'):
      dir['up'] = maze[x][y - 1]
      
    if(y + 1 <= 9 and maze[x][y + 1] != '.' and maze[x][y+1] != 'w'):
      dir['down'] = maze[x][y + 1]
      
    vals = []
    for key, value in dir.items():
      if(value == 'x'):
        print('done')
        exit=True
        break
      if(value!=0):
        print(value)
        vals.append(value)
    
    if(len(vals)>0):
      vals.sort()
      theKey = ''
      for key, value in dir.items():
        if(vals[0] == value):
          print(vals[0],':',key)
          theKey = key
          break
      
      print(theKey)
        
      if(theKey == 'right'):
        maze[x+1][y]=0
        x+=1
      elif(theKey == 'left'):
        maze[x-1][y]=0
        x-=1
      elif(theKey == 'up'):
        maze[x][y-1]=0
        y-=1
      elif(theKey == 'down'):
        maze[x][y+1]=0
        y+=1
      for row in maze:
        print(row)
     # break
    
tracePath()

  
  
  
  
  
