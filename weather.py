import math, csv

def find_nearest():
    with open('places.txt','r') as reader:
        for line in reader:
            line = line.split()
            print(line)
