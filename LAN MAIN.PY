WG, G, WO, B, WB, O, WBr, Br = str(1,2,3,4,5,6,7,8)
T568A = WG, G, WO, B, WB, O, WBr, Br
for i in range(10):
    a = input("Enter the PO separated by comma's with correct capitalization here: ")
    if a == T568A:
       print("YOU ARE CORRECT:")
    else:
        print("YOU ARE INCORRECT,PLEASE TRY AGAIN")
    print("T58A PINOUTS ARE WG, G, WO, B, WB, O, WBr, Br = ", T568A)
