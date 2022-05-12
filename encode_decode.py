import random
def rot(string):
    inp = []
    n = len(string)
    a = list(string)
    string1 = ""
    for i in range(0,n):
        b = ord(a[i])
        if b==32:
            rot=32
        elif b>=48 and b<=57:
            rot = ord(str(9-int(chr(b))))
        elif b>=78 and b<=90:
            rot = b-13
        elif b>=110:
            rot=b-13
        else:
            rot = b+13
        can = chr(rot)
        inp.append(can)
    for j in range(0,len(inp)):
        string1 = string1+inp[j]
    return string1

def check_ascii(a):
    for i in range(65,123):
        if i>90 and i<103:
            pass 
        else:
            if a == i:
                flag = 1
                break
            else:
                flag = 0    
    if flag == 1:
        return True
    else:
        return False

def generate_int():
    gen_int = []
    n = random.randint(65,90)
    p = random.randint(103,122)
    gen_int.append(n)
    gen_int.append(p)
    return random.choice(gen_int)

def special_encode(a):
    ref = ['(','~','!','@','#','$','%','&','*',')']
    b = list(a)
    string = ""
    for i in range(0,len(b)):
        asc = ord(b[i])
        lst_asc = list(str(asc))
        for j in range(0,len(lst_asc)):
            ind = lst_asc[j]
            char = ref[int(ind)]
            string = string+char
        string = string+"|"
    return string

def special_decode(a):
    a = a.replace(" ", "")
    ref = ['(','~','!','@','#','$','%','&','*',')']
    b = list(a)
    asc = ""
    string = ""
    for i in range(0,len(b)):
        if b[i] == '|':
            char = chr(int(asc))
            string = string+char
            asc = ""
        else:
            ind = ref.index(b[i])
            asc = asc + str(ind)
    return string

def compress(a):
    string = ""
    i = 0
    while (i < len(a)):
        count=1 
        c = a[i]
        j = i
        while (j<len(a)-1):
            if a[j] == a[j+1]:
                count = count +1
                j = j+1 
            else:
                break
        string = string+c+str(count)
        i = j + 1
    return string.replace("1", "")

def dcompress(a):
    string = ""
    b = list(a)
    j = 0
    for i in range(len(b)):
        if b[i].isdigit()==True:
            while j<int(b[i])-1:
                string = string + b[i-1]
                j = j + 1
        else:
            string = string+b[i]
            j = 0
    return string


def getEncode(a):
    lst = list(a)
    string1 = ""
    for i in range(0,len(lst)):
        ascii_value = ord(lst[i])
        octal_value = oct(ascii_value)
        binary_value = bin(int(str(octal_value).replace("0o","")))
        hex_value = hex(int(str(binary_value).replace("0b","")))
        n = generate_int()
        string1 = string1+(chr(n)+str(hex_value).replace("0x",""))
    string2 = rot(string1 + chr(generate_int()))
    encoded_string = special_encode(string2)
    return compress(encoded_string)

def getDecode(c):
    a = special_decode(dcompress(c))
    b = list(rot(a))
    string = ""
    decoded_string = ""
    string_lst = []
    for i in range(0,len(b)):
        if check_ascii(ord(b[i])) == False:
            string = string + b[i]
        if string != "" and check_ascii(ord(b[i]))==True:
            string_lst.append(string)
            string=""
    for j in range(0,len(string_lst)):
        hexToint = int(string_lst[j],16)
        binToint = int(str(hexToint),2)
        octToint = int(str(binToint),8)
        intToascii = chr(octToint)
        decoded_string = decoded_string+intToascii
    return decoded_string
