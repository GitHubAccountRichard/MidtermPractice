with open("emails.txt", "r") as e:
    for line in e:
        if "@" in line:
            print(line, end ="")

count = 0
while count < 10:
    count += 1
    print(count)

count2 = 0
number = 0
while count2 <= 100:
    number += count2
    count2 += 1
print(number)
