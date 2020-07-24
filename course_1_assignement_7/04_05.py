s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = 0
for i in s:
    if i in vowels:
        num_vowels +=1
print(num_vowels)


# Write your code here.
# Écrivez un code qui comptera le nombre de voyelles dans 
# la phrase 
# s et attribuera le résultat à la variable num_vowels. 
# Pour ce problème, les voyelles ne sont 
# que a, e, i, o et u. Astuce: utilisez l' inopérateur 
# avec vowels.