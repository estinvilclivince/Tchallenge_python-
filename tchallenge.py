#prmye exo a 
chenn = "Ayibobo Ayiti"
chenn_an_miniskil = chenn.lower()
print(chenn_an_miniskil)

# dezyem exo a 
def koupe_ekzanp(chenn):
    eleman  = chenn.split()
    return eleman 

# Egzanp d'apre sa ou te bay:
chenn = "Ayibobo Ayiti"
lis = koupe_ekzanp(chenn)
print(lis)
 # Mete tout premye let chak mo an majiskil:
chenn="yon chenn ak plizye mo"
chenn_majiskil= " ".join(word.capitalize()for word in chenn.split() )
print(chenn_majiskil)


#Rekipire premye let ckak mo ak afiche yon nouvo chenn ak tout inisyal sa yo 

chenn ="yon chenn ak plizye mo "
inisyal_chenn="".join(word[0] for word in chenn.split())
print(inisyal_chenn)

# Ranplase tout karakte "a" nan yon pa "@"

chenn ="yon chenn ak plizye mo "
nouvo_chenn =chenn.replace("a","@")
print(nouvo_chenn)


#mete yon chenn karakte devan deye ,epi mete l an majiskil
chenn ="Ayiti"
nouvo_chenn= chenn[::-1].capitalize()
print(nouvo_chenn)



#Afiche eneks premye karakte "a"nan yon chenn
chenn ="Ayiti kapab avanse "
endeks =chenn.find("a")
print(endeks)

#Afiche total tout endeks karakte "a" nan yon chenn (ki se a majiskil oubyen miniskil)
chenn ="Ayiti kapab avanse"
total_endeks=[i for i, letter in enumerate(chenn) if letter == "a" or letter == "A"]
print(len(total_endeks))

#Kreye yon lis ki gen endeks tout karakte "a" nan yon chenn (selman a miniskil)
chenn ="Ayiti Kapab Avanse "
endeks_a_moiniskil =  [i for i, letter in enumerate(chenn) if letter == "a"]
print(endeks_a_moiniskil)

chenn = "yon chenn ak espas "
chenn_san_espas = chenn.replace(" ", "")  # Retire espas la
kantite_karakte = len(chenn_san_espas)  # Kalkile kantite karaktè nan chenn sa
print(chenn_san_espas)  # Résultat: "yonchennakespas"
print(kantite_karakte)  # Résultat: 16


n = 10
lis_divizib_pa_2 = [x for x in range(n+1) if x % 2 == 0]
print(lis_divizib_pa_2)


lis_antye = [1, 2, 3, 4, 5]
lis_chenn = [str(x) for x in lis_antye]
print(lis_chenn)




lis_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lis_divizib_pa_3 = [lis_original[i] for i in range(len(lis_original)) if i % 3 == 0]
print(lis_divizib_pa_3)



lis_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lis_gwoup = [tuple(lis_original[i:i+3]) for i in range(0, len(lis_original), 3)]
print(lis_gwoup)


lis_avek_doublon = [1, 2, 2, 3, 4, 4, 4, 5]
lis_sans_doublon = list(set(lis_avek_doublon))
print(lis_sans_doublon)


lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis_komen = [x for x in lis1 if x in lis2]
print(lis_komen)


lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis_distenge = [x for x in lis1 if x not in lis2] + [x for x in lis2 if x not in lis1]
print(lis_distenge)



diksyone = {"kle1": "valè1", "kle2": "valè2", "kle3": "valè3"}
lis_kle = list(diksyone.keys())
lis_valè = list(diksyone.values())
print(lis_kle)
print(lis_valè)


lis1 = [1, 2, 3]
lis2 = [2, 3, 4]
lis3 = [3, 4, 5]
lis_ansanm = list(set(lis1 + lis2 + lis3))
print(lis_ansanm)

lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis3 = [5, 6, 7, 8, 9]

# Konvèti chak lis an nan yon set
set1 = set(lis1)
set2 = set(lis2)
set3 = set(lis3)

# Reyini yo ansanm ak operatè `union`
lis_reyini = list(set1 | set2 | set3)

print(lis_reyini)
