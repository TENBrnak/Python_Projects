# My answer to a question about stacking boxes on top of one another
# found in a local coding contest
no_krabic, seznam, width = int(input()), [], 0.0
for i in range(no_krabic):
    temp = input().split()
    if int(temp[0]) >= int(temp[1]):
        seznam.append(int(temp[0]))
    else:
        seznam.append(int(temp[1]))
seznam.sort()
width += seznam.pop(-1)
for i in seznam:
    width += i/2
print(width)
