#printing average marks
M = [['name','maths','eng','phy','com''nep'],
          ['john',88.0,86.0,76.0,66.0,76.0],
          ['sam',77.0,67.0,87.0,67.0,56.0],
          ['anna',67.0,65.0,67.0,76.0,65.0]]
a=0
for i in range(len(M)):
    if i !=0:
        a=a+ M[i][1]
b=a/(len(M)-1)
print(f'the average marks of all student in maths is {b}')
#printing total and average marks of anna
c=0
for j in range(len(M[3])):
    if j !=0:
        c=c+M[3][j]
d=c/(len(M[0])-1)
print(f'the average marks of all student in maths is {d}')
