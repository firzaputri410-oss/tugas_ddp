kendaraan = ["vespa sprint", "motor", 150, "yellow", 2]
tambahan = [55000000, "matic"]
kendaraan.extend(tambahan) 
kendaraan.insert(2, "vespa")
print(kendaraan)

#tugas no 2
print("=== alat hitung luas bangun datar===")
print("pilih 1 untuk menghitung luas persegi")
print("pilih 1 untuk menghitung luas lingkaran")
print("pilih 1 untuk menghitung luas segitiga")

pilihan = int(input("masukan pilihan(1/2/3)"))

match pilihan:
    case 1:
        s = int(input("Masukan panjang sisi persegi"))
        luas = s + s
        print(f"luas persegi adalah:{luas}")

    case 2:
        r = int(input("Masukan panjang jari-jari lingkaran:"))
        pi = 3.14
        print(f"luas persegi adalah:{luas}")
        luas = pi * r**2
        
    case 3:
        a = int(input("Masukan panjang alas segitiga:"))
        t = int(input("Masukan panjang tinggi segitiga:"))
        luas = a * t / 2
        print(f"luas persegi adalah:{luas}")
        
