# Mendefinisikan harga buah
price_apel = 10000
price_jeruk = 15000
price_anggur = 20000

#mendefinisikan jumlah buah
stock_apel=10
stock_jeruk=7
stock_anggur=5

while True:
    # Meminta input jumlah apel kepada user
    while True:
        n_apel = int(input('Masukkan jumlah apel: '))
        if n_apel>stock_apel:
            print(f"pesanan anda tidak dapat dipenuhi, karena sisa stock sekarang{stock_apel}")
        else:
            break

    # Meminta input jumlah jeruk kepada user
    while True:
        n_jeruk = int(input('Masukkan jumlah jeruk: '))
        if n_jeruk>stock_jeruk:
            print(f"pesanan anda tidak dapat dipenuhi, karena sisa stock sekarang{stock_jeruk}")
        else:
            break

    # Meminta input jumlah anggur kepada user
    while True:
        n_anggur = int(input("Masukkan jumlah apel: "))
        if n_anggur>stock_anggur:
            print(f"pesanan anda tidak dapat dipenuhi, karena sisa stock sekarang{stock_anggur}")
        else:
            break


    # Menghitung total belanjaan per buah
    total_apel = n_apel * price_apel
    total_jeruk = n_jeruk * price_jeruk
    total_anggur = n_anggur * price_anggur

    # Menghitung total belanjaan
    total = total_apel + total_jeruk + total_anggur

    # Show
    print(f'''Detail Belanjaan
        
    Apel : {n_apel} x {price_apel} = {total_apel}
    Jeruk : {n_jeruk} x {price_jeruk} = {total_jeruk}
    Anggur : {n_anggur} x {price_anggur} = {total_anggur}
        
    Total : {total}
    ''')

    #pembayaran
    while True:
        bayar= int(input("masukkan uang anda:"))
        if bayar>=total:
            print("terimakasih")
            print(f"uang kembalian anda sebesar{bayar-total}")
            break
        else:
            print(f"uang anda kurang {total-bayar}")

    #update stock
    stock_apel-=n_apel
    stock_jeruk-=n_jeruk
    stock_anggur=n_anggur

    # Konfirmasi belanja ulang
    konfirmasi = input('Apakah akan melakukan belanja lagi?: ')
    if konfirmasi == 'no':
        break