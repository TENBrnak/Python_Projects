# My answer to a question about possible answers found in a local coding contest
# read = open(r"Directory of the neccessary file", "r")
readed = read.readlines()
count = 0
form = readed[count].split("*")
count += 1
start, end, tests = form[0], form[1], []
for i in range(int(readed[count])):
    count += 1
    tests.append(readed[count])
start_len, end_len  = len(start), len(end)
capitals, lower, numbers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789"

hi = open("test5.txt", "a")
for i in tests:
    flag = True
    istart = i[:start_len]
    iend = i[-(end_len):]
    if len(i) < start_len + end_len:
        hi.write("ne\n")
        continue
    for n, j in enumerate(start):
        if j == "A":
            if istart[n] not in capitals:
                hi.write("ne\n")
                flag = False
                break
        elif j == "a":
            if istart[n] not in lower:
                hi.write("ne\n")
                flag = False
                break
        elif j == "0":
            if istart[n] not in numbers:
                hi.write("ne\n")
                flag = False
                break
    if flag:
        for n, j in enumerate(end):
            if j == "A":
                if iend[n] not in capitals:
                    hi.write("ne\n")
                    flag = False
                    break
            elif j == "a":
                if iend[n] not in lower:
                    hi.write("ne\n")
                    flag = False
                    break
            elif j == "0":
                if iend[n] not in numbers:
                    hi.write("ne\n")
                    flag = False
                    break
    if flag:
        hi.write("ano\n")
