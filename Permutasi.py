import math
#Metode Perkalian
def Mperkalian(n):
	BanyakCara = 1
	for i in range (0,len(n)):
		BanyakCara = BanyakCara * n[i]
	return BanyakCara

#Permutasi
def Permutasi(r,n):
	Permutasi = math.factorial(n) / math.factorial(n-r)
	return int(Permutasi)

#Kombinasi
def Kombinasi(n,r):
	Kombinasi = math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
	return int(Kombinasi)
def potongan(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 

def P_AUB(A,B,S):
	P_A= len(A)/len(S)
	P_B= len(B)/len(S)
	AB = potongan(A,B)
	P_AB = len(AB)/len(S)
	P_AUB = P_A + P_B - P_AB
	return P_AUB

def P_A1An(A,S):
	nS= len(S)
	P_A1An = 0
	P=[]
	for i in range (0,len(A)):
		P.append(len(A[i])/nS)
		P_A1An = P_A1An + P[i]
	return P_A1An

def P_AB(A,B,S):
	P_A = len(A)/len(S)
	P_B = len(B)/len(S)
	P_AB = P_A*P_B
	return P_AB 

def P_AgB(A,B,S):
	P_B = len(B)/len(S)
	if P_B != 0:
		P_AB = len(potongan(A,B))/len(S)
		P_AgB = P_AB /P_B
	return P_AgB

A = [1,2,3,5,6]
B = [2,3,7,8,9,10]
S =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

A2 = [[1,2],[3,4,5],[6,9],[7,8,10,11],[14,15]]
S2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

G1 = []
for i in range (5):
	G1.append(i)
G2 = []
for i in range (20):
	G2.append(i)
K = []
for i in range (25):
	K.append(i)
S3 = []
for i in range (100):
	S3.append(i)


print(Mperkalian([3,5,3]))
print(Permutasi(2,3))
print(Kombinasi(4,3))
print(P_AUB(A,B,S))
print(P_A1An(A2,S))
print(P_AgB(G1,K,S3))