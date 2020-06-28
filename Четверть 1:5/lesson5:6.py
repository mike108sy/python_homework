with open("file5:6.txt", "r") as f:
    lines = f.readlines()
my_dict = {}
for line in lines:
    ind = line.find(':')
    subject = line[:ind]
    line_new = line.split()
    hours_subject = 0
    for i in line_new:
        ind2 = i.find('(')
        if ind2 != -1:
            hour = i[0:ind2]
            hours_subject = hours_subject + int(hour)
        else:
            continue
    my_dict[subject] = hours_subject
print(my_dict)
