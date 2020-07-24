items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for i in items:
    if i.find('w') > -1:
        acc_num += 1
print(acc_num)