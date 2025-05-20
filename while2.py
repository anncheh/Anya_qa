# put your python code here
films = input().split()
i = 0

while i < len(films) and films[i].isalpha():
    print(films[i])
    i += 1

