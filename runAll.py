"""
Run All looks at the JSON file 'dailyLines.json' and generates value calculations (printed to the terminal) for each line stored there
"""
masterPath = '/Users/harborwolff/desktop'
import json
import lineJudge as lj
import inferential as inf
from colorama import Fore

def output():
     filePath = f"{masterPath}/project/jsons/dailyLines.json"
     with open(filePath, 'r') as j:
          contents = json.loads(j.read())

     for item in contents:
          #print(item['name'].split(' ')[0] + ' ' + item['name'].split(' ')[1] + ' ' + str(item['shots']))
          prob = lj.compareH(item['name'].split(' ')[0], item['name'].split(' ')[1], float(item['shots']), 'S', True)
          if prob == False:
               print("Skipped player: " + item['name'].split(' ')[1] + ".")
          else:
          #"""
               datalist = inf.accessData(item['name'].split(' ')[0], item['name'].split(' ')[1])

               arr1 = []
               for i in range(0, len(datalist)-1):
                    arr1.append(datalist[i][3])

               arr1.sort()

               frequency = {}

               for thing in arr1:
                    if thing in frequency:
                         frequency[thing] +=1
                    else:
                         frequency[thing] = 1

               nSum = 0
               dSum = 0
               
               for i in frequency.keys():
                    if float(i) >= float(item['shots']):
                         nSum += int(frequency[i])
                    dSum += int(frequency[i])
               
               complex = round(prob, 3)
               simple = round(nSum/dSum, 3)
               print(Fore.RED + item['name'].split(' ')[1] + ' at '+ item['shots'] +': ') 
               if complex > .6 and complex < .657:
                    print(Fore.YELLOW + '\tComplex: ' + str(complex))
               elif complex > .657:
                    print(Fore.BLUE + '\tComplex: ' + str(complex))
               else:
                    print(Fore.WHITE + '\tComplex: ' + str(complex))
               if simple > .6 and simple < .657:
                    print(Fore.YELLOW + '\tSimple: ' + str(simple))
               elif simple > .657:
                    print(Fore.BLUE + '\tSimple: ' + str(simple))
               else:
                    print(Fore.WHITE + '\tSimple: ' + str(simple))    
               if round((simple+complex)/2, 6) > .6 and round((simple+complex)/2, 6) < .657:
                    print(Fore.YELLOW + '\tMean: ' + str(round((simple+complex)/2, 6)))
               elif round((simple+complex)/2, 6) > .657:
                    print(Fore.BLUE + '\tMean: ' + str(round((simple+complex)/2, 6)))
               else:
                    print(Fore.WHITE + '\tMean: ' + str(round((simple+complex)/2, 6)))
