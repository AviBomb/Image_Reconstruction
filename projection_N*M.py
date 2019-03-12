#Function responsible for reading in The Array from the .csv file
def read():
    import csv
    matrix=[]
    with open('xyz.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            row_matrix=[]
            for i in row:
                row_matrix.append(int(i));
            matrix.append(row_matrix)
    return(matrix)

#Start Reading Of Array from .CSV file
Original_Matrix=[]
Original_Matrix=read()
print(Original_Matrix)

#Finding the Order of a Matrix (Number of Rows)
n=0
for i in Original_Matrix:
    n=n+1
#print(n)

#Finding the Order of a Matrix (Number of Columns)
m=0
for i in Original_Matrix:
    for j in i:
        m=m+1
    break
#print(m)

#Calculating Row Wise Sum
row_sum=[]
for i in range(0,n):
    temp=[]
    sum=0
    for j in range(0,m):
        sum=sum+Original_Matrix[i][j]
    for k in range(0,m):
        temp.append(sum)
    row_sum.append(temp)
print(row_sum)

#Calculating The Difference between Row1's and Row2's Sum
row0=row_sum[0][0]
div=(row_sum[0][0]-row_sum[1][0])
# print(div)

#Operating Matrix (Duplicating the matrix to carry out Calculations)
operating_matrix=[]
for i in row_sum:
    operating_matrix.append(i)
#print(operating_matrix)

#Sum of the Elements Along the Main Diagonal
maindiagonal_sum=[]
for k in range(-n+1,m):
    diagonal_sum=0
    for i in range(0,n):
        for j in range(0,m):
            if((k+i)==j):
                diagonal_sum=diagonal_sum+Original_Matrix[i][j]
    maindiagonal_sum.append(diagonal_sum)
print(maindiagonal_sum)

#Adding the Main Diagonal Elements to the Matrix
temp=0
for k in range(-n+1,m):
    for i in range(0,n):
        for j in range(0,m):
            if((k+i)==j):
                operating_matrix[i][j]=maindiagonal_sum[temp]+operating_matrix[i][j]
    temp=temp+1
print(operating_matrix)

#Calculating Column Wise Sum
column_sum=[]
for i in range(0,m):
    sum=0
    for j in range(0,n):
        sum=sum+Original_Matrix[j][i]
    column_sum.append(sum)
print (column_sum)

#Adding Column Sums to each Column
for i in range(0,n):
    for j in range(0,m):
        operating_matrix[i][j]=column_sum[j]+operating_matrix[i][j]
print (operating_matrix)

#Sum of the Elements Along the Other Diagonal
otherdiagonal_sum=[]
for k in range(0,((n+m)-1)):
    diagonal_sum=0
    for i in range(0,n):
        for j in range(0,m):
            if((i+j)==k):
                diagonal_sum=diagonal_sum+Original_Matrix[i][j]
    otherdiagonal_sum.append(diagonal_sum)
print(otherdiagonal_sum)

#Adding the Other Diagonal Elements to the Matrix
for k in range(0,((m+n)-1)):
    for i in range(0,n):
        for j in range(0,m):
            if((i+j)==k):
                operating_matrix[i][j]=otherdiagonal_sum[k]+operating_matrix[i][j]
print(operating_matrix)

#Calculate The Sum of Each row in the final Matrix
total_sum_column=[]
for i in range(0,n):
    tsum=0
    for j in range(0,m):
        tsum=tsum+operating_matrix[i][j]
    total_sum_column.append(tsum)

#Calculating the Value the Matrix needs to be Divided by
div1=(total_sum_column[0]-total_sum_column[1])/div
#print(div1)

#Calculating the Value that needs to be Subtracted from the Matrix
sub=(total_sum_column[0]-(row0*div1))/m
#print(sub)

#Subtraction of Value from Matrix
for i in range(0,n):
    for j in range(0,m):
        operating_matrix[i][j]=operating_matrix[i][j]-sub
print(operating_matrix)

#Divided By Value in Matrix
for i in range(0,n):
    for j in range(0,m):
        operating_matrix[i][j]=round(operating_matrix[i][j]/div1)
print(operating_matrix)
