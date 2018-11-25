# Matrices
## Python code to create and operate on matrices:

   ### -matrices.py contains Matrix class and FMatrix, CMatrix and Identity sub-classes
  
   ### -exampleMatrices.py contains example matrices
-------------- 
Some examples:
--------------
#### Create matrice filled with random integers 
A=Matrix(4) #Creates a 4x4 matrix filled with random integers from the default range which is [-125,125]
B=Matrix([3,5],inRange=[10,25]) #Creates a 3x5 matrix with elements ranged between 10 and 25

----------------------------------------
#### Give list of numbers to create matrices
filled_rows=[[1,2,3],[4,5,6],[7,8,9]]

C=Matrix(listed=filled_rows) #Creates a matrix with the given list of numbers

----------------------------------------
#### Give a string filled with data and use the numbers in it to create a matrix (Integers only for now)

##### This example data is from a csv file, directly copied and pasted into a string format  

data="""1,K,60,69900,6325
2,K,30,79000,5200
3,E,52,85500,7825
4,E,57,17100,8375
5,E,55,5500,5450
6,E,68,27200,8550
7,E,41,20500,4500
8,E,20,69000,5050
9,K,33,13200,8325
10,E,37,31800,5975"""

D=Matrix(dim=[10,4],listed=data) #Creates a matrix form of the given string's *integers*, dimension is *required* as [dataAmount,features]

----------------------------------------
#### Create matrices filled with random float numbers

E=FMatrix(6) #Create a matrix filled with random float values in the default range
F=FMatrix(dim=[2,5],randomFill=0) #Fill the matrix with zeros

----------------------------------------
#### Create identity matrices

i=Identity(3) #3x3 identity matrix
i.addDim(2) #Add 2 dimensions to get a 5x5 identity matrix

----------------------------------------
#### Get properties of your matrix

C.dim #Returns the dimension of the matrix

C.grid #Prints the matrix's elements as a grid

C.string #Returns the string for of the matrix's elements

C.avg #Returns the overall average of the elements

C.det #Returns the determinant of the matrix

C.t #Returns the transposed matrix

C.minor(1,1) #Returns the 1st row's 1st element's minor matrix

C.adj #Returns the adjoint matrix

C.inv #Returns the inversed matrix

C.copy #Returns a copy of the matrix

C.summary #Returns the string form of the object 

----------------------------------------

### More examples can be found in exampleMatrices.py
