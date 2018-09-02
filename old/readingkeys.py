with open("keys.txt", "r") as f: #w for write, r+ for read and write
    for line in f:
        list = line.split(":")
        key = list[0]
    print(list)
