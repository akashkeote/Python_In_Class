#lex_auth_012693782475948032141

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    food_type = food_type.upper()
    if(quantity_ordered<1 or distance_in_kms<=0 or food_type not in ('V', 'N')):
        return -1
    bill=0
    if(food_type=='V'):
        bill=120*quantity_ordered
    elif(food_type=='N'):
        bill=150*quantity_ordered
        
    distance_in_kms=distance_in_kms-3
    
    if distance_in_kms<=0:
        bill_amount=bill

    elif distance_in_kms<=3:
        bill_amount=bill+(distance_in_kms*3)
        
    elif distance_in_kms>3:
        bill_amount=bill+(3*3)+(distance_in_kms-3)*6
       
        
    
    
    return bill_amount
#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)