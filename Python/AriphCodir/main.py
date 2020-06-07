from pandas import DataFrame

msg = "abbbcbb"
chars = []
probs = []
 

left_b  = []
right_b = []

new_left_b =  []
new_right_b = []

probabilities_l = []
probabilities_r = []

decodeProbs = []

codedSequence = 0

def getProbabilities():
    a = 0
    b = 0
    c = 0
    for symbol in msg:
        chars.append(symbol)
    for i in msg:
        prob = round(msg.count(i) / len(msg), 3)

        if i == "a":
            a = prob
            probabilities_l.append(0)
            probabilities_r.append(a)
        if i == "b":
            b =  prob + a
            probabilities_l.append(a)
            probabilities_r.append(b)
        if i == "c":
            c = prob
            probabilities_l.append(b)
            probabilities_r.append(1)

def encode():
    lb = 0
    rb = 0
    chars.clear()
    for char in msg:
        if char in chars:
            continue
        else:
            chars.append(char)
            prob = round(msg.count(char) / len(msg) , 3)
            probs.append(prob)
            left_b.append(lb)
            rb += prob
            right_b.append(rb)
            lb += prob
    
    print("\nTable 1. Symbols and its borders")
    datas = {"char": chars, "probability": probs, "left border": left_b, "right border": right_b}
    df = DataFrame(data=datas)
    print(df)

    chars.clear()
    
    new_lb = 0
    new_rb = 0

    for symbol in msg:
        chars.append(symbol)

    print("\nTable 2. Symbols and its probabilities")
    probsData = {"char": chars, "LB": probabilities_l, "RB": probabilities_r}
    probsDataFrame = DataFrame(data=probsData)
    print(probsDataFrame)

    new_left_b.append(left_b[0])
    new_right_b.append(right_b[0])

    for i in range(len(chars) - 1 ):

        new_lb = round(new_left_b[i] + (new_right_b[i] - new_left_b[i]) * probabilities_l[i+1], 6 )
        new_rb = round(new_left_b[i] + (new_right_b[i] - new_left_b[i]) * probabilities_r[i+1], 6 )
        
        new_left_b.append(new_lb)
        new_right_b.append(new_rb)
    
    print("\nTable 3. Encoding symbols")
    encodeData = {"char": chars, "LB" : new_left_b, "RB" : new_right_b}
    encodeDataFrame = DataFrame(data=encodeData)
    print(encodeDataFrame)

    codedSequence = new_left_b[-1]
    print("Coded sequence = " + str(codedSequence))

def decode():
    dec_int = 0
    decodeProbs.append(new_left_b[-1])
    for i in range(len(chars) - 1):
        dec_int = round((decodeProbs[i] - probabilities_l[i]) / (probabilities_r[i] - probabilities_l[i]) , 6)
        decodeProbs.append(dec_int)
    print("\nTable 4. Decoding")
    data = {"Decoding" : decodeProbs, "LB": probabilities_l, "RB" : probabilities_r, "Char": chars}
    datas = DataFrame(data=data)
    print(datas)

print("\ninput message: " + msg)
getProbabilities()
encode()
decode()

