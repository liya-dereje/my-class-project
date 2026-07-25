total_amount=4000
people=["friend1","friend2","friend3","friend4"]
rate=0.10

def calculate_amount(total_amount, people, rate):
    num_people=len(people)
    total_with_tip=total_amount*(1+rate)
    amount_per_person=total_with_tip/num_people
    return amount_per_person,total_with_tip
x=calculate_amount(total_amount, people, rate) 
for i in people:
    print(f"{i}: {x}ETB")
