angka=input('Masukan kombinasi angka:')
rev_angka=angka[::-1]
if angka==rev_angka:
    print('Palindrom')
else:
    print('Bukan Palindrom')