n=int(input("input the demention:"))
print ("input the item of the matrix A:")
A =[[float(input(f"A[{i}][{j}] =")) for j in range(n)] for i in range (n) ]
for row in A:
    print(row)
print ("input the item of the matrix B:")
B =[[float(input(f"B[{i}][{j}] =")) for j in range(n)] for i in range (n) ]
for row in B:
    print(row)
x=float(input("input a num"))
addition = [[A[i][j] + B[i][j] for j in range (n)]for i in range (n)]
multiplucation_par_x = [[A[i][j] * x for j in range (n)]for i in range (n)]
multiplucation_matrix = [[sum(A[i][k]+B[k][i] for k in range (n) ) for j in range (n)] for i in range (n)]
diagonale_A = [A[i][i] for i in range (n)]
moyenne_A = sum(sum(row) for row in A)/(n*n)
moyenne_cols_B =sum(B[i][0] for i in range (n))/n
maximum_A = max(max(row) for row in A)

print("\nresult :")
print("A+B= ")
for row in addition:
    print(row)

print("\nA*x= ")
for row in multiplucation_par_x:
    print(row)

print("\nA*B= ")
for row in multiplucation_matrix:
    print(row)

print("\ndiagonale de A :v")
print(diagonale_A)

print("\nmoyenne de tous element de A : ")
print(moyenne_A)

print("\nmoyrnnr de la colones 1 de B : ")
print(moyenne_cols_B)

print("\nmaximum de A : ")
print(maximum_A)