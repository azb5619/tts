import math, csv


def find_nearest(inputCity):
    with open('uscities.csv','r') as big:
        with open('places.txt','r') as small:
            a = [a.lower().strip().split(',')[1] for a in small]
            b = [i[0:-2] for i in big if (i.lower().strip().split(',')[0] in a)]
            
            print(b)

def main():
    find_nearest('charlotte')


main()
