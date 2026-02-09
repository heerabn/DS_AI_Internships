student={"name":"Amit","age":21,"courses":"Enginnering"}
print(student["name"])
student["age"]=22
student["city"]="Delhi"
print(student)

#Dictionary methods & Iteration
marks={"math":80,"science":75,"english":89}
print(marks.get("math"))
print(marks.get("history",0))
print(marks.update({"kannada":92}))
print(marks.pop("science"))
for subject,score in marks.items():
    print(subject,score)

purchases={"Alice":250,"Bob sent":400,"charlie":150}
for name,amount in purchases.items():
    print(f"{name}: spent ₹{amount}")

    print("Total costomer:",len(purchases))
    print("purchases amounts:",purchases.keys())

#Input dictionary from user
n=int(input("Enter number of customers:"))
user_purchases={}
for i in range(n):
    name=input("Enter customer name:")
    amount=int(input(f"Enter purchase amount for{name}:"))
    user_purchases[name]=amount
    print("Customer Purchases Data:",user_purchases)

 #when we need only key values
top_customers=max(purchases,key=purchases.get)
print("Top spending customer:",top_customers)   

top_customers=min(purchases,key=purchases.get)
print("Minimum spending customer:",top_customers)    