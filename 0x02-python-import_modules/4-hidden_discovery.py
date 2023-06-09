#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hd
    listm = dir(hd)
    for i in range(len(listm)):
        if listm[i][0] != "_" and listm[i][1] != "_":
            print (listm[i])
