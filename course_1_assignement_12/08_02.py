stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org = org.split()
acro = ""
for i in org:
    if i in stopwords:
        pass
    else :
        acro += i[0].upper()
print(acro)


# Write code that uses the string stored in org and creates 
# an acronym which is assigned to the variable acro. 
# Only the first letter of each word should be used, 
# each letter in the acronym should be a capital letter, 
# and there should be nothing to separate the letters of 
# the acronym. Words that should not be included in the 
# acronym are stored in the list stopwords. For example, 
# if org was assigned the string “hello to world” then the 
# resulting acronym should be “HW”.