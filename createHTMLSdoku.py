import random
import os

DIR = "C:/Users/junwh/Desktop/"

def add(S, x):
	return S|2**x
def check(S, x):
	return (S>>x)%2
def remove(S, x):
	if check(S, x):
		return S-(2**x)
	return S
def toggle(S, x):
	if check(S, x):
		return remove(S, x)
	else:
		return add(S,x)
 
f = open(DIR+"sdokus.txt",'r')
sdokuTxt = f.read().split("\n")
f.close()
for num in range(1, 5401):
    bitmask = [0b111111111, 0b111111111, 0b111111111,
    0b111111111, 0b111111111, 0b111111111,
    0b111111111, 0b111111111, 0b111111111,
    0b111111111, 0b111111111, 0b111111111,
    0b111111111, 0b111111111, 0b111111111,
    0b111111111, 0b111111111, 0b111111111,
    0b111111111, 0b111111111, 0b111111111,
    0b111111111, 0b111111111, 0b111111111,
    0b111111111, 0b111111111, 0b111111111,]
    matrix = []
    flag = False
    for line in sdokuTxt:
        if line==(str(num)+'.'):
            flag = True
        elif flag:
            if line!=(str(num+1)+'.'):
                matrix.append(list(line))
            else:
                del matrix[-1]
                flag = False   
                break
    for i in range((50+(num//100))):
        x = random.randint(0,8)
        y = random.randint(0,8)
        bitmask[x] = remove(bitmask[x],y)

    os.system('mkdir C:\\users\\junwh\\desktop\\sdokus\\'+str(num)+'th')
    sdoku = open(DIR+'sdokus/'+str(num)+'th/'+str(num)+'th sdoku.html','w')
    result = open(DIR+'sdokus/'+str(num)+'th/'+str(num)+'th result.html','w')

    sdoku.write('<html><head><style>')
    result.write('<html><head><style>')

    sdoku.write('h1{text-decoration:solid;text-align:center;text-size:50px}')
    result.write('h1{text-decoration:solid;text-align:center;text-size:50px}')

    sdoku.write('table{background-color:black;margin:auto;margin-top:20px}')
    result.write('table{background-color:black;margin:auto;margin-top:20px}')

    sdoku.write('td table{margin: 0px !important}')
    result.write('td table{width: 90px; height: 90px;margin: 0px !important}')

    sdoku.write('td{width:inherit;height:inherit;!imortant;padding:0px !important;background-color: white;border-color:black;width:30px;height:30px;text-align:center;}') 
    result.write('td{width:inherit!important;height:inherit !important;!imortant;padding:0px !important;background-color: white;border-color:black;width:30px;height:30px;text-align:center;}') 

    sdoku.write('input{width:inherit;height:inherit;text-align:center;font-size:normal;border-color:white;border-style:none;color:blue;}')
    result.write('input{width:inherit;height:inherit;text-align:center;font-size:normal;border-color:white;border-style:none;color:blue;}')

    sdoku.write('</style></head>')
    result.write('</style></head>')

    sdoku.write('<body><h1>'+str(num)+"th Sdoku"+'</h1><table>')
    result.write('<body><h1>'+str(num)+"th Result"+'</h1><table>')

    for i in range(3):
        sdoku.write('<tr>')
        result.write('<tr>')
        for j in range(3):
            sdoku.write('<td><table>')
            result.write('<td><table>')
            for k in range(3):
                sdoku.write('<tr>')
                result.write('<tr>')
                for l in range(3):
                    x = 3*j+l
                    y = 3*i+k
                    if check(bitmask[x],y):
                        sdoku.write('<td>'+matrix[x][y]+'</td>')
                        result.write('<td>'+matrix[x][y]+'</td>')

                    else:
                        sdoku.write('<td><input/></td>')
                        result.write('<td style="color:red!important;">'+matrix[x][y]+'</td>')       
                sdoku.write('</tr>')
                result.write('</tr>')
            sdoku.write('</table></td>')
            result.write('</table></td>')
        sdoku.write('</tr>')
        result.write('</tr>')
    sdoku.write('</table></body></html>')
    result.write('</table></body></html>')

    sdoku.close()
    result.close()





