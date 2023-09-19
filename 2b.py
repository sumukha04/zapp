def binaryToDecimal(binary):
    decimal, i,=0,0
    while(binary!=0):
        dec=binary%10
        decimal=decimal+dec*pow(2,i)
        binary=binary//10
        i+=1
        print(decimal)
        binaryToDecimal(0b0011)
                                
        def octTOHex(n):
            print("octal=", n)
            decnum=int(n,8)
            hexadecimal=hex(decnum).replace("0x", "")
            print("equivalent hexadecimalvalue=", hexadecimal)
            octTOHex('5123')