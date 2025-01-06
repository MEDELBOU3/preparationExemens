n = int(input("Veuillez sasir la taille du tableau : "))
T = []

for i in range(n):
    element = float(input(f"L element {i + 1} : "))
    T.append(element)
    
echange = True
while echange:
    echange = False
    for i in range(len(T) - 1):
        if T[i] > T[i + 1]:
            T[i], T[i + 1] = T[i + 1], T[i]
            echange = True
            
            print("Le tableau trie est : ", T)