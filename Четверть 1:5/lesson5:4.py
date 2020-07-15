with open("file5:4.txt") as f:
    file_new = []
    lines = f.readlines()
    f.seek(0)
    for i in lines:
        line = f.readline()
        ind = line.find(' ')
        if line[:ind] == 'One':
            line_new = line.replace('One', 'Один')
        elif line[:ind] == 'Two':
            line_new = line.replace('Two', 'Два')
        elif line[:ind] == 'Three':
            line_new = line.replace('Three', 'Три')
        elif line[:ind] == 'Four':
            line_new = line.replace('Four', 'Четыре')
        else:
            line_new = line
        file_new.append(line_new)
with open('file5:4:new.txt', 'w') as f_new:
    f_new.writelines(file_new)
