alpha = tuple("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890?!.,()@#%-+/=")
mod = input("input mod [E/D]:    ")
if mod != "E" and mod != "D":
    print("Not correct mode!")
    exit(0)
message = input("input message:    ")
print("Your key must have len(S matrix * S matrix)!!!") # Ключ должен иметь длину - площадь матрицы умноженная на площадь матрицы.
key = input("input key:    ")
lenmatrix = 3 # площадь матрицы, в данном случае 3 на 3.

message = message.upper()
for p in range(len(message)-1): # Если в сообщении есть символ которого нет в алфавите: удалить этот символ.
    if message[p] not in alpha:
        message = message.replace(message[p],"")

while len(message) % lenmatrix != 0: # Если длина сообщения не кратна площади матрицы будет добавлен последний символ в конец сообщения.
    message += message[-1]

def Ln(message,lenmatrix): # Создадим список и впишем туда по ((три буквы)в данном случае. Если матрица будет 4 на 4 то по 4) от сообщения.
    list1 = []
    message = message.upper()
    le = len(message) / lenmatrix
    le = int(le)
    i = 0
    l = 0
    j = lenmatrix
    while i != le:
        list1.append(message[l:j])
        l += lenmatrix
        j += lenmatrix
        i+=1
    return list1

def Appender(text): # Создаем матрицу из символов (сообщения длиною в площадь матрицы).
    matrix = []
    for three in text:
        matrix.append(list(three))
    return Coder(matrix)

def Coder(matrix): # Перевести буквы в символы по алфавиту.
    for x in range(len(matrix)):
        for y in range(lenmatrix):
            matrix[x][y] = alpha.index(matrix[x][y])
    return matrix

def M(i,j): # Находим М.
    timeM = []
    m = []
    n = 0
    for o in range(lenmatrix-1):
        m.append([0]*2)
    for x in range(len(matrixKey)):
        for y in range(lenmatrix):
            if x != i and y != j:

                timeM.append(matrixKey[x][y])

    for x in range(len(m)):
        for y in range(len(m)):
            m[x][y] = timeM[n]
            n += 1

    x = 0
    y = 0
    finelM = m[x][y] * m[x+1][y+1] - m[x+1][y] * m[x][y+1]
    return finelM

def A(): # Алгебраическое выражение.
    a = []
    for i in range(lenmatrix):
        a.append([0] * lenmatrix)
    for x in range(lenmatrix):
        for y in range(lenmatrix):
            m = M(x,y)
            a[y][x] = ((-1) ** (x+1 + y+1)) * m
    return a

def modedA(): # Алгебраическое выражение по модулю числа алфавита.
    global a
    a = A()
    for x in range(lenmatrix):
        for y in range(lenmatrix):
            a[y][x] = a[y][x] % len(alpha)
    return a

def cA(): # Умножим алгебраическое выражение по модулю на обратное число к определителю матрицы и поделим по модулю альфа.
    a = modedA()
    for x in range(lenmatrix):
        for y in range(lenmatrix):
            a[x][y] = a[x][y] * teorF
            a[x][y] = a[x][y]%len(alpha)
    return a

def encode(codmess,codkey,finely=""): # Кодирование/Декодирование.
    encodedMatrix = []
    for h in range(len(codmess)):
        coded = [0 for o in range(lenmatrix)]
        for x in range(lenmatrix):
            for y in range(lenmatrix):
                coded[x] += codkey[x][y]*codmess[h][y]
            coded[x] = coded[x] % len(alpha)
            coded[x] = alpha[coded[x]]
        encodedMatrix.append(coded)
    for i in encodedMatrix:
        finely += "".join(i)
    return finely

matrixMess = Appender(Ln(message,lenmatrix)) # Обработанное сообщение.
matrixKey = Appender(Ln(key,lenmatrix)) # Обработанный ключ.


C = encode(matrixMess,matrixKey) # Закодированное сообщение.
Cint = Appender(Ln(C,lenmatrix)) # Перевести в матрицу с числами закодированное сообщение.

tk = A()[0][0]*matrixKey[0][0]+A()[1][0]*matrixKey[0][1]+A()[2][0]*matrixKey[0][2] # --------
tk = tk%len(alpha) # -------------------------------------------------- Определитель матрицы.

teorF = (tk**(len(alpha)-2))%len(alpha) # Обратное число к определителю матрицы.

if mod == "E":
    print(C)
if mod == "D":
    print(encode(matrixMess, cA()))