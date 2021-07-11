file_path = r"C:\Users\yz632h\Desktop\CLI_YZ\CLI.txt"


f = open(file_path)

lines = f.read().splitlines()

res = []
for line in lines:
    if line != "":
        res.append(line)

f.close()
print(res)
