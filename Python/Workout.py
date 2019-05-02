# -*- coding: utf-8 -*-

# Workout Generator by VMoza

# General imports
import pandas as pd
import numpy as np
import statistics as s
import csv
import random
from pandas import *
import pprint as p

# The Workout
workout = [[],[]]

# Drawing file data
file = pd.ExcelFile("/Users/VMoza/desktop/Cal/Projects/FitUp/WorkoutPlan.xlsx")
sheet = file.parse('Sheet1')
datas = pd.DataFrame(sheet)

# Calculating general information (# of rows, # of columns) and column names
shape = datas.shape
cols = list(datas)

# Redefining each individual column of the original excel sheet
bicepsEx = datas[cols[0]]
bicepsSets = datas[cols[1]]
bis = [bicepsEx, bicepsSets]

tricepsEx = datas[cols[2]]
tricepsSets = datas[cols[3]]
tris = [tricepsEx, tricepsSets]

forearmsEx = datas[cols[4]]
forearmsSets = datas[cols[5]]
fores = [forearmsEx, forearmsSets]

chestEx = datas[cols[6]]
chestSets = datas[cols[7]]
chest = [chestEx, chestSets]

backEx = datas[cols[8]]
backSets = datas[cols[9]]
back = [backEx, backSets]

shouldersEx = datas[cols[10]]
shouldersSets = datas[cols[11]]
shoulds = [shouldersEx, shouldersSets]

legsEx = datas[cols[12]]
legsSets = datas[cols[13]]
legs = [legsEx, legsSets]

# Master Workouts
push = [chest, tris, shoulds]
pull = [back, bis, fores]
leg = [legs]
master = [push, pull, leg]

# Time Helper Method
def genTime(time, n):
    return (int)((time / 7) / n)

# Dual-Array Randomizer Helper Method
def rand(exNsets):
    exTemp = exNsets[0]
    setsTemp = exNsets[1]
    
    ex = list(filter(lambda v: v==v, exTemp))
    sets = list(filter(lambda v: v==v, setsTemp))
    
    c = list(zip(ex, sets))
    random.shuffle(c)
    ex, sets = zip(*c)
    
    return [ex, sets]

# Array Cutter Helper Method
def arrCut(arr, n):
    return [arr[0][:n], arr[1][:n]]

# Exercise Generator Method
def genEx(group, time):
    global workout
    sub = 0
    while (sub < len(master[group])):
        ex = master[group][sub]
        newTime = genTime(time, len(master[group]))
        add = arrCut(rand(ex), newTime)
        workout[0] = np.append(workout[0], add[0])
        workout[1] = np.append(workout[1], add[1])
        sub += 1

# Workout Generator Method
def genWorkout(work, time):
    global workout
    workout = [[], []]
    if (work == 0):
        genEx(0, time)
    elif (work == 1):
        genEx(1, time)
    elif (work == 2):
        genEx(2, time)
    else:
        print("Invalid Entry")
    p()
        
# Adds a Random Exercise (UNFINISHED)
def addEx(muscle):
    global workout
    rand = random.randint(1, 10)
    workout = np.append(workout, rand)
    
# Simple Print Helper Method
def p():
    print(np.c_[workout[0], workout[1]])
    print("\n")
    
# Simple Workout Creator
def g(ppl, t):
    if ppl == "Push" or ppl == "push":
        return genWorkout(0, t)
    elif ppl == "Pull" or ppl == "pull":
        return genWorkout(1, t)
    elif ppl == "Legs" or ppl == "legs":
        return genWorkout(2, t)
    return genWorkout(ppl, t)

# Creates Workout for All Muscles
def a(t):
    for x in range(3):
        g(x, t)

# create a way to make sure truly random each time

# Enter "Push" / "Pull" / "Legs" or 0 / 1 / 2
workoutDesired = "Push"
workoutMinutes = 60
g(workoutDesired, workoutMinutes)