import math





if __name__ == '__main__':
    
    # while True:
        
    #     s = input().split(' ')
    #     if not s[0] :
    #         break
    #     x,y = 0,0
    #     direct = s[0]
    #     steps = s[1]
    #     if direct == 'UP':
    #         y = y + int(steps)
    #     elif direct == 'DOWN':
    #         y  = y - int(steps)
    #     elif direct == 'RIGHT':
    #         x = x + int(steps)
    #     elif direct == 'LEFT':
    #         x = x - int(steps)
        
    # print(x,y)
    # print(round(math.sqrt(x**2 + y**2)))

    x,y=0,0
    while True:
        s = input()
        if not(s):
            break
        if 'UP' in s:
            print("UP")
            y = y+int(s.strip('UP '))
        elif 'DOWN' in s:
            y = y-int(s.strip('DOWN '))
            print("down")
        elif 'LEFT' in s:
            x = x+int(s.strip('LEFT '))
            print("left")
        elif 'RIGHT' in s:
            x = x-int(s.strip('RIGHT '))
    print(round(math.sqrt(x**2 + y**2)))

