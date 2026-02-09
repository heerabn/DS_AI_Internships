contacts={"Alice":"9876543210","Bob":"9876543210","Charlie":"9876543210"}
print(contacts)
contacts["Alice"]=9876543210
print(contacts)
print("Alice number:",contacts.get("Alice"))
print("Eve number:",contacts.get("Eve","Contact Not Found"))
for name, number in contacts.items():
    print(f"contact:{name}| phone:{number}")