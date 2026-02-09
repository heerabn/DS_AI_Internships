raw_logs=["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]
unique_logs=set(raw_logs)
print("ID05" in unique_logs)
#print("ID03" in unique_logs)
print(unique_logs)
print("Length of row_logs list:",len(raw_logs))
print("Length of unique_logs set:",len(unique_logs))
duplicates_removed=len(raw_logs)-len(unique_logs)
print("Number of duplicate entries removed:",duplicates_removed)