def celcius_ke_fahrenheit(celcius):
    hasil=(celcius*(9/5))+32
    print(hasil)
    
celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

def is_genap(bilangan):
 print(bilangan % 2 == 0)
 
is_genap(4)
is_genap(7)

def is_genap(bilangan):
 print(bilangan % 2 == 0)
 
is_genap(4)
is_genap(7)

def bilangan(angka):
    for i in range(1, angka*1):
        if i % 2 != 0:
            print(i, end="")
            
bilangan(20)
