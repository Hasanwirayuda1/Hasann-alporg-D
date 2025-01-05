#buatlah program pengecekan rentan angka sesuai nim

#++++++24-------33+++++++

inputUser = float(input("masukan angka yang bernilai\nkurang dari 24\natau\nlebih besar dari 33:"))

#+++++24-------------
#memeriksa angka kurang dari 24
iskurangdari = (inputUser <24)
print("kurang dari 24 =",iskurangdari)

#-----33+++++++++++++
#memeriksa angka lebih dari 33
islebihdari = (inputUser >33)
print("lebih dari 33 =",islebihdari)

#++++++24-------33+++++++
iscorrect = iskurangdari or islebihdari
print("angka yang anda masukan :",iscorrect)

#--------24++++++++33--------
print("\n",10*"=","\n")

inputUser = float(input("masukan angka yang bernilai\nlebih besar dari 24\ndan\nkurang dari 33:"))

#------24+++++++++++++
islebihdari = (inputUser >24)
print("lebih dari 24 =",islebihdari)

#++++++33-------------
iskurangdari = (inputUser <33)
print("kurang dari 33 =",iskurangdari)

#------24++++++++33---------
iscorrect = iskurangdari and islebihdari
print("angka yang anda masukan :",iscorrect)


