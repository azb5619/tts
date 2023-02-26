import math, csv, os


def find_nearest(inputCity):
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


def find_nearest_states(inputCity, inputState=None):
    big = csv.reader(open('bigcitylist.csv'))
    small = open('places.txt','r').readlines()
    noaa_city_names = [[a.lower().strip().split(',')[1], a.split(',')[2][0:-1]] for a in small]

    #noaacities = [[i, [b[0:-1] for b in small if i[3].lower().strip() in b.lower().strip()]] for i in big if ([i[3].lower().strip(), i[1]] in [[a[1].lower().strip(), a[2]] for a in small])]

    #i[3].lower.strip() == big name
    #i[1] == big state
    #a[1].lower.strip == small name
    #a[2] == small state
    #i big state + location

    noaacities = [[i, [noaa[0:-1] for noaa in small if [i[3].lower().strip(), i[1]] in [[a[1].lower().strip(), a[2]] for a in small]]] for i in big] #if ([i[3].lower().strip(), i[1]] in [[a[1].lower().strip(), a[2]] for a in small])]

    for i in big:
        #small arry
        if i in smallarry:
            ret += i

    

    print(noaacities)

    big = csv.reader(open('bigcitylist.csv'))
    icity = [i for i in big if i[3].lower().strip() == inputCity.strip().lower() and (bool(i[1].lower().strip() == inputState.lower().strip()) if inputState else True)][0]

    icitylat = icity[5]
    icitylong = icity[6]
    shortest_lenght = 9999999
    a,b = 0,0
    closest = None
    for i in noaacities:
        tokens = i[0] + i[1]
        distance = math.dist([float(tokens[5]),float(tokens[6])],[float(icitylat), float(icitylong)])
        print(tokens[1], " ", icity[1])
        if tokens[1] == icity[1] and distance<shortest_lenght:
            shortest_lenght = distance
            a,b=tokens[5],tokens[6]
            closest = i
    print(icity)
    print(icitylat, icitylong)
    print(shortest_lenght)
    print(closest)
    return closest

def getImage(closestCity):
    return "https://radar.weather.gov/ridge/standard/"+closestCity[1][0].split(',')[0]+"_loop.gif"

if __name__ == "__main__":
    a, b = input("city ").split()
    os.system('firefox '+getImage(find_nearest_states(a,b)))
