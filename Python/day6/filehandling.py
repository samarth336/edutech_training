file = open("Python\day6\sample.txt", "r")
content=file.readlines()
for i in content:
    print(f"{i}:{len(i)}")
# print(content)
