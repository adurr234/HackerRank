n=int(input())
d={}
for i in range(n):
    text = input().split()
    d[text[0]] = text[1]


while True:
    try:
        name = input()
        if name in d:
            print("{key}={value}".format(key=name, value=d[name]))
        else:
            print("Not found")
    except:
        break
