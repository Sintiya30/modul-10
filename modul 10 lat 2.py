#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:03:30 2024

@author: adesintia
"""

def bubble_sort_recursive(arr):
    # Base case: jika panjang array tinggal satu elemen atau kurang, array sudah terurut
    if len(arr) <= 1:
        return arr
    
    # Lakukan satu iterasi bubble sort
    # Bandingkan elemen-elemen bersebelahan dan tukar jika diperlukan
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Tukar jika elemen tidak terurut
    
    # Rekursif untuk elemen yang tersisa, kecuali elemen terakhir (karena elemen terakhir sudah berada di tempatnya)
    return bubble_sort_recursive(arr[:-1]) + arr[-1:]

# Daftar angka untuk diurutkan
numbers = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]

# Menampilkan daftar sebelum diurutkan
print("List Sebelum Disorting:")
print(numbers)

# Memanggil fungsi bubble_sort_recursive untuk mengurutkan daftar
sorted_numbers = bubble_sort_recursive(numbers)

# Menampilkan daftar setelah diurutkan
print("List Yang Sudah Disorting:")
print(sorted_numbers)
