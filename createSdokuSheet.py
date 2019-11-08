import random

DIR = "C:/Users/junwh/Desktop/"
THRESHOLD = 100000  

def getBox():
	returnArr = []
	scoreArr = [1,2,3,4,5,6,7,8,9]
	i = 0
	while len(scoreArr):
		idx=random.randint(0, len(scoreArr)-1)
		if i%3==0:
			returnArr.append([])	
		returnArr[(i//3)].append(scoreArr[idx])
		del(scoreArr[idx])
		i+=1
	return returnArr

def checkTwoBox(box1, box2, vh):
	if vh == 1: #vertical
		for i in range(0,3):
			temp1 = [box1[0][i], box1[1][i], box1[2][i]]
			temp2 = [box2[0][i], box2[1][i], box2[2][i]]
			for el1 in temp1:
				for el2 in temp2:
					if el1==el2:
						return False
	elif vh ==0: #horizontal
		for i in range(0,3):
			temp1 = [box1[i][0], box1[i][1], box1[i][2]]
			temp2 = [box2[i][0], box2[i][1], box2[i][2]]
			for el1 in temp1:
				for el2 in temp2:
					if el1==el2:
						return False
	return True

def changeDimension(matrix):
	newMatrix = []
	
	for i in range(0,3):
		for j in range(0,3):
			line = []
			for k in range(0,3):
				line.extend(matrix[i][k][j])
			newMatrix.append(line)
	return newMatrix

def shufle(changedMatrix, n):
	matrixTemp = changedMatrix
	for i in range(n):
		vh = random.randint(0,1)		
		groupRand = 3*random.randint(0,2)
		r1 = groupRand+random.randint(0,2)
		r2 = groupRand+random.randint(0,2)	
		if vh:
			tempLine = matrixTemp[r1]
			matrixTemp[r1] = matrixTemp[r2]
			matrixTemp[r2] = tempLine
		else:
			for i in range(9):
				tempNum = matrixTemp[i][r1]
				matrixTemp[i][r1] = matrixTemp[i][r2]
				matrixTemp[i][r2] = tempNum	
	return matrixTemp
def saveSdoku(matrix, fileStream, index):
    f.write((str(index)+".\n").encode())
    for line in matrix:
        for num in line:
            f.write(str(num).encode())
        f.write("\n".encode())
    f.write(" \n".encode())
index = 1
while True:
    f = open(DIR+"sdokus.txt","ab")
    matrix = [[getBox(),[],[]],[[],[],[]],[[],[],[]]]
    flag = False
    boxes = []
    for i in range(THRESHOLD):
        boxes.append(getBox())	
    
    for box in boxes:
        if checkTwoBox(box, matrix[0][0], 1):
            matrix[1][0] = box
            flag = True
            break
    if not flag:
        print("re-building...")
        continue
    else:
        flag=False

    for box in boxes:
        if checkTwoBox(box, matrix[0][0], 0):
            matrix[0][1] = box
            flag = True
            break
    if not flag:
        print("re-building...")
        continue
    else:
        flag=False

    for box in boxes:
        if checkTwoBox(box, matrix[0][1], 1) and checkTwoBox(box, matrix[1][0], 0):
            matrix[1][1] = box
            flag = True
            break
    if not flag:
        print("re-building...")
        continue
    else:
        flag=False

    for box in boxes:
        if checkTwoBox(box, matrix[0][0], 1) and checkTwoBox(box, matrix[1][0], 1):
            matrix[2][0] = box
            flag = True
            break
    if not flag:
        print("re-building...")
        continue
    else:
        flag=False

    for box in boxes:
        if checkTwoBox(box, matrix[2][0], 0) and checkTwoBox(box, matrix[0][1], 1) and checkTwoBox(box, matrix[1][1], 1):
            matrix[2][1] = box
            flag = True
            break
    if not flag:
        print("re-building...")
        continue
    else:
        flag=False

    for box in boxes:
        if checkTwoBox(box, matrix[2][0], 0) and checkTwoBox(box, matrix[2][1], 0):
            matrix[2][2] = box
            flag = True
            break
    if not flag:
        print("re-building...")
        continue
    else:
        flag=False

    for box in boxes:
        if checkTwoBox(box, matrix[1][0], 0) and checkTwoBox(box, matrix[1][1], 0) and checkTwoBox(box, matrix[2][2], 1):
            matrix[1][2] = box
            flag = True
            break
    if not flag:
        print("re-building...")
        continue
    else:
        flag=False
    for box in boxes:
        if checkTwoBox(box, matrix[0][0], 0) and checkTwoBox(box, matrix[0][1], 0) and checkTwoBox(box, matrix[1][2], 1) and checkTwoBox(box, matrix[2][2], 1):
            matrix[0][2] = box
            flag = True
            break
    if not flag:
        print("re-building...")
        continue
    else:
        flag=False
	
    print("processing...")
    matrix = changeDimension(matrix)
	
    for i in range(100):
        saveSdoku(shufle(matrix, 10),f,index)
        index+=1
    f.close()