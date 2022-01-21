## Python program for Dijkstra Allgorithum for adjencencey matrix:
## 
import math
import numpy as np

def Dijkstra(graph , root , City , b):   
    bucket = []
    Priority_Q = [] 
    Parent = {}
    Parent[root] = ''
    bucket.append(root)
    Distance = {}                          # Dictionary to store Distance of each node.
    for city in Cities:                    # Initialize Distance of root == 0 , others infinity.
        if city == root:                           
            Distance[root] = 0
        else:
            Distance[city] = np.Infinity          
    Priority_Q.extend(graph[root])         # Add root values in the Queue.
    temp0 = []
    for i in Priority_Q:
        for h in (i):
            temp0.append(h)
                                          # Helping function. 
    def Space_Intervl(City):              # To find direct Distance b/w two cities.
        checker = False 
        for i in range(0 , len(temp0) , 2):
            if temp0[i] == City:
                checker = True
                return (temp0[i + 1])
        if checker == False:
            return None
        
    if Space_Intervl(City) != None:
        Data_Save = Space_Intervl(City)
        
    while len(Priority_Q) != 0:
        temp = []                             # Use temparery list to find minimum distance
                                              # city from root in Priority Queue.
        for i in Priority_Q:                  # As Priority Queue contains tuple first divideing its tuple in:
            for v in (i):                     # 1:Cities and 2:Waits.
                temp.append(v)                # Now 'temp' contains cities and weights in sequence. 
    
        minimum_Distance = np.Infinity        # Finding Minimum Distance.
        for l in range(1 , len(temp) , 2):
            if temp[l] < minimum_Distance:
                minimum_Distance = temp[l]
                F = l                         # F is the index of minimum distance.
            if  Distance[temp[l-1]] == Distance[root]:              # If two cities have same minimum distance.
                Distance[temp[l-1]] == Distance[root]
            else:                     
                Distance[temp[l-1]] = Distance[root] + temp[l]      # Updating Distance in from infinity. 
        Parent[temp[F-1]] = root
        Q = Distance[root] + temp[F]          # Compare previous value of Distance with new one and select least one. 
        if Distance[temp[F-1]] > Q :          
            Distance[temp[F-1]] = Q
        bucket.append(temp[F-1])
        Priority_Q.pop(math.floor(F/2))       # Delete tuple from Queue. 
        root = temp[F-1]
        Found = False
        
        if b==2:
            Data_Save = None
            if Space_Intervl(City) != None:       
                Data_Save = Space_Intervl(City) # for single city tour. 
            if  temp[F-1] == City:
                Found   = True
                print(" ")
                print("DIRECT ROUTE WEIGHTS: " , Data_Save )
                print("LONG DISTANCE CITIES TOUR TRIP: " , Distance[Parent[City]])
                if Distance[Parent[City]] > Data_Save:
                    print("DIRECT DISTANCE BETWEEN TWO CITIES" , Data_Save , "IS LESSER THAN\
                                                                    IT'S CITIES TOUR TRIP.")
                    print("IF YOU WANT LESS COSTLY TOUR SELECT DIRECT ROUTE OTHERWISE LONG\
                                                DISTANCE TRIP FOR MORE TRAVELLING ENJOYMENT.") 
                    Q = input("IF YOU WANT SHORTEST ROUTE ENTER 's' AND IF LONGEST PATH ENTER\
                                                                                    'l'. \n")
                    if Q == "s":
                        print("IT TAKES" , float(Data_Save/10) , "HOUR's")
                        print("FARE = " , Data_Save*110 , "Rs")
                    elif Q == "l":
                        print("IT TAKES" , float(Distance[Parent[City]]/10) , "HOUR's")
                        print("FARE = " , Distance[Parent[City]]*110 , "Rs")
                    else:
                        print("PLEASE! ENTER CORRECT REPRESENTATION.")

                    break
                else:
                    print("DISTANCE BETWEEN TWO CITIES IS SMALLER THAN DIRECT ROUTE IF WE\
                                                        FOLLOW TOUR OF FOLLOWING CITIES ")
                    for i in bucket:
                        print(i , "=>" , end = "     ")
                print(" ")
    if b==1:
        print("                       'THIS WOULD BE THE BEST ROUTE FROM YOUR LOCATION\
                                                                FOR A 'WORLD TOUR' :) ")
        print(" ")
        for i in bucket:
            print(i , "=>" , end = "      ")
    if b==2:
        if Found == False:
            print("SORRY!")
            print("       'YOUR ENTERED CITY CANNOT BE ENTERTAINED BY OUR TRAVELLING SERVICES.'")
    if b==3:
        if Data_Save == None:
            print("SORRY!")
            print("       'YOUR ENTERED CITY CANNOT BE ENTERTAINED BY OUR TRAVELLING SERVICES.'")
        else: 
            print("THESE TWO CITIES HAS DIRECT ROUTE THAT IS", Data_Save,"km\n")
            print(" ")
    q = False
    if b ==4:
        for i in Cities:
            if i == City:
                q = True
        if q != True:
            print("SORRY!")
            print("       'YOUR ENTERED CITY CANNOT BE ENTERTAINED BY OUR TRAVELLING SERVICES.'")
        else:
            print("TWO CITIES CONNECTION's WEIGHT IS ",Distance[Parent[City]],"IN PARTICULAR WAY\
                                                        WHILE CROSSING THESE CITIES IN THE WAY:")
            for i in bucket:
                if i == City:
                    break
                print(i , "=>" , end = "     ")

