n = int(input("veuillez saisir la taille du tableau: "))
T = []

for i in range(n):
    element = float(input(f"L element {i + 1} "))
    T.append(element)
    
    for i in range(len(T) - 1):
        pos_min = i
        for j in range(i + 1, len(T)):
            if T[j] > T[i]:
                pos_min = j
                
                T[i], T[pos_min] = T[pos_min], T[i]
                
print("Le tableau trie est : ", T)