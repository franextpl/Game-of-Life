import time
import os


#zmienne programu
plane= []

plane2=[]

ster1=0
ster2=0

num1=0
num2=0
error_counter = 0

stop_input_faze=False


#zmienne środowiskowe
debug=False




for i in range(10):
    plane.append([0,0,0,0,0,0,0,0,0,0])
    plane2.append([0,0,0,0,0,0,0,0,0,0])

#funkcja manualnego zmiany stanu pola
def change(x,y):
    x=int(x)
    y=int(y)
    notnow=0
    if (plane[y])[x]==0:
        (plane[y])[x]=1
        notnow+=1
    if (plane[y])[x]==1 and notnow==0:
        (plane[y])[x]=0

def check_for_live_neighbours(x,y):
    x=int(x)
    y=int(y)
    liveneighbour=0
    global error_counter
    global plane

    try:
        if (plane[y])[x-1]==1:
            liveneighbour+=1
            if debug == True:
                print('lewo')
    except:
        error_counter+=1

    try:    
        if (plane[y])[x+1]==1:
            liveneighbour+=1
            if debug == True:
                print('prawo')
    except:
        error_counter+=1 

    try:               
        if (plane[y+1])[x]==1:
            liveneighbour+=1
            if debug == True:
                print('dol')
    except:
        error_counter+=1

    try:
        if (plane[y-1])[x]==1:
            liveneighbour+=1
            if debug == True:
                print('gora')
    except:
        error_counter+=1

    try:
        if (plane[y+1])[x+1]==1:
            liveneighbour+=1
            if debug == True:
                print('dolprawo')
    except:
        error_counter+=1

    try:                    
        if (plane[y-1])[x+1]==1:
            liveneighbour+=1
            if debug == True:
                print('goraprawo')
    except:
        error_counter+=1

    try:
        if (plane[y+1])[x-1]==1:
            liveneighbour+=1
            if debug == True:
                print('dollewo')
    except:
        error_counter+=1

    try:
        if (plane[y-1])[x-1]==1:
            liveneighbour+=1
            if debug == True:
                print('goralewo')
    except:
        error_counter+=1
    return(liveneighbour)

    #skrypt sterujący

while True:  
    what_to_do=input('what next?:')
    if what_to_do == 'start':
        break
    elif what_to_do == 'add':
        change((input('x value:')),( input('y value:')))

    elif what_to_do == 'clear':
        num1=0
        num2=0
        while num1 < len(plane):

            while num2 < len(plane[0]):

                try:
                    (plane[num1])[num2]=0
                except:
                    error_counter+=1
                num2+=1
            num2=0
            num1+=1
        print('cleared the page')


    elif what_to_do == 'disp':
        for i in plane:
            print(i)  
    elif what_to_do == 'help':
        print('start for running the simulation, add for adding a point, disp for displaying the current state of the board, clear for setting the board all zeros, verb for verbose mode')
    elif what_to_do == 'verb':
        debug=True
        print('enabled debug mode')
    else:
        print("no such command")    
    

    
num1=0
num2=0
while num1 < len(plane):

    while num2 < len(plane[0]):

        try:
            (plane2[num1])[num2]=(plane[num1])[num2]
        except:
            error_counter+=1  
        num2+=1
    num2=0
    num1+=1  
        



#skrypt uruchomionej gry

for i in range (200):
    os.system('cls')
    #wyświetlenie planszy i czekanie
    for i in plane:
        for o in i:
            if o==0:
                print('0',end=' ')
            else:
                print('#',end=' ')
        print()
    time.sleep(1)

    num1=0
    num2=0
    while num1 < len(plane):

        while num2 < len(plane[0]):

            try:
                (plane[num1])[num2]=(plane2[num1])[num2]
            except:
                error_counter+=1  
            num2+=1
        num2=0
        num1+=1  


    while ster1 < len(plane):
        while ster2 < len((plane[0])):
            if debug == True:
                print("koordynaty: x"+str(ster2)+",  y" + str(ster1))
            


            if (plane[ster1])[ster2]==0:
                if debug == True:
                    print(check_for_live_neighbours(ster2,ster1))

                if  check_for_live_neighbours(ster2,ster1)==3:
                    (plane2[ster1])[ster2]=1
                    if debug == True:
                        print('zmieniono')
                    alredy_evd=True
            
            if (plane[ster1])[ster2]==1:
                if debug == True:
                    print(check_for_live_neighbours(ster2,ster1))
                if  check_for_live_neighbours(ster2,ster1)<2 or check_for_live_neighbours(ster2,ster1)>3:
                    (plane2[ster1])[ster2]=0
                    if debug == True:
                        print('zmieniono')
            
                    
            ster2+=1
        ster1+=1
        ster2=0
    ster1=0
    ster2=0



    

