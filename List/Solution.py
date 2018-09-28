if __name__ == '__main__':
    l=[]
    for var in range(int(input())):
        data=input().split()
        if data[0] == "print":
            print (l)
        elif data[0] == "insert":
            l.insert(int(data[1]),int(data[2]))           
        elif data[0] == "remove":
            l.remove(int(data[1]))
        elif data[0]== "sort" :
            l.sort()
        elif data[0] == "append" :
            l.append(int(data[1]))
        elif data[0] == "pop":
            l.pop()
        elif data[0] ==  "reverse":
            l.reverse()
        else:
            break