######################STEP1##########################
# Convert Distance Data into list than 2D array using numpy: 
Matrix = np.zeros((30 , 30)) 
Daw = []
with open("Ddata.txt", "r+") as file:
    for line in file:
        for word in line.split():
            Daw.append(word)
            
for i in range(30):
    for j in range(30):
        if i == 0:
            Matrix[i][j] = Daw[j]
        else:
            k = ((i)*30) + j
            Matrix[i][j] = Daw[k] # Now, our matrix is a 2D array.
#####################STEP2############################
# Read the Cities Data.
Cities = []
with open("Citydata.txt", "r") as file:
    for line in file:
        for word in line.split():
            Cities.append(word)
####################STEP3############################
# Make Graph(Dictionry) with Keys as City Names and values is equal to pair (Related-Cities , Weights). 
City_weights = []
for i in range(30):
    Waits = []
    for j in range(30):
        if Matrix[i][j] != 0:       # Not including cities with zero wait or no edge. 
            N = Cities[j] , Matrix[i][j]
            Waits.append(N)
    City_weights.append(Waits)        
graph = dict(zip(Cities , City_weights))  # Zip will convert two lists in a dictionary.  
##################STEP4###############################
root = input("ENTER YOUR CURRENT OR NEARER LOCATIN FROM FOLLOWING CITIES FOR BETTER EXPERIENCE:\n")
MENU = "H"
while MENU != "Stop":
    print(" ")
    MENU = input("IF YOU WANT RECOMMENDATIONS ABOUT\n\
        WORLD TOUR ENTER A:\n\
        FARE AND DISTANCE BETWEEN TWO CITIES ENTER B:\n\
        DIRECT DISTANCE BETWEEN TWO CITIES ENTER C:\n\
        DISTANCE BETWEEN TWO CITIES IN A PARTICULAR ROUTE ENTER D:\n\
        IF YOU WANT TO STOP ENTER Stop.\n")
#****************************************WORLD-TOUR-ALGORITHUM*************************
    if MENU == "A":
        myBucket  = Dijkstra(graph , root , None , 1) 
#****************************SPACE-INTERVAL-ALGORITHUM*********************************
#************SHORTEST-DISTANCE.
#************LONGEST-DISTANCE.
    elif MENU == "B":
        City1 = input("ENTER YOUR DESTINATION'S NAME: \n")
        space_interval = Dijkstra(graph , root , City1 , 2)
# #*************************OTHER-PATH-THEN-DIRECT-ROUTE*******************************
    elif MENU == "C":
        City2 = input("ENTER YOUR DESTINATION'S NAME: \n")
        E = Dijkstra(graph , root , City2 , 3)
        print(" ")
    elif MENU == "D":
        City = input("ENTER YOUR DESTINATION'S NAME: \n")
        c = Dijkstra(graph , root , City , 4)       
        print(" ")