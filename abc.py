a = input("Enter Number In Any Format = ")
in_form = input("Enter The Format You Want To Convert From = ")
out_form = input("Enter The Format You Want To Convert To = ")


if in_form.lower() == "binary":
    val = int(a,2)
elif in_form.lower() == "octal":
    val = int(a,8)
elif in_form.lower() == "decimal": 
    val = int(a,10)       
elif in_form.lower() == "hexadecimal":  
    val = int(a,16) 
else:
    print("Invalid Input Format")

if out_form.lower() == "binary":
   print("Binary Representation of ",a,"is = ",bin(val)[2:])
elif out_form.lower() == "octal":
    print("Octal Representation of ",a,"is = ",oct(val)[2:])   
elif out_form.lower() == "decimal":
    print("Decimal Representation of ",a,"is = ",val)      
elif out_form.lower() == "hexadecimal":
    print("Hexadecimal Representation of ",a,"is = ",hex(val)[2:])   
else:
    print("Invalid Input Format")         