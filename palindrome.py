

def palindrome(string: str) -> bool:
    string=string.lower().replace(" ", "").strip()
    return string == string[::-1]


def run():
#    string: str = input("Ingrese una palabra: ")
    
    if palindrome(100):
        print("Es un palindromo")
    else:
        print("No es un palindromo")

if __name__ == "__main__":
    run()
