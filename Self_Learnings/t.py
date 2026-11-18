#lex_auth_012693782475948032141

def calculate_bill_amount(f,q,d):
    bill_amount=0
    #write your logic here
    try:
        if f=='N':
            if d>0 and q>0:
                if d>0 and d<3:
                    bill_amount=q*150
                elif d>=3 and d<6:
                    bill_amount=(q*150)+(d-3)*3
                elif d>=6 :
                    bill_amount=(q*150)+(9)+((d-6)*6)
        elif f=='V':
            if d>0 and q>1:
                if d>0 and d<3:
                    bill_amount=q*120
                elif d>=3 and d<6:
                    bill_amount=(q*120)+3
                elif d>=6 :
                    bill_amount=(q*120)+6
            
    except:
        print("distance must be positive")
    
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)