# Import the os module so we can check if files exist on the computer (Zaimportuj moduł os, abyśmy mogli sprawdzić, czy pliki istnieją na komputerze)
import os

# Define a function to encrypt or decrypt a file using a secret key (Zdefiniuj funkcję do szyfrowania lub deszyfrowania pliku za pomocą tajnego klucza)
def encrypt_decrypt_file(input_file_path, output_file_path, key):
    # Print a status message showing which file is being processed (Wypisz komunikat o stanie pokazujący, który plik jest przetwarzany)
    print(f"Processing file: {input_file_path}...")

    # Check if the input file actually exists before trying to open it (Sprawdź, czy plik wejściowy faktycznie istnieje przed próbą jego otwarcia)
    if not os.path.exists(input_file_path):
        # Print an error message if the file is missing (Wypisz komunikat o błędzie, jeśli plik jest pomijany/brakujący)
        print(f"Error: The file {input_file_path} does not exist!")
        # Exit the function early because there is nothing to process (Wyjdź z funkcji wcześniej, ponieważ nie ma nic do przetworzenia)
        return

    # Open the input file in binary read mode ('rb' means read bytes) (Otwórz plik wejściowy w trybie odczytu binarnego - 'rb' oznacza odczyt bajtów)
    with open(input_file_path, 'rb') as file_to_read:
        # Read all the raw bytes from the file into memory (Przeczytaj wszystkie surowe bajty z pliku do pamięci)
        file_bytes = file_to_read.read()

    # Create an empty byte array to store our modified/encrypted bytes (Stwórz pustą tablicę bajtów, aby przechowywać nasze zmodyfikowane/zaszyfrowane bajty)
    processed_bytes = bytearray()

    # Convert the string key into bytes so we can do math with file bytes (Przekonwertuj klucz tekstowy na bajty, abyśmy mogli robić matematykę z bajtami pliku)
    key_bytes = key.encode('utf-8')
    
    # Get the length of the key so we can loop through it repeatedly (Pobierz długość klucza, abyśmy mogli przechodzić przez niego w kółko)
    key_length = len(key_bytes)

    # Loop through every single byte in the file along with its index position (Przejdź przez każdy pojedynczy bajt w pliku wraz z jego pozycją indeksu)
    for index, current_byte in enumerate(file_bytes):
        # Get the corresponding byte from the key using modulo operator (%) to loop key bytes (Pobierz odpowiedni bajt z klucza za pomocą operatora modulo, aby zapętlić bajty klucza)
        key_byte = key_bytes[index % key_length]
        
        # Apply XOR operation (^) between file byte and key byte to scramble it (Zastosuj operację XOR pomiędzy bajtem pliku a bajtem klucza, aby go pomieszać/zaszyfrować)
        scrambled_byte = current_byte ^ key_byte
        
        # Append the new scrambled byte to our processed bytes collection (Dodaj nowy zaszyfrowany bajt do naszej kolekcji przetworzonych bajtów)
        processed_bytes.append(scrambled_byte)

    # Open the output file in binary write mode ('wb' means write bytes) (Otwórz plik wyjściowy w trybie zapisu binarnego - 'wb' oznacza zapis bajtów)
    with open(output_file_path, 'wb') as file_to_write:
        # Write all processed (encrypted or decrypted) bytes into the new file (Zapisz wszystkie przetworzone bajty do nowego pliku)
        file_to_write.write(processed_bytes)

    # Print a success message once the operation is fully completed (Wypisz komunikat o sukcesie, gdy operacja zostanie całkowicie zakończona)
    print(f"Success! Output saved to: {output_file_path}\n")

# Main execution block to test our function (Główny blok wykonawczy do przetestowania naszej funkcji)
if __name__ == "__main__":
    # Create a dummy text file to test our encryption on (Utwórz testowy plik tekstowy, aby przetestować na nim szyfrowanie)
    test_filename = "secret_message.txt"
    
    # Open the test file in write text mode and write a secret string (Otwórz plik testowy w trybie zapisu tekstu i wpisz tajny ciąg znaków)
    with open(test_filename, 'w', encoding='utf-8') as f:
        f.write("Top Secret Portfolio Project: Python and C++ rule!")

    # Define a secret password key for encryption (Zdefiniuj tajne hasło/klucz do szyfrowania)
    secret_key = "SuperSecretKey123"

    # Define filenames for encrypted and decrypted files (Zdefiniuj nazwy plików dla plików zaszyfrowanych i odszyfrowanych)
    encrypted_filename = "encrypted_file.enc"
    decrypted_filename = "decrypted_message.txt"

    # Step 1: Encrypt our original secret file (Krok 1: Zaszyfruj nasz oryginalny tajny plik)
    encrypt_decrypt_file(test_filename, encrypted_filename, secret_key)

    # Step 2: Decrypt the encrypted file back to readable text (Krok 2: Odszyfruj zaszyfrowany plik z powrotem do czytelnego tekstu)
    encrypt_decrypt_file(encrypted_filename, decrypted_filename, secret_key)