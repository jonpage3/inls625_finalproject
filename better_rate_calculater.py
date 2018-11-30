__author__ = 'Jonathon Page, jepage@email.unc.edu, Onyen = jepage'

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

#generate the davis_2017 values
davis17file = open('davis_results_2017.csv',encoding='utf-8')
davis17reader = csv.reader(davis17file)
davis17data = list(davis17reader)
davis_2017_acqs = []
for row in range(1,len(davis17data)):
    davis_2017_acqs.append(davis17data[row][1])
print(davis_2017_acqs)

#generate the davis_2017 predictions
davis_2017_predictions = []
davis16file = open('davis_results_2016.csv',encoding='utf-8')
davis16reader = csv.reader(davis16file)
davis16data = list(davis16reader)
acc2 =0
for row in range(1,len(davis16data)):
    davis_2017_predictions.append(round(rate_avg[acc2]*float(davis16data[row][2])))
    acc +=1
print(sum(davis_2017_predictions))

errors = []
for x in range(0,len(davis_2017_predictions)):
    errors.append(abs(int(davis_2017_acqs[x]) - int(davis_2017_predictions[x])))
print(errors)
error_avg = sum(errors)/19
print('Average error: ' + str(error_avg))