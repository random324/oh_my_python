print("Pertalite: harga 50.000")
print("Pertamax: harga 53.000")
print("Shampo: harga 60.000")
print("Sabun: harga 65.000")
print("Parfum: harga 70.000")
print("Buku: harga 75.000")
print("Sapu: harga 80.000")
print("Baju: harga 88.000")
print("Hoody: harga 90.000")
print("Kipas: harga 100.000")
print("------------------------------>")

barang=(input("masukkan barang :"))
if barang == "Pertalite":
    harga=50000
    nama="Pertalite"
elif barang == "Pertamax":
    harga=53000
    nama="Pertamax"
elif barang == "Shampo":
    harga=60000
    nama="Shampo"
elif barang == "Sabun":
    harga=65000
    nama="Sabun"
elif barang == "Parfum":
    harga=70000
    nama="Parfum"
elif barang == "Buku":
    harga=75000
    nama="Buku"
elif barang == "Sapu":
    harga=80000
    nama="Sapu"
elif barang == "Baju":
    harga=88000
    nama="Baju"
elif barang == "Hoody":
    harga=90000
    nama="Hoody"
elif barang == "Kipas":
    harga=100000
    nama="Kipas"
else:
    harga=0
    nama=""
    print("barang tidak tersedia")
if harga > 0:
    kuantitas=int(input("masukkan jumlah barang "+nama+" :"))
    if harga > 0:
        total_belanja=harga*kuantitas
        print("Harga satuan :",harga)
        print("Total belanja anda :",total_belanja)
        if total_belanja < 1000000:
            discount=total_belanja*0/100
            total_bayar=total_belanja-discount
            print("Total discount anda :",discount)
            print("Total pembayaran :", total_bayar)
        elif total_belanja <= 1500000:
            discount=total_belanja*10/100
            total_bayar=total_belanja-discount
            print("Total discount anda :",discount)
            print("Total pembayaran :", total_bayar)
        elif total_belanja > 1500000:
            discount=total_belanja*15/100
            total_bayar=total_belanja-discount
            print("Total discount anda :",discount)
            print("Total pembayaran :", total_bayar)
        else:
            print("anda tidak membeli apapun")