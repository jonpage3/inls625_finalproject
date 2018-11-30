__author__ = 'Jonathon Page, jepage@email.unc.edu, Onyen = jepage'

#weighted rate calculator but for 2013-14 predictions

#rate calculator using weighted average
import glob
import csv

files2 = glob.glob('*.csv')
rate_values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#this adds of up the total
#rate values and collects
#them in a list called rate_values
w_acc = 10
for file in files2:
    result_file = open(file,encoding='utf-8')
    result_reader = csv.reader(result_file)
    result_data = list(result_reader)
    acc = 0
    for row in range(1,len(result_data)):
        rate_values[acc] += float(result_data[row][3]) * w_acc
        acc +=1
    w_acc -= 1
print(rate_values)
#collect a list of rate averages
rate_avg = []
#calculate average rate_values
for x in range(0,len(rate_values)):
    rate_avg.append(round(rate_values[x]/10,2))
print(rate_avg)

#generate the davis_2013 values
davis13file = open('davis_results_2013.csv',encoding='utf-8')
davis13reader = csv.reader(davis13file)
davis13data = list(davis13reader)
davis_2013_acqs = []
for row in range(1,len(davis13data)):
    davis_2013_acqs.append(davis13data[row][1])
print(davis_2013_acqs)

#generate the davis_2013 predictions
davis_2013_predictions = []
davis12file = open('davis_results_2012.csv',encoding='utf-8')
davis12reader = csv.reader(davis12file)
davis12data = list(davis12reader)
acc2 =0
for row in range(1,len(davis12data)):
    davis_2013_predictions.append(round(rate_avg[acc2]*float(davis12data[row][2])*0.35))
    acc +=1
print(davis_2013_predictions)

errors = []
for x in range(0,len(davis_2013_predictions)):
    errors.append(abs(int(davis_2013_acqs[x]) - int(davis_2013_predictions[x])))
print(errors)
error_avg = sum(errors)/19
print('Average error: ' + str(error_avg))