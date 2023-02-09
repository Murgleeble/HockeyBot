"""
Visuals uses matplotlib to generate frequency counts of requested NHL player's statistics,
used primarily as a demonstration of my programs working together and also to see a histogram of player performances
"""
masterPath = '/Users/harborwolff/desktop'
import matplotlib.pyplot as plt
import inferential as inf
import lineJudge as lj

name = input("Name: ")
while(name != 'quit'):
    namez = name.split(" ")
    bet = input("What line? ")

    probability = lj.compareH(namez[0], namez[1], float(bet), "S", True)
    if probability == False:
        print("Player File not found!")
        break

    datalist = inf.accessData(namez[0], namez[1])
    

    arr1 = []
    for i in range(0, len(datalist)-1):
        arr1.append(datalist[i][3])

    arr1.sort()

    frequency = {}

    for item in arr1:
        if item in frequency:
            frequency[item] +=1
        else:
            frequency[item] = 1

    arr = list(frequency.values())

    xlist = []
    liner = []
    for i in range(0, len(arr)):
        xlist.append(i)
        liner.append(bet)


    #plt.bar(xlist, arr)
    for i in range(0, len(arr)):
        if(xlist[i] < float(bet)):
            plt.bar([i], arr[i], color = "blue")
        else:
            plt.bar([i], arr[i], color = "red")

    plt.xlim(-1, 15)
    plt.ylim(0, 30)
    plt.text(6, 20, "Hit%: " + str(probability))
    plt.savefig(f'{masterPath}/graphs/{namez[0]}{namez[1]}.png')
    plt.show()
    name = input("Name: ")