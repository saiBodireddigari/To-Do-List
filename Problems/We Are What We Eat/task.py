# the list "meals" is already defined
# your code here
k_cal = 0
for dic in meals:
    k_cal += dic.get("kcal")

print(k_cal)
