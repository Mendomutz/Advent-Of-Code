lList = []
rList = []
distance = 0

with open("2024\\1\\input.txt", 'r') as arquivo:
    for linha in arquivo:
        numeros = linha.split()

        lList.append(numeros[0])
        rList.append(numeros[1])

    lList.sort()
    rList.sort()

    for i in range(len(lList)):
        lItem = int(lList[i])
        rItem = int(rList[i])

        distance += abs(lItem - rItem)

    print(distance)

