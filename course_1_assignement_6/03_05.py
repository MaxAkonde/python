addition_str = "2+5+10+20"
addition_str = addition_str.split("+")
sum_val = 0
for i in addition_str:
    sum_val += int(i)
print(sum_val)