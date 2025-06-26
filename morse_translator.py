# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

# Function to encrypt the string
def encrypt(message):
    encrypted = ''
    for char in message.upper():
        if char in MORSE_CODE_DICT:
            encrypted += MORSE_CODE_DICT[char] + ' '
        else:
            encrypted += '? '
    return encrypted.strip()

# Function to decrypt the string
def decrypt(message):
    reversed_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = message.split(' ')
    decrypted = ''
    for symbol in words:
        if symbol == '/':
            decrypted += ' '
        elif symbol in reversed_dict:
            decrypted += reversed_dict[symbol]
        else:
            decrypted += '?'
    return decrypted

# Main menu
def main():
    print("Morse Code Translator")
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()
    if choice == 'E':
        text = input("Enter message to encrypt: ")
        print("Encrypted Morse Code:", encrypt(text))
    elif choice == 'D':
        code = input("Enter Morse code to decrypt (use '/' for space): ")
        print("Decrypted Message:", decrypt(code))
    else:
        print("Invalid option")

if __name__ == '__main__':
    main()
