import random
from math import log
import csv


def get_error(mean, point):
    error = 0
    for i in range(len(mean)):
        error += (mean[i] - point[i])**2
    return error
        

def get_avg(group):
    avg = []
    for i in range(len(group[0])):
        avg.append(0)
    for point in group:
        for i in range(len(point)):
            avg[i] += point[i]
    for i in range(len(avg)):
        avg[i] /= len(group)
    return avg

def k_means(k, points):
    i = 0
    means = random.sample(points, k)
    meanGroups = dict()
    for point in means:
        meanGroups[point] = []

    while True:
        for point in points:
            errors = []
            for mean in means:
                errors.append(get_error(mean, point))
            
            meanGroups[means[errors.index(min(errors))]].append(point)
        
        newMeans = []
        for key in meanGroups:
            newMeans.append(get_avg(meanGroups[key]))
        
        if means == newMeans:
            break

        means = newMeans
        meanGroups = dict()
        for mean in means:
            meanGroups[mean] = []
        i += 1
        
    return meanGroups, i