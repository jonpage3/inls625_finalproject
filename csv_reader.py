__author__ = 'Jonathon Page, jepage@email.unc.edu, Onyen = jepage'

import csv
import glob

files = glob.glob('data/*.csv')
acc = 2008
for file in files:
    # dictionary of call number classes
    LCC = {'A': ['General Works', 0, 0], 'B': ['Philosophy, Psychology, Religion', 0, 0]
        , 'C': ['Aux Sci History', 0, 0], 'D': ['World History', 0, 0],
           'E': ['American History', 0, 0], 'F': ['Local American History', 0, 0],
           'G': ['Geography, Anth, Recreation', 0, 0], 'H': ['Social Sciences', 0, 0],
           'J': ['Poli Sci', 0, 0], 'K': ['Law', 0, 0], 'L': ['Education', 0, 0],
            'N': ['Fine Arts', 0, 0], 'P': ['Language/Literature', 0, 0],
           'Q': ['Science', 0, 0], 'R': ['Medicine', 0, 0],
           'T': ['Technology', 0, 0], 'U': ['Military Sci', 0, 0], 'V': ['Naval Science', 0, 0],
           'Z': ['Library Science', 0, 0]}
    #fixed encoding problem
    davis_file = open(file,encoding='utf-8')
    davis_reader = csv.reader(davis_file)
    #creates a list of data from csv file
    davis_data = list(davis_reader)

    #takes each row/element in list and
    #sees if call number matches, then adds
    #the last two elements of list
    for row in range(1,len(davis_data)):
        for key in LCC:
            if davis_data[row][0].startswith(key):
                LCC[key][1] += 1
                total_use = int(davis_data[row][1]) + int(davis_data[row][2])
                LCC[key][2] += total_use
    #add rate
    for key in LCC:
        try:
            LCC[key].append(round(LCC[key][1]/LCC[key][2],2))
        except ZeroDivisionError:
            LCC[key].append(0)
    namefile = 'davis_results_' + str(acc) + '.csv'
    output_file = open(namefile,'w',newline='')
    outputWriter = csv.writer(output_file)
    outputWriter.writerow(['Subject','Total Items','Total Usage','Items/Usage Rate'])
    for key in LCC:
        outputWriter.writerow(LCC[key])
    output_file.close()
    acc += 1
    davis_data.clear()









