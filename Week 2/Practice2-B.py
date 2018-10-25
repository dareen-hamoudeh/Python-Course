
# coding: utf-8

# In[13]:


print(" welcome to our Money Converter App, Please enter the amount of money you want to convert")
print("and the currencies you want to convert, as the following:")
print("write JD for Jordanian Dinar,")
print("write TL for Turkish lira,")
print("write US for Dollar")
print("-------------------------------------------")
amount=float(input("Enter Amount "))
currency_from=(input("Convert From: "))
currency_to=(input("Convert To: "))
print("-------------------------------------------")

if (currency_from=="JD"):
    if (currency_to=="TL"):
        print(amount,"JD=",amount*8.03,"TL")
    elif (currency_to=="US"):
        print(amount,"JD=",amount*1.41,"US")
    else:
        print("Currency NOT supported", "Try again!")
elif (currency_from=="TL"):
    if (currency_to=="JD"):
        print(amount,"TL=",amount/8.03,"JD")
    elif (currency_to=="US"):
        print(amount,"TL=",amount/5.70,"US")
    else:
        print("Currency NOT supported, Try again!")
elif (currency_from=="US"):
    if (currency_to=="JD"):
        print(amount,"US=",amount/1.41,"JD")
    elif (currency_to=="TL"):
        print(amount,"US=",amount*5.70,"TL")
    else:
        print("Currency NOT supported, Try again!")
else:
    print("Currency NOT supported, Try again!")
    
    

