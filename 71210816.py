def kalkulator(kalkulasi):
    x = kalkulasi.split(" ")
    if x[1] == '+':
        hasil = int(x[0])+int(x[2])
    elif x[1] == '-':
        hasil = int(x[0])-int(x[2])
    elif x[1] == '*':
        hasil = int(x[0])*int(x[2])
    elif x[1] == '/':
        hasil = float(x[0])/float(x[2])
    print(hasil)
i = 0        
while i != 1:
    x = input("Masukkan input: ")
    if x != "q":
        kalkulator(x)
    else:
        i = 1
