# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:38:28 2018

@author: Semih
"""
from MatricesM.matrices import Matrix,FMatrix,Identity,CMatrix

# =============================================================================
"""Example Inputs"""      
# =============================================================================
projectGrid="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

# =============================================================================
# Valid Matrices
# =============================================================================
o=Matrix(8,randomFill=0)
b=Matrix(1)
c=Matrix(dim=[2,4],ranged=[-50,50])
d=FMatrix([4,3])
e=Matrix(8,randomFill=0)
f=FMatrix(dim=6,ranged=[-1250,1250])
g=Matrix(dim=[3,6],ranged=[2,10])
p=Matrix(5,ranged=[0,100])
q=FMatrix(4)
q1=FMatrix(9,decimal=2)
q2=FMatrix(6,decimal=6)
y=Matrix(3,listed=[3,5,7,8,3,4,5,2,5])
c1=CMatrix(5)
c2=CMatrix([7,3],ranged=[-10,10])
# =============================================================================
# String inputs Matrices
# =============================================================================
proj=Matrix(20,listed=projectGrid)
validStr1=Matrix(dim=[2,3],listed=" 34-52\n33a c9d88 hello\n--3-")
validStr2=Matrix(listed="312as45\ndid12,,,44\ncc352as45\ndid12,,,44\ncc3-5")
validStr3=Matrix(listed="\n\n\ndd34 5\n\n44\nn659")
validStr4=Matrix(dim=[22,3],listed="""ulke,boy,kilo,yas,cinsiyet
tr,130,30,10,e
tr,125,36,11,e
tr,135,34,10,k
tr,133,30,9,k
tr,129,38,12,e
tr,180,90,30,e
tr,190,80,25,e
tr,175,90,35,e
tr,177,60,22,k
us,185,105,33,e
us,165,55,27,k
us,155,50,44,k
us,160,58,39,k
us,162,59,41,k
us,167,62,55,k
fr,174,70,47,e
fr,193,90,23,e
fr,187,80,27,e
fr,183,88,28,e
fr,159,40,29,k
fr,164,66,32,k
fr,166,56,42,k
""",features=["Height","Weight","Age"])

# =============================================================================
# InvalidMatrices
# =============================================================================
#You have to give the matrix a valid dimension, or a list to get a dimension, or it won't be a valid matrix

#a=Matrix(0)
#v=Matrix()
#k=Matrix(dim=-1)
#l=Matrix(ranged=[0])
#m=Matrix(randomFill=1)

# =============================================================================
# Identity Matrices
# =============================================================================
id1=Identity()
id2=Identity(5)
id3=id2.subM(3,3)
id4=Identity(6)

# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving dimensions")
l=[proj,o,b,c,d,e,f,g,p,q,q1,q2,y,c1,c2]
for matrix in l:
    print(matrix)
print('################################')     
# =============================================================================
"""PRINT THE IDENTITY MATRICES """
# =============================================================================
print('################################') 
print("Identity matrices")
for i in [id1,id2,id3,id4]:
    print(i)
print('################################')     
# =============================================================================
"""PROPERTIES, METHODS CALLS"""   
# =============================================================================
print('################################')  
print("Attribute call outputs\n")
print('################\n')
      
print("d:")
print(d)
print("d.matrix:\n")
print(d.matrix)

print('\n################\n')
      
print("f.subM(1,4,2,3):\n",f.subM(1,4,2,3),"\n")
print(f)
print("f.delDim(4)")
print(f)
print("f.uptri.p")
f.uptri.p
print("f.lowtri.p")
f.lowtri.p
print("f-(f.lowtri@f.uptri)")
print(f-(f.lowtri@f.uptri))
print('################')
      
print("g.dim:\n",g.dim)
print("g.ranged():\n",g.ranged())
print("g:",g)      
print("g.remove(3):")
g.remove(3)
print(g)

print('################')
print("q1.decimal",q1.decimal)
q1.p
print("q1.decimal=5")
q1.decimal=5
q1.p
print('################')      
h=proj.subM(12,18,5,11)
print("h=proj.subM(12,18,5,11):\n",h)
print("h.mean():",h.mean())
print("\nh.det:",h.det)
print("\nh.rank:",h.rank)
print("\nh.rrechelon:",h.rrechelon)
print("\nh.inv:")
print(h.inv)
print("h.minor(3,4):\n",h.minor(3,4),"\n")

print('################')
      
j=g.subM(1,2,1,4)
print("j=g.sub(1,2,1,4):\n",j,"\n")
print("j.summary:\n",j.summary)

print('\n################')
      
print("proj=proj.subM(5,15).copy:\n")
proj=proj.subM(5,15).copy
print(proj)

print('################')
      
print("p:",p)
print("p.det:\n",p.det)
print("\np.adj:\n",p.adj)
print("p.inv:\n")
print(p.inv)

print('################')
      
print("p:")
print(p)
print("p.remove(c=1) and p.remove(r=2)")
p.remove(c=1)
p.remove(r=2)
print(p)
print("p.add(col=2,lis=[55,55,55,55,55]):")
p.add(col=2,lis=[55,55,55,55])
print(p)
print("p.sdev()")
print(p.sdev())

print('################\n')

print("proj.find(40)")
print(proj.find(40))
print("\nproj.find(40,0)")
print(proj.find(40,0))
print("\nproj.find(111)")
proj.find(111)

print("################\n")
      
print("id2:\n",id2)
print("\nid2.addDim(2):",id2.addDim(2))
print("id2.matrix:\n",id2.matrix)

print('################')
      
print("id3:\n")
print(id3)

print('################')
      
print("id4:\n")
print(id4)
print("\nid4.delDim(6):\n")
print(id4.delDim(6))

print('################')
      
print("id4:",id4)
print("\nid4.addDim(10)):\n",id4.addDim(10))

print("################")
print("r=p.t")
r=p.t
print("r.remove(r=2):")
r.remove(r=2)
print(r)
print("r.rank:",r.rank)
print("\nr[0]=r[1][:]")
r[0]=r[1][:]
print(r)
print("r.rank:",r.rank)    

      
# =============================================================================
"""OPERATIONS ON ELEMENTS"""    
# =============================================================================

print("################################")   
print("Operator examples")
print("################")
      
print("\nc.dim=",c.dim," d.dim:",d.dim)
print("\nmMulti=c@d:")
mMulti=c@d
print(mMulti)
print("\n((((mMulti)+125)**3)%2):")
print(((((mMulti)+125)**3)%2))

print("################\n")
      
print("f:\n",f)
print("f1=f.intForm")
f1=f.intForm
print(f1)
print("f2=f.roundForm(3)")
f2=f.roundForm(2)
print(f2)
print("f2-f1")
f3=f2-f1
print(f3)

print("################")
      
print("e+=Identity(e.dim[0])*99")
e+=Identity(e.dim[0])*99
print(e)
print("\ne-=33:")
e-=33
print(e)
print("\ne+=FMatrix(e.dim):")
e+=FMatrix(e.dim)
print(e)
print("\ne*=[2,1,1,0.5,0.2,0.0003,1,3]:")
e*=[2,1,1,0.5,0.2,0.0003,1,3]
print(e)
print("e%=[2,2,2,2,1,1,1,1]")
e%=[5,5,5,5,3,3,1,1]
print(e)

print("################")
      
print("\nc%j")
print(c%j)

print("\n(f.lowtri@f.uptri).roundForm(4)==f.roundForm(4)")
print((f.lowtri@f.uptri).roundForm(4)==f.roundForm(4))
# =============================================================================
""" STRING MATRICES' OUTPUTS"""
# =============================================================================
print("\n################################")
print("Strings' matrices:")
print("################\n")
      
