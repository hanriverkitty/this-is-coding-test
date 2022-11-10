
a = input()
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
go = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)]
count = 0
for i in range(len(l)):
    if(l[i] == a[0]):
        column = i+1
row = int(a[1])
for i in go:
    if(column+i[0] >= 1 and column+i[0] <= 8 and row+i[1] >= 1 and row+i[1] <= 8):
        count += 1
print(count)
