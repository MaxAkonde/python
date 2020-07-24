sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
sentence = sentence.split(" ")
letters = ['a', 'e']
num_a_or_e = 0
for i in sentence:
    if i.find('a') > -1 or i.find('e') > -1:
        num_a_or_e += 1
print(num_a_or_e)
    

#Écrivez le code qui compte le nombre de mots sentence qui 
# contiennent soit un « a » ou un « e ». Stockez 
# le résultat dans la variable num_a_or_e.
#Remarque 1: veillez à ne pas compter deux fois les 
# mots contenant à la fois un a et un e.
#CONSEIL 1: utilisez l' inopérateur.
#CONSEIL 2: Vous pouvez utiliser or ou elif.
#Les réponses codées en dur ne recevront aucun crédit.