#1
a = input()
x = a.lower().split()  # lower chuyen viet hoa thanh viet thuong
b = input()             #  split t/c
if b in x:{
    print("Đúng")
    }
else:{
    print("Sai")
    }

#
C = 'nguyen trong nghia' 

# txt = D.lower()
x = C.lower().split()
dic = {}
for i in x:
	if( i in dic):
		dic[i] += 1
	else:
		dic[i] = 1
print(dic)