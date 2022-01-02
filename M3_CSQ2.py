K = input()
K_int = float(K)
Bill = 0
if K_int <= 10:
    Bill += (K_int * 15)
    print(float(Bill))
elif K_int > 10 and K_int <= 100:
    Bill += 150 + ((K_int -10) * 8)
    print(float(Bill))
elif K_int > 100:
    Bill += (150 + 720) + ((K_int - 100) * 6)
    print(float(Bill))
    
