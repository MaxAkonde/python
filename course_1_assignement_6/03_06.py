week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(",")
sum_val = 0
nb = 0
for i in week_temps_f:
    sum_val += float(i)
    nb += 1
avg_temp = sum_val/nb
print(avg_temp)


# week_temps_f is a string with a 
# list of fahrenheit temperatures separated by 
# the , sign. Write code that uses the accumulation 
# pattern to compute the average (sum divided by number of items) 
# and assigns it to avg_temp. Do not hard code your answer 
# (i.e., make your code compute both the sum or the number of 
# items in week_temps_f) (You should use the .split(",") 
# function to split by "," and float() to cast to a float).