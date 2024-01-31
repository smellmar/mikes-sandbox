alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_index = []
for i in alphabet:
    alphabet_index.append(i)

chars = " ", "!", "?", ",", ".", ":", "-", "=", "+", "/", "*", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", """'""", '''"''', "[", "]", ">", "<"

all_chars = ""
for i in chars:
    all_chars += i
for i in alphabet_index:
    all_chars += i
# print(all_chars)


# PYTHON TOOLS--
def to_clipboard(tocopy):
    import pyperclip
    copied = str(tocopy)
    pyperclip.copy(copied)


# AUTHOR MIKE DELMAR 2024 [>.<]
# ----------
# LOCKER--
def vigenere(message, key, lock=True):
    print("\n")
    print(""""il derevigenere" the only app that lets you vigenere, devigenere, and revigenere venered and unvigenered strings""")
    print("----------")
    message = str(input("[enter message to encode][abc][123][!?/]: "))
    key = str(input("[enter keyword][abc]: "))
    for a in key:
        if alphabet.find(a) >= 0:
            continue
        else:
            print("\n")
            print("[invalid][accepts abc only]\n/restarting...\n")
            print("\n")
            vigenere(message, key, True)
    dere = str(input("[devigenere or reviginere][d/r]: "))
    if dere == "d" or dere == "D":
        lock = True
    elif dere == "r" or dere == "R":
        lock = False
    else:
        print("\n")
        print("[invalid][accepts d/r only]\n/restarting...\n")
        print("\n")
        vigenere(message, key, True)
    
    print("\n")
    print("/encrypting your message...\n---")
    keystone = ""
    
    # Prepares strings, inserts [>.<] where character is unknown--
    message_lower = message.lower()
    message = ""
    for i in message_lower:
        if all_chars.find(i) >= 0:
            message += str(i)
        else:
            message += "[>.<]"

    key = key.lower()

    # Gets alphabet index value of each character in given message--
    message_index = []
    for i in message:
        if alphabet.find(i) >= 0:
            message_index.append(alphabet.find(i))
        else:
            continue
    # print("orig. index:\t", message_index)

    # Prepares keystone length to match given message--
    for i in range(0, len(message), len(key)):
        keystone += key
    keystone = keystone[:len(message)]

    # Cuts keystone into keycode, inserting key letter alphabet index values--
    keycode = []
    for i in keystone:
        keycode.append(alphabet.find(i))
    # print("keycode:\t", keycode)

    # LOCK--
    if lock == False:
        # Subtracts keystone index value from message index value--
        key_turn_lock = []
        for i in range(len(message_index)):
            x = message_index[i] - keycode[i]
            if x < 0:
                key_turn_lock.append(len(alphabet)+x)
            else:
                key_turn_lock.append(x)
        # print("combined:\t", key_turn_lock)

        # Converts result into corresponding letters based on alphabet--
        letters = []
        for i in key_turn_lock:
            letters.append(alphabet[i])
        # print("converted:\t", letters)
    
    # UNLOCK
    else:
        # Adds keystone index value to message index value--
        key_turn_unlock = []
        for i in range(len(message_index)):
            x = message_index[i] + keycode[i]
            if x > 25:
                key_turn_unlock.append(x-len(alphabet))
            else:
                key_turn_unlock.append(x)
        # print("combined:\t", key_turn_unlock)

        # Converts result into corresponding letters based on alphabet--
        letters = []
        for i in key_turn_unlock:
            letters.append(alphabet[i])
        # print("converted:\t", letters)

    # Reassembles sentence interting {chars} before returning to string--
    for i in range(len(message)):
        for j in chars:
            if message[i] == j:
                letters.insert(i, message[i])
            else:
                continue

    # Prints encrypted message and saves it to user's clipboard--
    your_message = ""
    for i in letters:
        your_message += str(i)
    to_clipboard(your_message)
    print("[your encrypted message is]:\t"+ your_message + "\n")
    print("[your key word is]:\t"+ key + "\n")
    print("\n")
    print("/copied message to clipboard\n")
    print("\n")
    vigenere("message", "key", True)

vigenere("message", "key", True)