from numpy import matrix
from numpy import linalg
from time import sleep
import math

#Lavet på baggrund af algoritmen, der er beskrevet i artiklen:
#Algebraic computations with continued fractions af Pierre Liardet og Pierre Stambul i J. Number Theory 73 (1998), no. 1, s. 92-121.

#Interessante konstanter
#Kvadratroden af phi: [1;3,1,2,11,3,5,1,10,1,2,5,3]
#x = [1,3,1,2,11,3,5,1,10,1,2,5,3]
#Kvadratroden af 2: [1;2,2,2,2,2,2,2,2]
#Kvadratroen af pi: 
x =[1,1,3,2,1,1,6,1,28]
#x = [1,1,3,2,1,1,6,1,28]
#Hvis vi vil vælge selv:
#x = [int(y) for y in input("Skriv kædebrøk ").split()]

print ("x ser ud på formen "+str(x))
x_squared = []

B = matrix([[1,0,0,0],[0,0,0,1]])
C = matrix([[1,0],[0,1]])

#Hvis alle tællerne er større end alle nævnerne i matrixen (eller omvendt) er den i D_4 eller D_4'. Hvis ikke er den i E_4
def is_matrix_in_e(M):
	if (M.item(0,0) > M.item(1,0) and (M.item(0,1) < M.item(1,1) or \
	M.item(0,2) < M.item(1,2) or \
	M.item(0,3) < M.item(1,3))) or\
	(M.item(0,1) > M.item(1,1) and (M.item(0,0) < M.item(1,0) or \
	M.item(0,2) < M.item(1,2) or \
	M.item(0,3) < M.item(1,3))) or \
	(M.item(0,2) > M.item(1,2) and (M.item(0,0) < M.item(1,0) or \
	M.item(0,2) < M.item(1,2) or \
	M.item(0,3) < M.item(1,3))) or \
	(M.item(0,3) > M.item(1,3) and (M.item(0,0) < M.item(1,0) or \
	M.item(0,2) < M.item(1,2) or \
	M.item(0,3) < M.item(1,3))):
		return 1
	else:
		return 0

#When in D_4 
def add(M):
	global B
	while M.item(0,0) >= M.item(1,0) and \
		M.item(0,1) >= M.item(1,1) and \
		M.item(0,2) >= M.item(1,2) and \
		M.item(0,3) >= M.item(1,3):
		l = []
		print ("B er i D_4")
		for j in range(0,4):
			if M.item(1,j) != 0:
				l.append(math.floor(M.item(0,j)/M.item(1,j)))
		print ("Så vi tilføjer et "+str(min(l)))
		x_squared.append(min(l))
		C = matrix([[0,1],[1,-min(l)]])
		print ("B ændres til")
		M = C * M
		B = M
		print (B)

def make_e(M):
	global C
	if is_matrix_in_e(M):
		print ("B er i E_4")
		print ("Så vi gør ingenting")

	elif M.item((0,0)) <= M.item((1,0)) and \
		M.item((0,1)) <= M.item((1,1)) and \
		M.item((0,2)) <= M.item((1,2)) and \
		M.item((0,3)) <= M.item((1,3)):
		print ("B er i D_4' så vi tilføjer et 0 og går til D_4")
		x_squared.append(0)
		C = matrix([[0,1],[1,0]])
		M = C * M
		add(M)
	else:
		add(M)

def squared(number):
	global B
	for i in range(0,len(number)):
		print ("Vi er kommet til " + str(number[i]))
		M = matrix([[number[i] ** 2,number[i],number[i],1], \
					[number[i],0,1,0], \
					[number[i],1,0,0], \
					[1,0,0,0]])
		B = B * M
		print ("Og B er på formen:")
		print (B)
		make_e(B)
		if not is_matrix_in_e(B):
			B = C * B

squared(x)

print ("Kædebrøken ser ud på formen")
print (x_squared)

x_fixed = []

def remove_0(frac):
	for i in range(0,len(frac)):
		if frac[i] == 0:
			frac[i+1] = frac[i-1] + frac[i+1]
			x_fixed.remove(frac[i-1])
		else:
			x_fixed.append(frac[i])

if 0 in x_squared:
	remove_0(x_squared)
	print ("Og uden 0'er")
	print (x_fixed)