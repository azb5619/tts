

with open('places.txt','r') as reader:
    for line in reader:
        line = line.split()
        print(line)
        print()
