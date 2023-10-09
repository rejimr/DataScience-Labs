# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:35:18 2023

@author: rejimr
"""
#printing Hello world
print('Hello World') 
for i in range(1,10):
    print(i) # printing values from 1 to 10 using for loop
    
 #Variables in Python
    total = 0
    for i in range(1,10):
        total = total+i
        print (total)
    print('Final toatal:',total)
    
#functions in python
    def say_hello_to(name):
        print('Hello '+name)
    
        say_hello_to("Cagatay")
        say_hello_to("Fred")  

#Conditionals in pytho
    value = 5
    if value > 0:
       print("This is positive!")
    elif(value < 0):
       print("This is negative!")
    else:
        print("This is 0, you can't fool me, I am clever piece of code")
        
#Comments in python
#please ignore me
#Data types in python
    x = 3 # unmbers
    a = "gorillas" #string
    t = True #boolean        

#Lists
    myFavouriteParks =[]
    myFavouriteParks.append("Victoria")
    myFavouriteParks.append("Hampstead Heath")
    myFavouriteParks.append("Richmomd")
    print(myFavouriteParks)
    print("----------------------------------------")
    for value in myFavouriteParks:
        print (value)
#Dictionaries
    foods ={}
    foods["banana"]= "yellow"
    foods["avocado"]= "green"
    foods
    foods["banana"]
    print("Now trying with a non existing key")
  # foods["cheese"]
  
    print("We need to load th epachage first")
    import numpy as np
    myArray = np.arange(10)
    print(myArray)
    
#Week-1 Lab
    # To print the records in csv file
    import csv # impots th ecsv module
    import sys # imports the sys module
    f = open('TB_burden_countries_2023-10-08.csv') # opens the csv file
    for row in csv.reader(f):
        print (row)
    f.close()
    
    #To print the number of rows in the csv file
    f = open('TB_burden_countries_2023-10-08.csv') # opens the csv file
    #next(f)
    count = 0
    for row in csv.reader(f):
        #print (row)
        count = count + 1   
    print("The number of lines ",count) # printing the number of lines exluding the header lines 
    f.close()
    
    #To find the average value of any numeric column
    
    f = open ('TB_burden_countries_2023-10-08.csv')
    next(f)
    average = 0
    sum = 0
    count = 0
    rowitem=0
    #try:
    for row in csv.reader(f):
            if row[8] is None :
                rowitem = 0
            if row[8]=='':
                rowitem = 0
            else:
                rowitem = row[8]
            #print(rowitem)
            count +=1
            sum = sum + float(rowitem)
            #print(count)
    average = sum /(count-1)
    print ('\nsum is :',sum, '\naverage is:' ,average,'\ncount is: ',count)
           
    #except:
        #print('invalid')
        #average = sum /count
        #print ('average is ',average)
        
        
        # Average for year 1990 and 2011
    f.close()
        
    f = open ('TB_burden_countries_2023-10-08.csv')
    next(f)
    average = 0
    sum = 0
    count = 0
    rowitem=0
    #try:
    for row in csv.reader(f):
            if (row[5] == '1991') or row[5]=='2011':
                rowitem = row[8]
                count += 1
                if rowitem=='':
                   rowitem=0
                sum = sum + float(rowitem)
    average = sum /(count-1)
    print ('\nsum is :',sum, '\naverage is:' ,average,'\ncount is: ',count)
        
        
        #NumPy Basics
        
        
    import numpy as np
    a = np.array([0,1,2,3])
    print(' a is ',a)
    
    # alternative methods
    a = np.arange(10)
    b = np.arange(1,9,2)
    c = np.linspace(0,1,6)
    d = np.linspace(0,1,5,endpoint = False)         
    e = np.diag(np.array([0,1,2,3,4,5]))
    
    #generate random points
    f = np.random.rand(4) # uniform in 0,1
    g = np.random.randn(4) # gaussian distribution
    print(' a',a,"\n b = ",b,"\n c = ",c,"\n d= ",d,"\n e= ",e,"\n f= ",f,"\n g= ",g)
    
    # checking the properties of arrays
    print ('\nProperties of arrays')
    print (a.ndim)
    print (a.shape) 
    
    #array of different forms and transitions between array forms:
    print('array of different forms and transition between array forms')    
    a = np.array([[0,1,2],[3,4,5]]) #2 x 3 array
    print('2x3 array\n', a)
    b = np.arange(10).reshape((5,2))  # 5x2 array
    print('5x2 array\n',b)
    print('Transpose of b\n',b.T)
    
    #You can store different types of data in numpy arrays:
    c = np.array([1, 2, 3], dtype=float)
    e = np.array([True, False, False, True])
    f = np.array(['Bonjour', 'Hello', 'Hallo', 'Terve', 'Hej'])
    print (c.dtype)
                
    #Numpy enables many basic operations to be done quickly and easily on arrays:
    a = np.array([1, 2, 3, 4])
    a + 1
    2**a
    b = np.ones(4) + 1
    a - b
    a * b
    a == b
    print('value of a and b is ',a,b)
    
    
    #visualisation with Matplotlib:
    import matplotlib.pyplot as plt # first import library

    x = np.linspace(0, 3, 20)
    y = np.linspace(0, 9, 20)
    plt.plot(x, y)       # line plot
    plt.plot(x, y, 'o')  # dot plot
    plt.show()           # shows the plot (not needed with Ipython/Spyder console)
    
    
    #Part 2 -DIY
    # Create an array ranging from 5 to 15
    arrayA=np.arange(5,15)
    print('\nPrint array raning from 5 to 15',arrayA)
    
    #Create an array containing 7 evenly spaced numbers between 0 and 23
    arrayB =  np.linspace(0,7,23)
    print('\nSeven Evently spaced numbers between 0 and 23\n',arrayB)
    
    #generate an artificial numpy array with values between -1 and 1 that follow a uniform data distribution.
    #arrayC = np.random.rand(4)
    arrayU = np.random.uniform(-1,1,6)
    print ('\nRandom array ArrayU ',arrayU)
    
    #Visualise the array in an histogram in matlab
    
    arrayU = np.random.uniform(-1,1,6) 
    count, bins, ignored = plt.hist(arrayU, 6 , density=True)
    plt.plot(bins, np.ones_like(bins),color='r')
    plt.title('Uniform Distribution')
    plt.show()
    #Create two random numpy arrays with 10 elements. Find the Euclidean distance between the arrays using arithmetic operators
    array1 = np.random.randint(1,20,10)
    print( array1)
    array2 = np.random.randint(1,50,10)
    print (array2)
    sumsqr = np.sum(np.square(array1-array2))
    ecldist= np.sqrt(sumsqr)
    print('Euclidean diatance is : ',ecldist)
    
    