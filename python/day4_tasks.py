
cart=["shirt" , "facewash" , " bodyspray" , "shoes"]
print(cart)

cart[-2]="perfume"
print("after updating the value: ",cart)

cart.append("watch")
print("after adding the watch: ",cart)

cart.remove("shirt")
print("after removing the shirt: ",cart)

print(f"the length of the list after modifications is: {len(cart)}")

