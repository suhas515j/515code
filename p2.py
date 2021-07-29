if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    l2=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if(i+j+k != n):
                    l1=[]
                    l1.append(i)
                    l1.append(j)
                    l1.append(k)
                    l2.append(l1)
    print(l2)
