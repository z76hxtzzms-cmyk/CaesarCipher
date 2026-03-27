# Implement a list to represent the alphabet and use it to encode and decode messages.
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S",
            "T", "U", "V", "W", "X", "Y", "Z"]

msg = input("Enter a message: ")
shift = int(input("Enter shift amount: "))
encoded = ""    # The string we will apend to when encoding
decoded = ""    # The string we will append to when decoding
msg = msg.upper()   # Turn into uppercase to prep for encryption

print("1) Encode message")
print("2) Decode message")

# Ensure user is only able to have two options
# TODO: Implement a while loop instead so we don't have to terminate
#       over user error.

choice = int(input("Enter choice: "))
if choice != 1 and choice != 2:
    print("Invalid choice, terminating program.")
    exit()


# If the above passes, then we drop down to this code.
if choice == 1:
    # Create a for loop that loops through every char
    # Append to encoded (user picked 1)
    for char in msg:
        new_position = (alphabet.index(char) + shift) % 26
        encoded += alphabet[new_position]
else:
    for char in msg:
        new_position = (alphabet.index(char) - shift) % 26
        decoded += alphabet[new_position]
        
#TODO: Complete the rest soon!


    

