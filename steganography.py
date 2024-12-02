def hide_message_in_bmp(input_bmp, output_bmp, secret_message):
    try:
        # the code open the BMP photo in binary 
        with open(input_bmp, "rb") as file:
            data = bytearray(file.read())

        # this line changes the secret message to binary and adds 8 zero bits to know when it ended 
        message_bits = ''.join(f'{ord(char):08b}' for char in secret_message) + '00000000'

        # a checker to see if the message will fit in the file 
        if len(message_bits) > (len(data) - 54) * 8:  # Header is 54 bytes
            raise ValueError(" image too small to write the secret message.")

        # putting the binary message in the image 
        bit_index = 0
        for i in range(54, len(data)):
            if bit_index >= len(message_bits):
                break
            data[i] = (data[i] & 0xFE) | int(message_bits[bit_index])  # replace LSB with message
            bit_index += 1

        # save the new data to the BMP output
        with open(output_bmp, "wb") as file:
            file.write(data)
        print("messaage hidden")
    except:
        raise FileNotFoundError("File Not Found")


def extract_message_from_bmp(input_bmp):
    # open the BMP file with the hidden message
    with open(input_bmp, "rb") as file:
        data = bytearray(file.read())

    # extract bits after 54 bits 
    message_bits = []
    for byte in data[54:]:
        message_bits.append(byte & 1)  # Get the least significant bit
    return message_bits


def binary_to_str(message_bits):
    message_chars = []
    for i in range(0, len(message_bits), 8):
        byte = message_bits[i:i + 8]
        char = chr(int(''.join(map(str, byte)), 2))
        if char == '\x00':  # stop at the null terminator 
            break
        message_chars.append(char)
    # return the message
    return ''.join(message_chars)


# program
print("choose an option")
print("1. write a secret message using an BMP file")
print("2. reveal a secret message from an BMP file")
mode = input("choose 1 or 2: ")

if mode == "1":
    # hide message mode
    input_bmp = input("enter the path to your BMP file")
    output_bmp = input("enter the path to save your output as BMP file ")
    secret_message = input("enter your secret message: ")
    hide_message_in_bmp(input_bmp, output_bmp, secret_message)

elif mode == "2":
    # extract message 
    input_bmp = input("enter path of the output of BMP file ")
    extracted_message = extract_message_from_bmp(input_bmp)
    string_message = binary_to_str(extracted_message)
    print("secret message:", string_message)

else:
    print("please pick 1 or 2 .")