# my answer to a question found in a local coding contest
# about which inputs will hit a target and which won't
# read = open("Directory to the input file", "r")
count = 0
readed = read.readlines()
arr = readed[count].split()
count += 1
xterce = float(arr[0])
yterce = float(arr[1])
radius = float(arr[2])
f = open("output.txt", "a")
for i in range(int(readed[count])):
    count += 1
    coords = readed[count].split()
    x = float(coords[0]) - xterce
    y = float(coords[1]) - yterce
    if x**2 + y**2 <= radius**2:
        f.write(str(i + 1) + "\n")