for numb,strings in enumerate([validStr1,validStr2,validStr3,validStr4]):
    print("validStr"+str(numb+1)+":")
    print(strings)         
    print('################')
print("")
# =============================================================================
"""Basic statistical properties"""
# =============================================================================
print("validStr4.ranged()")
print(validStr4.ranged())
print("")

print("validStr4.mean()")
print(validStr4.mean())
print("")

print("validStr4.sdev()")
print(validStr4.sdev())
print("")

print("validStr4.median()")
print(validStr4.median())
print("")

print("validStr4.freq()")
print(validStr4.freq())
print("")

print("validStr4.mode()")
print(validStr4.mode())
print("")

print("validStr4.iqr()")
print(validStr4.iqr())
print("")

print("validStr4.iqr(as_quartiles=True)")
print(validStr4.iqr(as_quartiles=True))
print("")

print("validStr4.variance()")
print(validStr4.variance())
print("")

print('################')
print("Linear model for validStr4:")
print("""
validStr4.corr().p #First and second columns have strong positive correlation. Let's choose first column to be predicted

var=validStr4.subM(1,validStr4.dim[0],2,2)
var.add("bias",[1]*validStr4.dim[0],col=1)

out=validStr4.subM(1,validStr4.dim[0],1,1)

coefs=(((var.t@var).inv)@var.t)@out

preds=var@coefs
err=out-preds
""")
validStr4.corr().p

var=validStr4.subM(1,validStr4.dim[0],2,2)
var.add("bias",[1]*validStr4.dim[0],col=1)

out=validStr4.subM(1,validStr4.dim[0],1,1)

coefs=(((var.t@var).inv)@var.t)@out

