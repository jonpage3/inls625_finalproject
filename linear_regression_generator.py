__author__ = 'Jonathon Page, jepage@email.unc.edu, Onyen = jepage'

import csv
import glob

files = glob.glob('*.csv')
LCC = {'General Works':[], 'Philosophy, Psychology, Religion':[],
         'Aux Sci History': [],'World History':[],
           'American History':[],'Local American History':[],
           'Geography, Anth, Recreation':[],'Social Sciences':[],
           'Poli Sci':[], 'Law':[], 'Education': [],
            'Fine Arts':[], 'Language-Literature':[],
           'Science':[], 'Medicine':[],
           'Technology':[], 'Military Sci':[], 'Naval Science':[],
           'Library Science':[]}

for key in LCC:
    acc = 2008
    for file in files:
        dfile = open(file,encoding='utf-8')
        dfile_reader = csv.reader(dfile)
        davis_data = list(dfile_reader)
        for x in davis_data:
            if key == x[0]:
                LCC[key].append([acc,x[1],x[2]])
        acc += 1
        davis_data.clear()

for key in LCC:
    namefile = key + '.csv'
    output_file = open(namefile, 'w', newline='')
    outputWriter = csv.writer(output_file)
    outputWriter.writerow(['Year','Items acquired','Times used'])
    for row in LCC[key]:
        outputWriter.writerow(row)
    output_file.close()
