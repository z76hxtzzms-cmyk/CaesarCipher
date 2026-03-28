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

choice = int(input("Enter choice: "))

# Only let user pick 1 or 2, else keep asking to re enter. 
while choice != 1 and choice != 2:
    print("Invalid choice, enter 1 or 2")
    choice = int(input("Enter choice: "))


# If the above passes, then we drop down to this code.
if choice == 1:
    # Append to encoded (user picked 1)
    for char in msg:
        if char in alphabet:    # Check if char in alphabet
            new_position = (alphabet.index(char) + shift) % 26
            encoded += alphabet[new_position]
        else:
            encoded += char # If not in alphabet, probably special char, space, etc. append.
    # Append to decoded (user picked 2)
else:
    for char in msg:
        if char in alphabet:
            new_position = (alphabet.index(char) - shift) % 26
            decoded += alphabet[new_position]
        else:
            decoded += char

# Print results
if choice == 1:
    print("Encoded Message: " + encoded)
else:
    print("Decoded Message: " + decoded)


    

