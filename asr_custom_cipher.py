from random import randint


class Encode:
    def encoder(self, input_filepath, output_filepath):
        """
        Encodes text from an input file and writes the encrypted text to an output file.
        """
        try:
            # Specify utf-8 encoding for reading
            with open(input_filepath, 'r', encoding='utf-8') as infile:
                plaintext = infile.read()
        except FileNotFoundError:
            print(f"Error: Input file '{input_filepath}' not found.")
            return
        except UnicodeDecodeError:
            print(
                f"Error: Could not decode input file '{input_filepath}' with UTF-8. Try a different encoding if known.")
            return

        key_str = input("Enter Key ")
        try:
            key = list(map(int, key_str.split()))
        except ValueError:
            print("Error: Invalid key format. Please enter space-separated integers.")
            return

        encrypted_text = self.__custom_encrypt(plaintext, key)

        try:
            # Specify utf-8 encoding for writing
            with open(output_filepath, 'w', encoding='utf-8') as outfile:
                outfile.write(encrypted_text)
            print(f"Text successfully encoded and saved to '{output_filepath}'")
        except IOError:
            print(f"Error: Could not write to output file '{output_filepath}'.")

    def __caesar(self, plaintext_chunk: str, key_1: int):
        """
        Performs Caesar cipher encryption on a given chunk of text.
        """
        res = ""
        for char in plaintext_chunk:
            # This operation can produce characters that are not directly printable
            # in some encodings like cp1252. UTF-8 handles them correctly.
            res += chr((ord(char) + key_1) % 256)
        return res

    def __custom_encrypt(self, plaintext: str, key):
        """
        Custom encryption logic. Processes plaintext in chunks based on the key.
        """
        encrypted = ""
        index_curr = 0
        len_plaintext = len(plaintext)

        while index_curr < len_plaintext:
            for k_val in key:
                if index_curr >= len_plaintext:
                    break

                chunk_end = min(index_curr + k_val, len_plaintext)
                plaintext_chunk = plaintext[index_curr:chunk_end]

                if not plaintext_chunk and index_curr == len_plaintext:
                    break  # All plaintext processed and nothing to add

                key_temp = randint(0, 255)
                encrypted += self.__caesar(plaintext_chunk, key_temp)
                encrypted += chr(key_temp)
                index_curr = chunk_end

        return encrypted


class Decode:
    def decoder(self, input_filepath, output_filepath):
        """
        Decodes text from an input file and writes the decrypted text to an output file.
        """
        try:
            # Specify utf-8 encoding for reading
            with open(input_filepath, 'r', encoding='utf-8') as infile:
                encrypted_text = infile.read()
        except FileNotFoundError:
            print(f"Error: Input file '{input_filepath}' not found.")
            return
        except UnicodeDecodeError:
            print(
                f"Error: Could not decode input file '{input_filepath}' with UTF-8. Try a different encoding if known.")
            return

        key_str = input("Enter Key ")
        try:
            key = list(map(int, key_str.split()))
        except ValueError:
            print("Error: Invalid key format. Please enter space-separated integers.")
            return

        decrypted_text = self.__custom_decrypt(encrypted_text, key)

        try:
            # Specify utf-8 encoding for writing
            with open(output_filepath, 'w', encoding='utf-8') as outfile:
                outfile.write(decrypted_text)
            print(f"Text successfully decoded and saved to '{output_filepath}'")
        except IOError:
            print(f"Error: Could not write to output file '{output_filepath}'.")

    def __caesar_decrypt(self, encrypted_chunk: str, key: int):
        """
        Performs Caesar cipher decryption on a given chunk of encrypted text.
        """
        res = ""
        for char in encrypted_chunk:
            res += chr((ord(char) - key) % 256)
        return res

    def __custom_decrypt(self, encrypted: str, key1):
        """
        Custom decryption logic. Reverses the encryption process.
        """
        decrypted = ""
        index_curr = 0
        len_encrypted = len(encrypted)

        while index_curr < len_encrypted:
            for k_val in key1:
                if index_curr >= len_encrypted:
                    break

                chunk_end = index_curr + k_val

                # Check if there's enough data for the chunk and the key character
                if chunk_end >= len_encrypted:
                    # Handle the very last potential partial chunk
                    if index_curr < len_encrypted:  # If there's anything left to decrypt
                        # The last character is assumed to be the key_temp for the preceding data
                        key_char_index = len_encrypted - 1
                        key_for_last_chunk = ord(encrypted[key_char_index])
                        decrypted_chunk = encrypted[index_curr:key_char_index]
                        decrypted += self.__caesar_decrypt(decrypted_chunk, key_for_last_chunk)
                        index_curr = len_encrypted  # Mark as fully processed
                    break  # Exit inner loop, done with encrypted data

                key_char_index = chunk_end
                # Ensure we don't go out of bounds trying to read the key_temp
                if key_char_index >= len_encrypted:
                    # This implies malformed encrypted data if it happens here,
                    # as every chunk should have a key_temp following it.
                    # For robustness, handle it as the end of data if no key_temp is present.
                    if index_curr < len_encrypted:
                        # Attempt to decrypt whatever remains using a default or error key if needed,
                        # but ideally, this path shouldn't be hit with correctly formed encrypted data.
                        # For now, let's assume valid data and just break.
                        pass
                    break

                key_for_chunk = ord(encrypted[key_char_index])
                encrypted_chunk = encrypted[index_curr:chunk_end]
                decrypted += self.__caesar_decrypt(encrypted_chunk, key_for_chunk)
                index_curr = chunk_end + 1

        return decrypted

            #Example usage

#encode_obj = Encode()
#decode_obj = Decode()
#print("--- Encoding ---")
#encode_obj.encoder("plaintext.txt", "encrypted.txt")
#print("\n--- Decoding ---")
#decode_obj.decoder("encrypted.txt", "decrypted.txt")
