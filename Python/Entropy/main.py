
from math import log2

#text = open("Python/Entropy/1984.txt", "r").read()
text = "aaaaaaaaasdasvasasassa sadsa dsadasda a"
text_lenght = len(text)

text_lenght_1 = (text_lenght / 2) + (text_lenght % 2)
text_lenght_2 = text_lenght / 2

alphabetta_a = ""
alphabetta_b = ""

alph_a_lenght = 0
alph_b_lenght = 0

array_a = []
array_b = []

probability_array = []

def getIndex(symbol, position):
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
    #print("N2 = " + str(alphabetta_b))
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
        index = getIndex(text[iterator], position)
        ####
        #print(index)
        if(index == -1):
            if(position == True):
                alphabetta_a += text[iterator]
            else:
                alphabetta_b += text[iterator]
    #print("N2 = " + str(alph_b_lenght))
    print("Done")
    return True

def setProbability(txt, prob_arr,arr_a, arr_b):
    global alph_a_lenght, alph_b_lenght

    alph_a_lenght += len(alphabetta_a)
    alph_b_lenght += len(alphabetta_b)
    #print("N2 = " + str(alph_b_lenght))

    for iterator in range(0, alph_a_lenght):
        arr_a.append(0)

    for iterator in range(0, alph_b_lenght):
        arr_b.append(0)

    for parser in range(0, text_lenght):
        if parser % 2 == 0:
            index = getIndex(text[parser], True)
            if(index >= 0):
                arr_a[index] +=  1
        else:
            index = getIndex(text[parser], False)
            if(index >= 0):
                arr_b[index] += 1
    
    #prob
    for row in range(alph_a_lenght):
        prob_arr.append([])
        for column in range(alph_b_lenght):
            prob_arr[row].append(0)
    
    current_row    = 0
    current_column = 0
    for iterator in range(0, (text_lenght - 1), 2):
        current_row    = getIndex(text[iterator], True)
        current_column = getIndex(text[iterator + 1], False)
        prob_arr[current_row][current_column] += 1
        print(prob_arr[current_row][current_column])

def Entropy():
    SchennonEntropyFirst = 0
    prob = 0
    for iterator in range(alph_a_lenght):
        prob = array_a[iterator] / text_lenght_1
        SchennonEntropyFirst += (-1) * prob * log2(prob)
    
    print("test")
    SchennonEntropySecond = 0
    for iterator in range(alph_b_lenght):
        prob = array_b[iterator] / text_lenght_2
        print(array_b[iterator])
        SchennonEntropySecond += (-1) * prob * log2(prob)
    print("end")
    SchennonEntropyTotal = SchennonEntropyFirst + SchennonEntropySecond

    print("H (thirdparty source) = " + str(SchennonEntropyTotal))

result_true  = setAplhabetta(text, True,  text_lenght)
result_false = setAplhabetta(text, False, text_lenght)

if result_false == True:
    print("setAlphabetta False...[DONE]")
else:
    print("setAlphabetta False...[SOME ERROR HAS OCCURED]")

print(text_lenght)
setProbability(text, probability_array, array_a, array_b)
print(array_a)
print(array_b)
Entropy()
