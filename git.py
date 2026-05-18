def oraliq(min, max, qadam=1):
    sonlar = []
    hozirgi = min
    
    # Agar qadam 0 bo'lsa, xatolikni oldini olish kerak
    if qadam == 0:
        return "Qadam 0 ga teng bo'lishi mumkin emas."

    while hozirgi < max:
        sonlar.append(hozirgi)
        hozirgi += qadam  # Har safar qadam miqdoricha oshiramiz
        
    return sonlar

# Tekshirish:
#print(oraliq(2, 10, 2))  # Natija: [2, 4, 6, 8]
print(oraliq(5, 15))     # Natija: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]