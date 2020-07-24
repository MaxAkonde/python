week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(",")
sum_val = 0
nb = 0
for i in week_temps_f:
    sum_val += float(i)
    nb += 1
avg_temp = sum_val/nb
print(avg_temp)