preds=var@coefs
err=out-preds
print("Height={0} + {1}*{2}".format(coefs[0][0],coefs[1][0],validStr4.features[1]))
print("\nAverage error:",err.mean(1)["Col 1"])
# =============================================================================
""" Expected Outputs """
# =============================================================================
"""
################################
Matrices created by giving dimensions

Square matrix
Dimension: 20x20
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10', 'Col 11', 'Col 12', 'Col 13', 'Col 14', 'Col 15', 'Col 16', 'Col 17', 'Col 18', 'Col 19', 'Col 20']

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 12 50 77 91  8 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48  4 56 62  0 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30  3 49 13 36 65 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 71 37  2 36 91 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 
24 47 32 60 99  3 45  2 44 75 33 53 78 36 84 20 35 17 12 50 
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 
67 26 20 68  2 62 12 20 95 63 94 39 63  8 40 91 66 49 94 21 
24 55 58  5 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 
21 36 23  9 75  0 76 44 20 45 35 14  0 61 33 97 34 31 33 95 
78 17 53 28 22 75 31 67 15 94  3 80  4 62 16 14  9 53 56 92 
16 39  5 42 96 35 31 47 55 58 88 24  0 17 54 24 36 29 85 57 
86 56  0 48 35 71 89  7  5 44 44 37 44 60 21 58 51 54 17 58 
19 80 81 68  5 94 47 69 28 73 92 13 86 52 17 77  4 89 55 40 
 4 52  8 83 97 35 99 16  7 97 57 32 16 26 26 79 33 27 98 66 
88 36 68 87 57 62 20 72  3 46 33 67 46 55 12 32 63 93 53 69 
 4 42 16 73 38 25 39 11 24 94 72 18  8 46 29 32 40 62 76 36 
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74  4 36 16 
20 73 35 29 78 31 90  1 74 31 49 71 48 86 81 16 23 57  5 54 
 1 70 54 71 83 51 54 69 16 92 33 48 61 43 52  1 89 19 67 48 


Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Square matrix
Dimension: 1x1
Features: ['Col 1']

0 


Dimension: 2x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

 27 -14 -16 -18 
  1 -22  11 -35 


Float Matrix
Dimension: 4x3
Features: ['Col 1', 'Col 2', 'Col 3']

0.9133 0.6953 0.2260 
0.2893 0.1291 0.2030 
0.7909 0.1419 0.4390 
0.5836 0.6225 0.7174 


Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  929.1768   406.8270   538.5267  -530.0911  -474.3029   -41.7780 
 -118.8649   133.0728   866.0093  -300.1095  1051.6778  -915.7099 
 -958.0214   421.0756  1057.2273  1036.3870 -1040.2774   818.2078 
  436.4906   425.1540   431.9700  1150.8095  -966.0850   161.8615 
 -610.5025   311.1176   307.3141  -557.5741   -12.7051  -302.0376 
  720.4246   553.8861  1114.9347    46.1970  -961.3555    98.3581 


Dimension: 3x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

6 8 6 1 9 9 
2 5 1 5 8 7 
9 6 9 9 4 7 


Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

50  2 37 54 62 
20 57  8 18 45 
 0 27 63 57 37 
 9 32 65 68 72 
63 94 54 38 49 


Float Matrix
Square matrix
Dimension: 4x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

0.4650 0.6656 0.1387 0.0410 
0.7379 0.8679 0.5744 0.9325 
0.2866 0.6744 0.3147 0.6569 
0.2245 0.7037 0.4770 0.0185 


Float Matrix
Square matrix
Dimension: 9x9
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9']

0.47 0.56 0.95 0.54 0.31 0.96 0.26 0.89 0.72 
0.59 0.25 0.94 0.47 0.30 0.51 0.13 0.34 0.95 
0.55 0.42 0.75 0.60 0.18 0.64 0.94 0.97 0.94 
0.41 0.32 0.30 0.97 0.13 0.84 0.72 0.74 0.64 
0.43 0.36 0.77 0.62 0.00 0.96 0.15 0.35 0.04 
0.45 0.48 0.09 0.58 0.60 0.96 0.57 0.60 0.33 
0.71 0.91 0.95 0.55 0.51 0.65 0.74 0.30 0.11 
0.07 0.20 0.47 0.90 0.68 0.72 0.15 0.31 0.27 
0.70 0.39 0.28 0.53 0.62 0.39 0.07 0.77 0.70 


Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

0.296906 0.692452 0.331592 0.427348 0.544634 0.923903 
0.808821 0.557066 0.593266 0.827196 0.184442 0.576556 
0.883512 0.530791 0.075573 0.900557 0.920487 0.629482 
0.942062 0.510508 0.973096 0.663279 0.260068 0.057897 
0.175938 0.563483 0.825912 0.497389 0.014856 0.160114 
0.871888 0.891952 0.145956 0.149158 0.484102 0.918801 


Square matrix
Dimension: 3x3
Features: ['Col 1', 'Col 2', 'Col 3']

3 5 7 
8 3 4 
5 2 5 


Complex Matrix
Square matrix
Dimension: 5x5

 0.2942+0.1047j   0.3952+0.3834j   0.5861+0.8795j   0.5164+0.1468j   0.3728+0.5658j  
 0.7693+0.1029j   0.7389+0.9766j   0.0323+0.7148j   0.2096+0.9777j    0.8443+0.926j  
  0.785+0.7261j   0.1035+0.6769j   0.6618+0.2616j   0.6909+0.9058j    0.976+0.2629j  
 0.0457+0.0824j   0.6037+0.5484j   0.4229+0.6988j   0.2719+0.7869j   0.7627+0.2611j  
 0.1359+0.2119j   0.7192+0.8858j   0.5932+0.0279j   0.4788+0.7318j   0.5137+0.5312j  


Complex Matrix
Dimension: 7x3

 -6.8035+4.5885j   -2.7705+0.5119j    4.6181-4.0714j  
  7.9279-6.8752j   -8.1467+0.1259j    6.4454+0.2045j  
 -4.5879+0.7444j    2.4068+4.6147j    6.1166-4.7027j  
  8.4221+0.5901j    9.3498+8.0055j   -3.4893-8.6782j  
  7.8864-5.7452j   -1.7462-5.2976j   -1.6031+5.4556j  
 -5.6535+8.6739j   -0.9739-2.7566j   -3.6957+5.5612j  
  6.6509-9.2533j   -0.4714+5.8167j    5.2516-8.7339j  

################################
################################
Identity matrices

Identity Matrix
Dimension: 1x1

 1 


Identity Matrix
Dimension: 5x5

 1  0  0  0  0 
 0  1  0  0  0 
 0  0  1  0  0 
 0  0  0  1  0 
 0  0  0  0  1 


Identity Matrix
Dimension: 3x3

 1  0  0 
 0  1  0 
 0  0  1 


Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 

################################
################################
Attribute call outputs

################

d:

Float Matrix
Dimension: 4x3
Features: ['Col 1', 'Col 2', 'Col 3']

0.9133 0.6953 0.2260 
0.2893 0.1291 0.2030 
0.7909 0.1419 0.4390 
0.5836 0.6225 0.7174 

d.matrix:

[[0.9133283333220504, 0.6953264809045525, 0.22598844443804444], [0.28931592090512837, 0.12905562832948458, 0.20298455878114408], [0.7909014410172631, 0.14190421077897486, 0.43898033637063116], [0.583585062992855, 0.6225124370114479, 0.7173884106759288]]

################

f.subM(1,4,2,3):
 
Float Matrix
Dimension: 4x2
Features: ['Col 2', 'Col 3']

 406.8270  538.5267 
 133.0728  866.0093 
 421.0756 1057.2273 
 425.1540  431.9700 
 


Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  929.1768   406.8270   538.5267  -530.0911  -474.3029   -41.7780 
 -118.8649   133.0728   866.0093  -300.1095  1051.6778  -915.7099 
 -958.0214   421.0756  1057.2273  1036.3870 -1040.2774   818.2078 
  436.4906   425.1540   431.9700  1150.8095  -966.0850   161.8615 
 -610.5025   311.1176   307.3141  -557.5741   -12.7051  -302.0376 
  720.4246   553.8861  1114.9347    46.1970  -961.3555    98.3581 

f.delDim(4)

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  929.1768   406.8270   538.5267  -530.0911  -474.3029   -41.7780 
 -118.8649   133.0728   866.0093  -300.1095  1051.6778  -915.7099 
 -958.0214   421.0756  1057.2273  1036.3870 -1040.2774   818.2078 
  436.4906   425.1540   431.9700  1150.8095  -966.0850   161.8615 
 -610.5025   311.1176   307.3141  -557.5741   -12.7051  -302.0376 
  720.4246   553.8861  1114.9347    46.1970  -961.3555    98.3581 

f.uptri.p

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  929.1768   406.8270   538.5267  -530.0911  -474.3029   -41.7780 
    0.0000   185.1161   934.9003  -367.9213   991.0027  -921.0543 
    0.0000     0.0000 -2632.5038  2160.4110 -6029.0159  4957.2396 
    0.0000     0.0000     0.0000  1041.8552   300.9002  -542.7699 
    0.0000     0.0000     0.0000     0.0000  2220.4756 -2546.7208 
    0.0000     0.0000     0.0000     0.0000     0.0000  -353.0673 

f.lowtri.p

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

 1.0000  0.0000  0.0000  0.0000  0.0000  0.0000 
-0.1279  1.0000  0.0000  0.0000  0.0000  0.0000 
-1.0310  4.5406  1.0000  0.0000  0.0000  0.0000 
 0.4698  1.2643  0.3810  1.0000  0.0000  0.0000 
-0.6570  3.1246  0.8585 -1.5463  1.0000  0.0000 
 0.7753  1.2882  0.1926  0.4944 -0.3864  1.0000 

f-(f.lowtri@f.uptri)

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 

################
g.dim:
 [3, 6]
g.ranged():
 {'Col 1': [2, 9], 'Col 2': [5, 8], 'Col 3': [1, 9], 'Col 4': [1, 9], 'Col 5': [4, 9], 'Col 6': [7, 9]}
g: 
Dimension: 3x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

6 8 6 1 9 9 
2 5 1 5 8 7 
9 6 9 9 4 7 

g.remove(3):

Dimension: 2x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

6 8 6 1 9 9 
2 5 1 5 8 7 

################
q1.decimal 2

Float Matrix
Square matrix
Dimension: 9x9
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9']

0.47 0.56 0.95 0.54 0.31 0.96 0.26 0.89 0.72 
0.59 0.25 0.94 0.47 0.30 0.51 0.13 0.34 0.95 
0.55 0.42 0.75 0.60 0.18 0.64 0.94 0.97 0.94 
0.41 0.32 0.30 0.97 0.13 0.84 0.72 0.74 0.64 
0.43 0.36 0.77 0.62 0.00 0.96 0.15 0.35 0.04 
0.45 0.48 0.09 0.58 0.60 0.96 0.57 0.60 0.33 
0.71 0.91 0.95 0.55 0.51 0.65 0.74 0.30 0.11 
0.07 0.20 0.47 0.90 0.68 0.72 0.15 0.31 0.27 
0.70 0.39 0.28 0.53 0.62 0.39 0.07 0.77 0.70 

q1.decimal=5

Float Matrix
Square matrix
Dimension: 9x9
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9']

0.46999 0.55656 0.94646 0.53798 0.30883 0.95922 0.25618 0.88795 0.71952 
0.59451 0.24768 0.93903 0.47206 0.29866 0.51457 0.12949 0.33910 0.95339 
0.54669 0.42338 0.74931 0.59635 0.18434 0.64378 0.93642 0.97486 0.94005 
0.40820 0.31506 0.30245 0.96533 0.12602 0.84050 0.72321 0.74207 0.63519 
0.42873 0.36274 0.76549 0.62227 0.00959 0.96444 0.15242 0.34530 0.03668 
0.45388 0.48226 0.08702 0.58137 0.60016 0.95801 0.56830 0.59907 0.32888 
0.71327 0.91021 0.94512 0.54539 0.51454 0.64956 0.74412 0.29857 0.10853 
0.07446 0.20219 0.47367 0.90183 0.67606 0.71664 0.15257 0.31392 0.26714 
0.69980 0.38769 0.27550 0.53231 0.61679 0.39430 0.06955 0.76592 0.70375 

################
h=proj.subM(12,18,5,11):
 
Square matrix
Dimension: 7x7
Features: ['Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10', 'Col 11']

96 35 31 47 55 58 88 
35 71 89  7  5 44 44 
 5 94 47 69 28 73 92 
97 35 99 16  7 97 57 
57 62 20 72  3 46 33 
38 25 39 11 24 94 72 
72 30 23 88 34 62 99 

h.mean(): {'Col 5': 57.142857142857146, 'Col 6': 50.285714285714285, 'Col 7': 49.714285714285715, 'Col 8': 44.285714285714285, 'Col 9': 22.285714285714285, 'Col 10': 67.71428571428571, 'Col 11': 69.28571428571429}

h.det: 1287494735579.9985

h.rank: 7

h.rrechelon: 
Float Matrix
Square matrix
Dimension: 7x7
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7']

1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 


h.inv:

Float Matrix
Square matrix
Dimension: 7x7
Features: ['Col 8', 'Col 9', 'Col 10', 'Col 11', 'Col 12', 'Col 13', 'Col 14']

 0.0011  0.0229 -0.0279 -0.0196  0.0155  0.0175  0.0081 
 0.0015  0.0268 -0.0174 -0.0279  0.0197  0.0212 -0.0029 
 0.0048 -0.0282  0.0340  0.0407 -0.0241 -0.0400 -0.0096 
 0.0028 -0.0406  0.0363  0.0380 -0.0121 -0.0393 -0.0074 
 0.0398 -0.0745  0.0710  0.0630 -0.0317 -0.0622 -0.0487 
 0.0017 -0.0272  0.0178  0.0197  0.0007 -0.0011 -0.0167 
-0.0195  0.0605 -0.0501 -0.0545  0.0096  0.0471  0.0410 

h.minor(3,4):
 
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 5', 'Col 6', 'Col 7']

96 35 31 55 58 88 
35 71 89  5 44 44 
97 35 99  7 97 57 
57 62 20  3 46 33 
38 25 39 24 94 72 
72 30 23 34 62 99 
 

################
j=g.sub(1,2,1,4):
 
Dimension: 2x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

6 8 6 1 
2 5 1 5 
 

j.summary:
 Matrix(dim=[2, 4],listed=[[6, 8, 6, 1], [2, 5, 1, 5]],ranged=[-5, 5],randomFill=True,features=['Col 1', 'Col 2', 'Col 3', 'Col 4'],header=False,directory='')

################
proj=proj.subM(5,15).copy:


Dimension: 5x15
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10', 'Col 11', 'Col 12', 'Col 13', 'Col 14', 'Col 15']

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 

################
p: 
Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

50  2 37 54 62 
20 57  8 18 45 
 0 27 63 57 37 
 9 32 65 68 72 
63 94 54 38 49 

p.det:
 112561285.00000006

p.adj:
 
Float Matrix
Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

  1584455.0000   -780900.0000   -170270.0000  -1459585.0000    985600.0000 
  -284063.0000   2494655.0000   2635458.0000  -2529241.0000   -205187.0000 
 -3148907.0000  -7042600.0000  -7145638.0000   8377366.0000   3538112.0000 
  4693849.0000   8093075.0000  13395541.0000 -12960172.0000  -4443054.0000 
 -1662123.0000  -2296680.0000  -7350452.0000   7547169.0000    970083.0000 

p.inv:


Float Matrix
Square matrix
Dimension: 5x5
Features: ['Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10']

 0.0141 -0.0069 -0.0015 -0.0130  0.0088 
-0.0025  0.0222  0.0234 -0.0225 -0.0018 
-0.0280 -0.0626 -0.0635  0.0744  0.0314 
 0.0417  0.0719  0.1190 -0.1151 -0.0395 
-0.0148 -0.0204 -0.0653  0.0670  0.0086 

################
p:

Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

50  2 37 54 62 
20 57  8 18 45 
 0 27 63 57 37 
 9 32 65 68 72 
63 94 54 38 49 

p.remove(c=1) and p.remove(r=2)

Square matrix
Dimension: 4x4
Features: ['Col 2', 'Col 3', 'Col 4', 'Col 5']

 2 37 54 62 
27 63 57 37 
32 65 68 72 
94 54 38 49 

p.add(col=2,lis=[55,55,55,55,55]):

Dimension: 4x5
Features: ['Col 2', 'Col', 'Col 3', 'Col 4', 'Col 5']

 2 55 37 54 62 
27 55 63 57 37 
32 55 65 68 72 
94 55 54 38 49 

p.sdev()
{'Col 2': 39.10136400007891, 'Col': 0.0, 'Col 3': 12.76388133236386, 'Col 4': 12.39287429668087, 'Col 5': 15.253414918196734}
################

proj.find(40)
[(1, 8), (2, 4), (2, 12), (3, 11), (5, 14), (5, 15)]

proj.find(40,0)
[(0, 7), (1, 3), (1, 11), (2, 10), (4, 13), (4, 14)]

proj.find(111)
Value not in the matrix
################

id2:
 
Identity Matrix
Dimension: 5x5

 1  0  0  0  0 
 0  1  0  0  0 
 0  0  1  0  0 
 0  0  0  1  0 
 0  0  0  0  1 


id2.addDim(2): 
Identity Matrix
Dimension: 7x7

 1  0  0  0  0  0  0 
 0  1  0  0  0  0  0 
 0  0  1  0  0  0  0 
 0  0  0  1  0  0  0 
 0  0  0  0  1  0  0 
 0  0  0  0  0  1  0 
 0  0  0  0  0  0  1 

id2.matrix:
 [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]]
################
id3:


Identity Matrix
Dimension: 3x3

 1  0  0 
 0  1  0 
 0  0  1 

################
id4:


Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 


id4.delDim(6):

All rows have been deleted

Identity Matrix
Dimension: 0x0


################
id4: 
Identity Matrix
Dimension: 0x0



id4.addDim(10)):
 
Identity Matrix
Dimension: 10x10

 1  0  0  0  0  0  0  0  0  0 
 0  1  0  0  0  0  0  0  0  0 
 0  0  1  0  0  0  0  0  0  0 
 0  0  0  1  0  0  0  0  0  0 
 0  0  0  0  1  0  0  0  0  0 
 0  0  0  0  0  1  0  0  0  0 
 0  0  0  0  0  0  1  0  0  0 
 0  0  0  0  0  0  0  1  0  0 
 0  0  0  0  0  0  0  0  1  0 
 0  0  0  0  0  0  0  0  0  1 

################
r=p.t
r.remove(r=2):

Square matrix
Dimension: 4x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

 2 27 32 94 
37 63 65 54 
54 57 68 38 
62 37 72 49 

r.rank: 4

r[0]=r[1][:]

Square matrix
Dimension: 4x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

37 63 65 54 
37 63 65 54 
54 57 68 38 
62 37 72 49 

Determinant is 0, can't get lower/upper triangular matrices
r.rank: 3
################################
Operator examples
################

c.dim= [2, 4]  d.dim: [4, 3]

mMulti=c@d:

Float Matrix
Dimension: 2x3
Features: ['Col 1', 'Col 2', 'Col 3']

 -2.5495   3.4913 -16.6768 
-17.1772 -22.3709 -24.5195 


((((mMulti)+125)**3)%2):

Float Matrix
Dimension: 2x3
Features: ['Col 1', 'Col 2', 'Col 3']

1.5537 1.4108 0.2573 
0.1687 1.2551 0.9044 

################

f:
 
Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  929.1768   406.8270   538.5267  -530.0911  -474.3029   -41.7780 
 -118.8649   133.0728   866.0093  -300.1095  1051.6778  -915.7099 
 -958.0214   421.0756  1057.2273  1036.3870 -1040.2774   818.2078 
  436.4906   425.1540   431.9700  1150.8095  -966.0850   161.8615 
 -610.5025   311.1176   307.3141  -557.5741   -12.7051  -302.0376 
  720.4246   553.8861  1114.9347    46.1970  -961.3555    98.3581 

f1=f.intForm

Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  929   406   538  -530  -474   -41 
 -118   133   866  -300  1051  -915 
 -958   421  1057  1036 -1040   818 
  436   425   431  1150  -966   161 
 -610   311   307  -557   -12  -302 
  720   553  1114    46  -961    98 

f2=f.roundForm(3)

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  929.1800   406.8300   538.5300  -530.0900  -474.3000   -41.7800 
 -118.8600   133.0700   866.0100  -300.1100  1051.6800  -915.7100 
 -958.0200   421.0800  1057.2300  1036.3900 -1040.2800   818.2100 
  436.4900   425.1500   431.9700  1150.8100  -966.0900   161.8600 
 -610.5000   311.1200   307.3100  -557.5700   -12.7100  -302.0400 
  720.4200   553.8900  1114.9300    46.2000  -961.3600    98.3600 

f2-f1

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

 0.1800  0.8300  0.5300 -0.0900 -0.3000 -0.7800 
-0.8600  0.0700  0.0100 -0.1100  0.6800 -0.7100 
-0.0200  0.0800  0.2300  0.3900 -0.2800  0.2100 
 0.4900  0.1500  0.9700  0.8100 -0.0900  0.8600 
-0.5000  0.1200  0.3100 -0.5700 -0.7100 -0.0400 
 0.4200  0.8900  0.9300  0.2000 -0.3600  0.3600 

################
e+=Identity(e.dim[0])*99

Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

99  0  0  0  0  0  0  0 
 0 99  0  0  0  0  0  0 
 0  0 99  0  0  0  0  0 
 0  0  0 99  0  0  0  0 
 0  0  0  0 99  0  0  0 
 0  0  0  0  0 99  0  0 
 0  0  0  0  0  0 99  0 
 0  0  0  0  0  0  0 99 


e-=33:

Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

 66 -33 -33 -33 -33 -33 -33 -33 
-33  66 -33 -33 -33 -33 -33 -33 
-33 -33  66 -33 -33 -33 -33 -33 
-33 -33 -33  66 -33 -33 -33 -33 
-33 -33 -33 -33  66 -33 -33 -33 
-33 -33 -33 -33 -33  66 -33 -33 
-33 -33 -33 -33 -33 -33  66 -33 
-33 -33 -33 -33 -33 -33 -33  66 


e+=FMatrix(e.dim):

Float Matrix
Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

 66.6259 -32.8824 -32.8704 -32.6032 -32.9167 -32.4574 -32.8098 -32.6343 
-32.6676  66.9179 -32.1691 -32.0942 -32.7876 -32.6916 -32.7562 -32.1596 
-32.8124 -32.7963  66.4258 -32.6649 -32.8900 -32.0467 -32.7930 -32.7254 
-32.4794 -32.3746 -32.8298  66.8817 -32.8257 -32.8546 -32.7991 -32.2459 
-32.9069 -32.6324 -32.5170 -32.7167  66.1998 -32.0346 -32.6013 -32.4904 
-32.8657 -32.5016 -32.6797 -32.3902 -32.0898  66.7044 -32.6180 -32.0046 
-32.4336 -32.3481 -32.4738 -32.4374 -32.3167 -32.1420  66.4658 -32.4155 
-32.0659 -32.6124 -32.3273 -32.9161 -32.6268 -32.4459 -32.3792  66.7556 


e*=[2,1,1,0.5,0.2,0.0003,1,3]:

Float Matrix
Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

133.2518 -32.8824 -32.8704 -16.3016  -6.5833  -0.0097 -32.8098 -97.9030 
-65.3352  66.9179 -32.1691 -16.0471  -6.5575  -0.0098 -32.7562 -96.4789 
-65.6248 -32.7963  66.4258 -16.3324  -6.5780  -0.0096 -32.7930 -98.1761 
-64.9587 -32.3746 -32.8298  33.4408  -6.5651  -0.0099 -32.7991 -96.7377 
-65.8139 -32.6324 -32.5170 -16.3584  13.2400  -0.0096 -32.6013 -97.4712 
-65.7314 -32.5016 -32.6797 -16.1951  -6.4180   0.0200 -32.6180 -96.0137 
-64.8672 -32.3481 -32.4738 -16.2187  -6.4633  -0.0096  66.4658 -97.2465 
-64.1317 -32.6124 -32.3273 -16.4581  -6.5254  -0.0097 -32.3792 200.2669 

e%=[2,2,2,2,1,1,1,1]

Float Matrix
Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

3.2518 2.1176 2.1296 3.6984 2.4167 2.9903 0.1902 0.0970 
4.6648 1.9179 2.8309 3.9529 2.4425 2.9902 0.2438 0.5211 
4.3752 2.2037 1.4258 3.6676 2.4220 2.9904 0.2070 0.8239 
0.0413 2.6254 2.1702 3.4408 2.4349 2.9901 0.2009 0.2623 
4.1861 2.3676 2.4830 3.6416 1.2400 2.9904 0.3987 0.5288 
4.2686 2.4984 2.3203 3.8049 2.5820 0.0200 0.3820 0.9863 
0.1328 2.6519 2.5262 3.7813 2.5367 2.9904 0.4658 0.7535 
0.8683 2.3876 2.6727 3.5419 2.4746 2.9903 0.6208 0.2669 

################

c%j

Dimension: 2x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

3 2 2 0 
1 3 0 0 


(f.lowtri@f.uptri).roundForm(4)==f.roundForm(4)
True

################################
Strings' matrices:
################

validStr1:

Dimension: 2x3
Features: ['Col 1', 'Col 2', 'Col 3']

 34 -52  33 
  9  88  -3 

################
validStr2:
You should give proper dimensions to work with the data
Example dimension:[data_amount,feature_amount]

Dimension: 1x10
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10']

312  45  12  44 352  45  12  44   3  -5 

################
validStr3:
You should give proper dimensions to work with the data
Example dimension:[data_amount,feature_amount]

Dimension: 1x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

 34   5  44 659 

################
validStr4:

Dimension: 22x3
Features: ['Height', 'Weight', 'Age']

130  30  10 
125  36  11 
135  34  10 
133  30   9 
129  38  12 
180  90  30 
190  80  25 
175  90  35 
177  60  22 
185 105  33 
165  55  27 
155  50  44 
160  58  39 
162  59  41 
167  62  55 
174  70  47 
193  90  23 
187  80  27 
183  88  28 
159  40  29 
164  66  32 
166  56  42 

################

validStr4.ranged()
{'Height': [125, 193], 'Weight': [30, 105], 'Age': [9, 55]}

validStr4.mean()
{'Height': 163.36363636363637, 'Weight': 62.13636363636363, 'Age': 28.681818181818183}

validStr4.sdev()
{'Height': 21.077059193407987, 'Weight': 22.286650829472002, 'Age': 12.98858973112413}

validStr4.median()
{'Height': 166, 'Weight': 60, 'Age': 29}

validStr4.freq()
{'Height': {130: 1, 125: 1, 135: 1, 133: 1, 129: 1, 180: 1, 190: 1, 175: 1, 177: 1, 185: 1, 165: 1, 155: 1, 160: 1, 162: 1, 167: 1, 174: 1, 193: 1, 187: 1, 183: 1, 159: 1, 164: 1, 166: 1}, 'Weight': {30: 2, 36: 1, 34: 1, 38: 1, 90: 3, 80: 2, 60: 1, 105: 1, 55: 1, 50: 1, 58: 1, 59: 1, 62: 1, 70: 1, 88: 1, 40: 1, 66: 1, 56: 1}, 'Age': {10: 2, 11: 1, 9: 1, 12: 1, 30: 1, 25: 1, 35: 1, 22: 1, 33: 1, 27: 2, 44: 1, 39: 1, 41: 1, 55: 1, 47: 1, 23: 1, 28: 1, 29: 1, 32: 1, 42: 1}}

validStr4.mode()
{'Height': {'All': 1}, 'Weight': {'90': 3}, 'Age': {'10, 27': 2}}

validStr4.iqr()
{'Height': 25, 'Weight': 40, 'Age': 17}

validStr4.iqr(as_quartiles=True)
{'Height': [155, 166, 180], 'Weight': [40, 60, 80], 'Age': [22, 29, 39]}

validStr4.variance()
{'Height': 444.24242424242414, 'Weight': 496.6948051948051, 'Age': 168.70346320346317}

################
Linear model for validStr4:

validStr4.corr().p #First and second columns have strong positive correlation. Let's choose first column to be predicted

var=validStr4.subM(1,validStr4.dim[0],2,2)
var.add("bias",[1]*validStr4.dim[0],col=1)

out=validStr4.subM(1,validStr4.dim[0],1,1)

coefs=(((var.t@var).inv)@var.t)@out

preds=var@coefs
err=out-preds


Float Matrix
Square matrix
Dimension: 3x3
Features: ['Col 1', 'Col 2', 'Col 3']

1.0000 0.9420 0.5329 
0.9420 1.0000 0.4434 
0.5329 0.4434 1.0000 

Height=110.52445385731674 + 0.8503745538690818*Weight

Average error: -1.4081665126881984e-13
"""
# =============================================================================
