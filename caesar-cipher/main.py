alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    newText = ""
    for char in text:
        if(char.isalpha()):
            index = alphabet.index(char)+shift
            if(index> len(alphabet)):
                index = (alphabet.index(char)+shift)-len(alphabet) 
            newText += alphabet[index]
        else:
            newText += char
    return newText
def decrypt(text, shift):
    newText = ""
    for char in text:
        if(char.isalpha()):
            index = alphabet.index(char)-shift
            newText += alphabet[index]
        else:
            newText += char
    return newText

if(direction == "encode"):
    print(encrypt(text, shift))
if(direction == "decode"):
    print(decrypt(text, shift))