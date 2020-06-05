
text = open("Python/Entropy/1984.txt", "r").read()

text_lenght = len(text)

text_lenght_1 = (text_lenght / 2) + (text_lenght % 2)
text_lenght_2 = text_lenght / 2

alphabetta_a = ""
alphabetta_b = ""

alph_a_lenght = 0
alph_b_lenght = 0

array_a = []
array_b = []

def getIndex(symbol, position):
    global alphabetta_a, alphabetta_b
    aplhabetta = ""
    if(position == True):
        aplhabetta = alphabetta_a
    else:
        alphabetta = alphabetta_b
    
    for parser in range(0, len(aplhabetta)):
        t = ""
        t = aplhabetta[parser]

        if symbol == t:
            return parser
    
    return -1

def setAplhabetta(txt, position, lenght):
    global alphabetta_a, alphabetta_b
    begin = 0
    if position == True:
        begin = 0
    else:
        begin = 1
    
    for iterator in range(begin, lenght, 2):
        index = 0
        index = getIndex(text[iterator], position)
        if(index == -1):
            if(position == True):
                alphabetta_a += text[iterator]
            else:
                alphabetta_b += text[iterator]
    return True

def setProbability(txt):
    global alph_a_lenght, alph_b_lenght, array_a, array_b

    alph_a_lenght += len(alphabetta_a)
    alph_b_lenght += len(alphabetta_b)

    for iterator in range(0, alph_a_lenght):
        array_a.append(0)

    for iterator in range(0, alph_b_lenght):
        array_b.append(0)

    for parser in range(0, text_lenght):
        if parser % 2 == 0:
            index = getIndex(text[parser], True)
            if(index >= 0):
                array_a[index] = array_a[index] + 1
        else:
            index = getIndex(text[parser], False)
            if(index >= 0):
                array_b[index] = array_b[index] + 1

result_true  = setAplhabetta(text, True, text_lenght)
result_false = setAplhabetta(text, False, text_lenght)

if result_false == True:
    print("setAlphabetta False...[DONE]")
else:
    print("setAlphabetta False...[SOME ERROR HAS OCCURED]")

setProbability(text)