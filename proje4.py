#kullanıcıdan alacagın sifrelerin uygunluk durum kontrolü
#kosul 1=sifre icinde hem büyül hem küçük harf olmalı
#kosul 2=sifrede en az bir sayi kullanılmış olmalı
#sifrenin 8 karakterden uzun olması gerek
#sifrenin 16 karakterden kısa olması gerek
kücükh=False
büyükh=False
sayi=False
karakter_sayi=0
sifre=input("lütfen sifre olustur:")
for ch in sifre:
    if büyükh==False and ch>="A" and ch<="Z":
       büyükh= True
    elif kücükh==False and ch>='a' and ch<='z':
        kücükh=True
    elif sayi==False and ch>='0' and ch<='9' :
        sayi=True
    karakter_sayi+=1
if büyükh==False:
        print("büyük harf kullan")   
elif kücükh==False:
        print("kücük harf kullan")       

elif sayi==False:
        print("sayi kullan")       
elif karakter_sayi<8 :
      print("eksik karakter sayisi")
elif karakter_sayi>16:
      print("fazla karakter sayi")      

else:    
      print("sifre onaylandı")  