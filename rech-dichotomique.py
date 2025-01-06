n = int(input("veuillez saisir la taille du tableau : "))
T = []

for i in range(n):
    element = float(input(f"L element {i + 1} : "))
    T.append(element)
   
N = len(T) 
for i in range(len(T)):
    pos_min = i
    for j in range(i + 1, len(T)):
        if T[j] < T[pos_min]:
            pos_min = j
            T[i], T[pos_min] = T[pos_min], T[i]
            
print("tableau trie est : ", T)

x = float(input("Veuillez saisir element x : "))
deb = 0
fin = len(T) - 1
b = False

while deb <= fin :
    mil = (deb + fin) // 2
    if T[mil] == x:
        b = True
        print(f"L element {x} est trouvable a l indice {mil} . ")
        break
    elif T[mil] < x:
        deb = mil + 1
    else :
        fin = mil - 1
        
    if not b:
        print(f"l element {x} n existe pas dans le tableau.")
        
    