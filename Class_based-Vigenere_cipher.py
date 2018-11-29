"""
author: Jason van Raamsdonk
"""

from abc import ABC, abstractmethod


class AbstractClass (ABC):
    @abstractmethod
    def getUserInput(self):
        pass

    @abstractmethod
    def msg_and_key(self):
        pass

    @abstractmethod
    def create_vigenere_table(self):
        pass

    @abstractmethod
    def cipher_encryption(self, message, mapped_key):
        pass

    @abstractmethod
    def itr_count(self, mapped_key, message):
        pass

    @abstractmethod
    def cipher_decryption(self, message, mapped_key):
        pass


class Cipher(AbstractClass):

    def getUserInput(self):
        print("Key and message must be fully alphabetic")
        choice = int(input("1. Encryption\n2. Decryption\nChoice:  "))
        message, mapped_key = self.msg_and_key()

        if choice == 1:
            print("-" * 20)
            print("-------- Encryption -------")
            print("-" * 20)
            self.cipher_encryption(message, mapped_key)

        elif choice == 2:
            print("-" * 20)
            print("-------- Encryption -------")
            print("-" * 20)
            self.cipher_decryption(message, mapped_key)

        else:
            print("Wrong choice")

    def msg_and_key(self):

        msg = input("Enter message: ").upper()
        key = input("Enter key: ").upper()

        # variable to store mapped key
        key_map = ""

        j = 0
        for i in range(len(msg)):
            if ord(msg[i]) == 32:
                # ignore space
                key_map += " "
            else:
                if j < len(key):
                    key_map += key[j]
                    j += 1
                else:
                    j = 0
                    key_map += key[j]
                    j += 1

        print(key_map)
        return msg, key_map

    def create_vigenere_table(self):

        table = []
        for i in range(26):
            table.append([])

        for row in range(26):
            for column in range(26):
                if (row + 65) + column > 90:
                    # move back to letter A after Z
                    # after first row, each letter will shift to the left by one position
                    # compared to the row above it
                    table[row].append(chr((row + 65) + column - 26))
                else:
                    table[row].append(chr((row + 65) + column))

        # printing the table
        # for row in table:
        #     for column in row:
        #         print(column, end=" ")
        #     print(end="\n")

        return table

    def cipher_encryption(self, message, mapped_key):
        table = self.create_vigenere_table()
        encrypted_text = ""

        for i in range(len(message)):
            if message[i] == chr(32):
                # ignoring spacing
                encrypted_text += " "
            else:
                # getting an element at a specific index of the table
                row = ord(message[i]) - 65
                column = ord(mapped_key[i]) - 65
                encrypted_text += table[row][column]

        print("Encrypted message: {}".format(encrypted_text))

    def itr_count(self, mapped_key, message):
        counter = 0
        result = ""

        # starting alphabets from mapped_key letter and finishing all 26 letters from it , (after z we move to a)
        for i in range(26):
            if mapped_key + i > 90:
                result += chr(mapped_key + (i - 26))
            else:
                result += chr(mapped_key + i)

        # counting the number of iterations it takes from mapped kek letter to ciphertext letter
        for i in range(len(result)):
            if result[i] == chr(message):
                break
            else:
                counter += 1

        return counter

    def cipher_decryption(self, message, mapped_key):
        # table = create_vigenere_table()
        decrypted_text = ""

        for i in range(len(message)):
            if message[i] == chr(32):
                # ignoring space
                decrypted_text += " "
            else:
                # adding number of iterations it takes to reach from mapped_key
                # to cipher letter in 65
                # by doing so we get a column header of ciphertext letter, which happens
                # to be a decrypted letter
                decrypted_text += chr(65 + self.itr_count(ord(mapped_key[i]), ord(message[i])))

        print("Decrypted message: {}".format(decrypted_text))


f = Cipher()
f.getUserInput()
