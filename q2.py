# Function to encode or decode text using Caesar cipher
def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            # Get ASCII value for 'A' or 'a' depending on case
            base = ord('A') if char.isupper() else ord('a')

            # Shift letter forwards or backwards depending on mode
            if mode == "encode":
                new_char = chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decode":
                new_char = chr((ord(char) - base - shift) % 26 + base)

            result += new_char
        else:
            result += char  # Leave spaces and punctuation unchanged

    return result

# Read all text from a file
def read_file(filename):
    file = open(filename, 'r')
    return file.read()

# Write text to a file
def write_file(filename, text):
    file = open(filename, 'w')
    file.write(text)

# Main function to run the program
def main():
    # Get input file name from user
    input_file = input("Enter the name of the input text file: ")

    # Get mode: encode or decode
    mode = input("Do you want to encode or decode? ").lower()

    # Get shift number (e.g., 3 means A → D)
    shift = int(input("Enter the shift number: "))

    # Get output file name to save result
    output_file = input("Enter the name of the output file: ")

    # Read text from input file
    original_text = read_file(input_file)

    # Apply Caesar cipher
    result_text = caesar_cipher(original_text, shift, mode)

    # Save result to output file
    write_file(output_file, result_text)

    print(f"\nDone! The {mode}d text has been saved to {output_file}.")

# Run the program
main()
