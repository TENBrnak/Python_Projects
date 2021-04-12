# my answer to a question on Hackerrank.com
arr = input().split()
arr = [int(i) for i in arr]
cata = arr[0]
catb = arr[1]
mouse = arr[2]
if mouse - cata > mouse - catb:
    print("Cat A")
if mouse - cata < mouse - catb:
    print("Cat B")
if mouse - cata == mouse - catb:
    print("Mouse C")
