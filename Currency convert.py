# Currency convert 
cn_Yuan = float(input("Ingrese que le quedo en Yuan: "))
jp_Yen = float(input("Ingrese que le quedo en Yen: "))
kr_Won = float(input("ingrese que le quedo en Won: "))
yuan_Dl = 0.145
yen_Dl = 0.007
won_Dl = 0.001
ex_Tot = (cn_Yuan*yuan_Dl)+(jp_Yen*yen_Dl)+(kr_Won*won_Dl)
print(f"Su remanente de cambio en dolares es: ",ex_Tot)
