map_x, map_y = map(int, input().split())
cx, cy, d = map(int, input().split())
d += 4
cnt = 1
map = [list(map(int, input().split())) for _ in range(map_y)]


while(True):
    map[cy][cx] = 2
    if((map[cy+1][cx] == 1 or map[cy+1][cx] == 2) and (map[cy-1][cx] == 1 or map[cy-1][cx] == 2) and (map[cy][cx+1] == 1 or map[cy][cx+1] == 2) and (map[cy][cx-1] == 1 or map[cy][cx-1] == 2)):
        if(d % 4 == 0):
            if(map[cy+1][cx] == 2):
                cy += 1

            else:
                break
        elif(d % 4 == 3):
            if(map[cy][cx+1] == 2):
                cx += 1

            else:
                break
        elif(d % 4 == 2):
            if(map[cy-1][cx] == 2):
                cy -= 1

            else:
                break
        elif(d % 4 == 1):
            if(map[cy][cx-1] == 2):
                cx -= 1

            else:
                break
    else:
        if(d % 4 == 0):
            if(map[cy][cx-1] == 1 or map[cy][cx-1] == 2):
                d += 3
            else:
                map[cy][cx-1] = 2
                d += 3
                cx -= 1
                cnt += 1

        elif(d % 4 == 3):
            if(map[cy+1][cx] == 1 or map[cy+1][cx] == 2):
                d += 3
            else:
                map[cy+1][cx] = 2
                d += 3
                cy += 1
                cnt += 1

        elif(d % 4 == 2):
            if(map[cy][cx+1] == 1 or map[cy][cx+1] == 2):
                d += 3
            else:
                map[cy][cx+1] = 2
                d += 3
                cx += 1
                cnt += 1

        elif(d % 4 == 1):
            if(map[cy-1][cx] == 1 or map[cy-1][cx] == 2):
                d += 3
            else:
                map[cy-1][cx] = 2
                d += 3
                cy -= 1
                cnt += 1


print(cnt)
