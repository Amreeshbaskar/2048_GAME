import random
def print_mat():
    for i in range(4):
        for j in range(4):
            print(mat[i][j],end=" ")
        print()
    print()

def game_win():
    flag=0
    for i in range(4):
        for j in range(4):
            if(mat[i][j]==2048):
                flag=1
                break
    if(flag==1):
        return 0
    else:
        return 1
def check_move():
    move_available=0
    for i in range(4):
        for j in range(4):
            if(mat[i][j]==0):
                move_available=1
                break
    if(move_available==0):
        if(mat[0][0]==mat[0][1] or mat[0][0]==mat[1][0]):
            move_available=1
            
    if(move_available==0):
        if(mat[0][1]==mat[0][2] or mat[0][1]==mat[1][1]):
            move_available=1
            
    if(move_available==0):
        if(mat[0][2]==mat[0][3] or mat[0][2]==mat[1][2]):
            move_available=1
            
    if(move_available==0):
        if(mat[0][3]==mat[1][3]):
            move_available=1
            
    if(move_available==0):
        if(mat[1][0]==mat[1][1] or mat[1][0]==mat[2][0]):
            move_available=1
            
    if(move_available==0):
        if(mat[1][1]==mat[1][2] or mat[1][1]==mat[2][1]):
            move_available=1
            
    if(move_available==0):
        if(mat[1][2]==mat[1][3] or mat[1][2]==mat[2][2]):
            move_available=1
            
    if(move_available==0):
        if(mat[1][3]==mat[2][3]):
            move_available=1
            
    if(move_available==0):
        if(mat[2][0]==mat[2][1] or mat[2][0]==mat[3][0]):
            move_available=1
            
    if(move_available==0):
        if(mat[2][1]==mat[2][2] or mat[2][1]==mat[3][1]):
            move_available=1
    
    if(move_available==0):
        if(mat[2][2]==mat[2][3] or mat[2][2]==mat[3][2]):
            move_available=1

    if(move_available==0):
        if(mat[2][3]==mat[3][3]):
            move_available=1

    if(move_available==0):
        if(mat[3][0]==mat[3][1]):
            move_available=1
    
    if(move_available==0):
        if(mat[3][1]==mat[3][2]):
            move_available=1
            
    if(move_available==0):
        if(mat[3][2]==mat[3][3]):
            move_available=1
            
    if(move_available==1):
        return 1
    else:
        return 0
    
            
def right_move():
    move=0
    for z in range(4):
        for i in range(3,-1,-1):
            if(mat[z][i]!=0):
                for j in range(i-1,-1,-1):
                    
                    if(mat[z][i]==mat[z][j]):
                        mat[z][i]+=mat[z][i]
                        mat[z][j]=0
                        move=1
                        break
                    if(mat[z][j]!=0):
                        break
        for i in range(3,-1,-1):
            if(mat[z][i]==0):
                for j in range(i-1,-1,-1):
                    if(mat[z][j]!=0):
                        mat[z][i]=mat[z][j]
                        mat[z][j]=0
                        move=1
                        break
    return move

def left_move():
    move=0
    for z in range(4):
        for i in range(4):
            if(mat[z][i]!=0):
                for j in range(i+1,4):
                    if(mat[z][i]==mat[z][j]):
                        mat[z][i]+=mat[z][i]
                        mat[z][j]=0
                        move=1
                        break
                    if(mat[z][j]!=0):
                        break
        for i in range(4):
            if(mat[z][i]==0):
                for j in range(i+1,4):
                    if(mat[z][j]!=0):
                        mat[z][i]=mat[z][j]
                        mat[z][j]=0
                        move=1
                        break
    return move   

def transpose():
    mat1=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            mat1[i][j]=mat[j][i]
    return mat1

def up_move():
    global mat
    mat=transpose()
    move=0
    for z in range(4):
        for i in range(4):
            if(mat[z][i]!=0):
                for j in range(i+1,4):
                    if(mat[z][i]==mat[z][j]):
                        mat[z][i]+=mat[z][i]
                        mat[z][j]=0
                        move=1
                        break
                    if(mat[z][j]!=0):
                        break
        for i in range(4):
            if(mat[z][i]==0):
                for j in range(i+1,4):
                    if(mat[z][j]!=0):
                        mat[z][i]=mat[z][j]
                        mat[z][j]=0
                        move=1
                        break
    mat=transpose()
    return move   
    
    
    
def down_move():
    global mat
    mat=transpose()
    move=0
    for z in range(4):
        for i in range(3,-1,-1):
            if(mat[z][i]!=0):
                for j in range(i-1,-1,-1):
                    if(mat[z][i]==mat[z][j]):
                        mat[z][i]+=mat[z][i]
                        mat[z][j]=0
                        move=1
                        break
                    if(mat[z][j]!=0):
                        break
        for i in range(3,-1,-1):
            if(mat[z][i]==0):
                for j in range(i-1,-1,-1):
                    if(mat[z][j]!=0):
                        mat[z][i]=mat[z][j]
                        mat[z][j]=0
                        move=1
                        break
    mat=transpose()
    return move 

#def up_move():
#def down_move():

                    
def add_tiles():
    choice_list=[]
    pos=0
    for i in range(4):
        for j in range(4):
            if(mat[i][j]==0):
                choice_list.append(pos)
            pos+=1
    a=random.choice(choice_list)
    #print(a)
    #print(choice_list)
    choice_list=[2,4]
    pos=0
    for i in range(4):
        for j in range(4):
            if(a==pos):
                mat[i][j]=random.choice(choice_list)
            pos+=1
    

def start_game():
    while(game_win() and check_move()):
        move=0
        while(move==0):
            print("Enter direction to move : ",end="")
            direction=input()
            if(direction=='r'):
                move=right_move()
            if(direction=='l'):
                move=left_move()
            if(direction=='d'):
                move=down_move()
            if(direction=='u'):
                move=up_move()
        add_tiles()
        print_mat()
        
        #flag=int(input("Enter 1 to continue the game : "))
        
        
        
    
    
mat=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
choice_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a=random.choice(choice_list)
choice_list.remove(a)
b=random.choice(choice_list)
choice_list=[2,4]
pos=0

for i in range(4):
    for j in range(4):
        #print(pos)
        if(pos==a):
            mat[i][j]=random.choice(choice_list)
        if(pos==b):
            mat[i][j]=random.choice(choice_list)
        pos+=1
print("Start the Game")
print()
print('R->Right')
print('L->Left')
print('U->Up')
print('D->Down')
print()
print_mat()
start_game()
if(!game_win()):
    print("You won the Game!")
else:
    print("Oops! You lose the game")