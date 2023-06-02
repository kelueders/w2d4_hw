from IPython.display import clear_output  # won't work in VS code

# step 1
def store_info():
    # step 2
    d = {}
    
    # step 3
    while True:
        # step 4
        name = input("Enter a name or say 'quit' to quit: ")
        if name.lower() != "quit":
            address = input("Enter an address or say 'quit' to quit: ")
        # step 5
        if name.lower() == "quit" or address.lower() == "quit":
            # step 5A
            for name, address in d.items():
                print(f"The address for {name} is {address}.")
            # step 5B
            break
        # step 6
        d[name] = address
        
# step 7
store_info()   