class Item: 
    def __init__(self, value, weight): 
        self.value = value 
        self.weight = weight 

def fractionalKnapsack(W, arr): 
    # Sorting items based on value-to-weight ratio in descending order
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True) 
    finalvalue = 0.0  # Result (value in knapsack)
    
    # Loop through all items
    for item in arr: 
        # If adding the whole item won't exceed capacity, add it completely
        if item.weight <= W: 
            W -= item.weight 
            finalvalue += item.value 
        else: 
            # Add fractional part of the item
            finalvalue += item.value * W / item.weight 
            break 

    return finalvalue  # Return the final value of items in knapsack

# Driver Code
if __name__ == "__main__": 
    # Take user input for maximum knapsack weight
    W = float(input("Enter the maximum weight capacity of the knapsack: "))

    # Take user input for the number of items
    n = int(input("Enter the number of items: "))
    
    arr = []
    for i in range(n):
        value = float(input(f"Enter value of item {i + 1}: "))
        weight = float(input(f"Enter weight of item {i + 1}: "))
        arr.append(Item(value, weight))  # Add item to the list
    
    # Calculate maximum value for the given knapsack capacity
    max_val = fractionalKnapsack(W, arr) 
    print(f"The maximum value in the knapsack can be: {max_val}")
