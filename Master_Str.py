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