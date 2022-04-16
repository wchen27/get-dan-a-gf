from cmath import inf
import csv
import math
import random

f = open('star_data.csv')
csvreader = csv.reader(f)
header = []
header = next(csvreader)
stars = []
for row in csvreader:
    stars.append([math.log(float(row[0])),math.log(float(row[1])),math.log(float(row[2])),float(row[3]),float(row[4])])

def getMeanSquare(sample,star):
    return sum([(sample[i]-star[i])**2 for i in range(4)])

def kmeans(k,stars):
    samples = random.sample(stars, k)
    prev = []
    while prev != samples:
        buckets = []
        for x in range(k):
            buckets.append([])
        for star in stars:
            m = inf
            mSample = []
            for sample in samples:
                if getMeanSquare(sample,star)<m:
                    m = getMeanSquare(sample,star)
                    mSample = sample
            buckets[samples.index(mSample)].append(star)
        means = []
        for bucket in buckets:
            temp = []
            for i in range(4):
                tempAvg = 0
                for star in bucket:
                    tempAvg += star[i]
                temp.append(tempAvg/len(bucket))
            means.append(temp)
        prev = samples
        samples = means
    for i in range(k):
        print("Mean " + str(i) + ": " + str(samples[i]))
        for star in buckets[i]:
            print(str(int(star[4])) + " " + str(star))
        print()

kmeans(6,stars)