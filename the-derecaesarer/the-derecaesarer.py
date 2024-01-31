print("\n")
print("the derecaesarer: a program to caesar, decaesar or recaesar decaesared, recaesared or otherwise caesared strings.\n----------\n")

# GLOBALS
alphabet = "abcdefghijklmnopqrstuvwxyz"
allowed_chars = "1234567890 !?.,!@#$%^&*()_+'-=[]|:" 

def to_clipboard(tocopy):
    import pyperclip
    copied = str(tocopy)
    pyperclip.copy(copied)


# DECAESAR ---
def decaesar(message, n):
    decaesared = ""
    cipherbet = alphabet[-n:] + alphabet[:-n]
    for i in message:
        if allowed_chars.find(i) >= 0:
            decaesared += i
        else:
            cypher_pos = cipherbet.find(i)
            alpha_letter = alphabet[cypher_pos]
            decaesared += alpha_letter
    return decaesared


# RECAESAR ---
def recaesar(message, n):
    recaesared = ""
    cipherbet = alphabet[-n:] + alphabet[:-n]
    for i in message:
        if allowed_chars.find(i) >= 0:
            recaesared += i
        else:
            alpha_pos = alphabet.find(i)
            cipher_letter = cipherbet[alpha_pos]
            recaesared += cipher_letter
    return recaesared


# # TESTS ---
# encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
# print("decaesared: ", decaesar(encoded_message, 10))
# print("\n")

# print("new message with clue: ", decaesar("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))
# print("\n")

# print("second message offset 14: ", decaesar("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))
# print("\n")


# PROGRAM WITH USER INPUTS --
def start():
    which_caeser = str(input("[decaesar or recaesar (d/r)]?: "))
    if which_caeser == "D" or which_caeser == "d":
        decaesarer()
    elif which_caeser == "R" or which_caeser == "r":
        recaesarer()
    else:
        print("""\n[invalid input]\n[accepts "d" or "r" only]\n""")
    start()

def recaesarer():
    print("\n")
    print("/receasarer\n-----")
    message = str(input("""[message to recaesar]: """)).lower()
    for i in message:
        if allowed_chars.find(i) >= 0 or alphabet.find(i) >= 0:
            n = int(input("[value shift][enter '1-25' or '0' for all]: "))
            if n > 0 and n < 26:
                print("\n")
                print("/recaesaring...\n---")
                print("[your recaesared message is]: " + recaesar(message, n))
                print("[shift]: " + str(n) + "\n---")
                print("\n")
                to_clipboard(recaesar(message, n))
                print("/saved to clipboard")
                print("\n")
                break
            elif n == 0:
                print("\n")
                print("/recaesaring 25 times...\n---")
                for x in range(len(alphabet)):
                    print("[shift: " + str(x) + "][your recaesared message is]: " + recaesar(message, x))
                print("\n")
                select = int(input("[enter 1-25 to select]: "))
                for y in range(len(alphabet)):
                    if select > 0 and select < 26:
                        if y == select:
                            print("\n")
                            print("/saved [shift: " + str(y) + "] to clipboard")
                            to_clipboard(recaesar(message, y))
                            print("\n")
                            start()
                        else:
                            continue
                    else:
                        print("""\n[invalid input]\n[only accepts 1 - 25]\n""")
                        recaesarer()
            else:
                print("""\n[invalid input]\n[only accepts 1 - 25]\n""")
                recaesarer()
        else:
            print("""\n[invalid input]\n[allowed characters '""" + str(alphabet) + """' and '""" + str(allowed_chars) + """']\n""")
            recaesarer()
    start()

def decaesarer():
    print("\n")
    print("/deceasarer\n-----")
    message = str(input("""[message to decaesar]: """)).lower()
    for i in message:
        if allowed_chars.find(i) >= 0 or alphabet.find(i) >= 0:
            n = int(input("[value shift][enter '1-25' or '0' for all]: "))
            if n > 0 and n < 26:
                print("\n")
                print("/decaesaring...\n---")
                print("[your decaesared message is]: " + decaesar(message, n))
                print("[shift]: " + str(n) + "\n---")
                print("\n")
                to_clipboard(decaesar(message, n))
                print("/saved to clipboard")
                print("\n")
                break
            elif n == 0:
                print("\n")
                print("/decaesaring 25 times...\n---")
                for x in range(len(alphabet)):
                    print("[shift: " + str(x) + "][your decaesared message is]: " + decaesar(message, x))
                print("\n")
                select = int(input("[enter 1-25 to select]: "))
                for y in range(len(alphabet)):
                    if select > 0 and select < 26:
                        if y == select:
                            print("\n")
                            print("/saved [shift: " + str(y) + "] to clipboard")
                            to_clipboard(decaesar(message, y))
                            print("\n")
                            start()
                        else:
                            continue
                    else:
                        print("""\n[invalid input]\n[only accepts 1 - 25]\n""")
                        decaesarer()
            else:
                print("""\n[invalid input]\n[only accepts 1 - 25]\n""")
                decaesarer()
        else:
            print("""\n[invalid input]\n[allowed characters '""" + str(alphabet) + """' and '""" + str(allowed_chars) + """']\n""")
            decaesarer()
    start()

start()