friend_a={"python","cooking","hiking","movies"}
freind_b={"hiking","gaming","photography","python"}
common_interests=friend_a & freind_b
print("Common interests between friend a and friend b:",common_interests)
All_interests=friend_a | freind_b
print("All interests of friend a and friend b:",All_interests)
unique_intersets=friend_a - freind_b
print("Unique interests of friend a:",unique_intersets)