#/usr/bin/env python
# -*- coding: utf-8 -*-

def ekle(x, y):
   """This function adds two numbers"""

   return x + y

def cikart(x, y):
   """This function subtracts two numbers"""

   return x - y

def carp(x, y):
   """This function multiplies two numbers"""

   return x * y

def bol(x, y):
   """This function divides two numbers"""
   return x / y

print("Seçiniz")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

secim = input("Seçim (1/2/3/4):")

sayi1 = int(input("ilk sayi: "))

sayi2 = int(input("ikinci sayi: "))


if secim == 1: print(sayi1,"+",sayi2,"=", ekle(sayi1,sayi2))

elif secim == 2 : print(sayi1,"-",sayi2,"=", cikart(sayi1,sayi2))

elif secim == 3: print(sayi1,"*",sayi2,"=", carp(sayi1,sayi2))

elif secim == 4: print(sayi1,"/",sayi2,"=", bol(sayi1,sayi2))

else: print("hatalı giriş")