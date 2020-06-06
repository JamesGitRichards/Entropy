
# -*- coding: utf-8 -*-
from math import log2
from pandas import DataFrame

text = open("Path", "r").read()
text_lenght = len(text)

text_lenght_1 = (text_lenght / 2) + (text_lenght % 2)
text_lenght_2 = text_lenght / 2

alphabetta_a = ""
alphabetta_b = ""

alph_a_lenght = 0
alph_b_lenght = 0

array_a           = []
array_b           = []
probability_array = []

Hts = 0
H   = 0


def getRealPoint(symbol, position):
    global alphabetta_a, alphabetta_b
    aplhabetta = ""
    
    if(position == True):
        aplhabetta = alphabetta_a
    else:
        aplhabetta = alphabetta_b
        
    for parser in range(0, len(aplhabetta)):
        t = ""
        t = aplhabetta[parser]
        if symbol == t:
            return parser

    return -1

def setAplhabetta(txt, position, lenght):
    global alphabetta_a, alphabetta_b
    begin = 1

    if position == True:
        begin = 0
    else:
        begin = 1
    
    for iterator in range(begin, lenght, 2):
        index = 0
        index = getRealPoint(text[iterator], position)
        if(index == -1):
            if(position == True):
                alphabetta_a += text[iterator]
            else:
                alphabetta_b += text[iterator]

def setProbability(txt, prob_arr,arr_a, arr_b):
    global alph_a_lenght, alph_b_lenght

    alph_a_lenght += len(alphabetta_a)
    alph_b_lenght += len(alphabetta_b)

    for iterator in range(0, alph_a_lenght):
        arr_a.append(0)

    for iterator in range(0, alph_b_lenght):
        arr_b.append(0)

    for parser in range(0, text_lenght):
        if parser % 2 == 0:
            index = getRealPoint(text[parser], True)
            if(index >= 0):
                arr_a[index] += 1
        else:
            index = getRealPoint(text[parser], False)
            if(index >= 0):
                arr_b[index] += 1
    
    for row in range(alph_a_lenght):
        prob_arr.append([])
        for column in range(alph_b_lenght):
            prob_arr[row].append(0)
    
    current_row    = 0
    current_column = 0

    for iterator in range(0, (text_lenght - 1), 2):
        current_row    = getRealPoint(text[iterator], True)
        current_column = getRealPoint(text[iterator + 1], False)
        prob_arr[current_row][current_column] += 1

def Entropy(prob_arr, arr_a):
    global Hts, H
    SchennonEntropyFirst  = 0
    SchennonEntropySecond = 0
    prob = 0
    for iterator in range(alph_a_lenght):
        prob = array_a[iterator] / text_lenght_1
        SchennonEntropyFirst += (-1) * prob * log2(prob)
    
    for iterator in range(alph_b_lenght):
        prob = array_b[iterator] / text_lenght_2
        SchennonEntropySecond += (-1) * prob * log2(prob)
    Hts += round(SchennonEntropyFirst + SchennonEntropySecond, 3)

    #print("H (thirdparty source) = " + str(round( SchennonEntropyTotal, 3)))

    value = 0
    pairs = text_lenght / 2 
    for rows in range(alph_a_lenght):
        var = 0
        for columns in range(alph_b_lenght):
            iterator_prob  = prob_arr[rows][columns] / pairs
            iterator_prob /=  (arr_a[rows] / text_lenght_1)
            if prob_arr[rows][columns] != 0:
                var += -1 * iterator_prob * log2(iterator_prob)
            
        value += (arr_a[rows] / text_lenght_1) * var
    
    H = round(SchennonEntropyFirst + value, 3)

    #print("H = " + str(round(H, 3)))

def main():
    
    setAplhabetta(text, True,  text_lenght)
    setAplhabetta(text, False, text_lenght)

    setProbability(text, probability_array, array_a, array_b)
    Entropy(probability_array, array_a)

    datas = {"Энтропия источника независимых сообщений" : [Hts], "Энтропия" : [H]}
    df = DataFrame(data=datas)
    print(df)

main()