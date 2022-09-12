while True:
    number = int(input('Masukkan angka : '))
    print('Roman value is : ', end = " ")
    # printRoman('Roman value is : ')2
    lanjut = input('Mau ulang atau tidak (y/n) : ')
    if lanjut == 'Y' or lanjut == 'y':
        continue
    elif lanjut == 'N' or lanjut == 'n':
        break
    else:
        print('Keyword yang anda masukkan salah')