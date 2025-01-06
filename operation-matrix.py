linges = int(input("Veuillez saisir les lignes de la matrice A."))
colonnes = int(input("Veuillez saisir les colonnes de la matrice A."))

A = [[0 for _ in range(colonnes)] for _ in range(linges)]
B = [[0 for _ in range(colonnes)] for _ in range(linges)]

print("Saisir les elements de la amatrice A.")
for i in range(linges):
    for j in range(colonnes):
        A[i][j] = float(input(f"Element A[{i + 1}] [{j + 1}] : "))
        
print("Saisir les elements de la amatrice B.")
for i in range(linges):
    for j in range(colonnes):
        B[i][j] = float(input(f"Element B[{i + 1}] [{j + 1}] : "))
        
C = [[0 for _ in range(linges)] for _ in range(colonnes)] 

for i in range(linges):
    for j in range(colonnes):
        C[i][j] = A[i][j] + B[i][j]  
        
print("Matrice A:")
for ligne in A:
    print(ligne)   
  
print("Matrice B:")
for ligne in B:
    print(ligne)  
    
print("Resultat de l addition des deux matrices est :")
for ligne in C:
    print(ligne) 
