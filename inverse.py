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
# print(n)

#Finding the Order of a Matrix (Number of Columns)
m=0
for i in Original_Matrix:
    for j in i:
        m=m+1
    break
# print(m)
index=0
while (index!=7):
    x = input('Enter : 1. To Add a Vertex 2. To Add an Edge 3. To Delete a Vertex 4. To Delete an Edge 5. To Calculate the Inverse of Matrix 6. To Display Matrix 7. To Exit ')
    y = x.split()
    index=int(y[0])

    #Adding a Vertex to the Matrix
    if(index==1):
        for i in range(0,n):
                Original_Matrix[i].append(0)
        temp=[]
        n=n+1
        m=m+1
        for i in range(0,m):
                temp.append(0)
        Original_Matrix.append(temp)
        print(Original_Matrix)

    #Adding an Edge to the Matrix
    if(index==2):
        a = input('Enter the Row Number of Edge : ')
        b = a.split()
        row=int(b[0])
        a = input('Enter the Column Number of Edge : ')
        b = a.split()
        column=int(b[0])
        #a = input('Enter the value for the Vertex : ')
        #b = a.split()
        #value=int(b[0])
        for i in range(0,n):
            for j in range(0,m):
                if(i==row-1 and j==column-1):
                    Original_Matrix[i][j]=1
                if(j==row-1 and i==column-1):
                    Original_Matrix[i][j]=1
        print(Original_Matrix)

    #Deleting a Vertex to the Matrix
    if(index==3):
        a = input('Enter the Vertex to be Deleted : ')
        b = a.split()
        v=int(b[0])
        deleted_vertex=[]
        for i in range(0,n):
            temp=[]
            for j in range(0,m):
                if(i==v-1 or j==v-1):
                    continue
                else:
                    temp.append(Original_Matrix[i][j])
            if not temp:
                continue
            else:
                deleted_vertex.append(temp)
        n=n-1
        m=m-1
        Original_Matrix=[]
        for i in deleted_vertex:
            Original_Matrix.append(i)
        print(Original_Matrix)

    #Deleting an Edge to the Matrix
    if(index==4):
        a = input('Enter the Row Number of Edge : ')
        b = a.split()
        row=int(b[0])
        a = input('Enter the Column Number of Edge : ')
        b = a.split()
        column=int(b[0])
        for i in range(0,n):
            for j in range(0,m):
                if(i==row-1 and j==column-1):
                    Original_Matrix[i][j]=0
                if(j==row-1 and i==column-1):
                    Original_Matrix[i][j]=0
        print(Original_Matrix)

    #Calculating the Inverse of Matrix
    if(index==5):
        inverse_matrix=[]
        for i in range(0,m):
            temp=[]
            for j in range(0,n):
                temp.append(Original_Matrix[j][i])
            inverse_matrix.append(temp)
        Original_Matrix=[]
        for i in inverse_matrix:
            Original_Matrix.append(i)
        print(Original_Matrix)
        j=n
        n=m
        m=j

    #Displaying The Matrix
    if(index==6):
        print(Original_Matrix)

    #Exiting
    if(index==7):
        print("Exiting")
