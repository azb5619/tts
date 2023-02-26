import math, csv, os


def find_nearest(inputCity, inputState=None):
    big = open('uscities.csv','r')
    small = open('places.txt','r').readlines()
    a = [a.lower().strip().split(',')[1] for a in small]
    noaacities = [[i[0:-2], [b for b in small if i.lower().split(',')[0] in b.lower().strip()]] for i in big if (i.lower().strip().split(',')[0] in a)]
    big = open('uscities.csv','r')

    icity= [i for i in big if i.lower().strip().split(',')[0] == inputCity.strip().lower()][0]
    icitylat = icity.split(',')[1]
    icitylong = icity.split(',')[2]
    shortest_lenght = 9999999
    closest = None
    for i in noaacities:
        tokens = i[0].split(',')
        distance = math.dist([float(tokens[1]),float(tokens[2])],[float(icitylat), float(icitylong)])
        if distance<shortest_lenght:
            shortest_lenght = distance
            closest = i

    return closest

def getImage(closestCity):
    return "https://radar.weather.gov/ridge/standard/"+closestCity[1][0].split(',')[0]+"_loop.gif"

def main():
    os.system('firefox '+getImage(find_nearest(input('what city? '))))


main()
