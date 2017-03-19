"""
Ask the user for their username. If the username is in the above list of authorised users, print “Access
granted”, otherwise print “Access denied”.
"""


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Enter username: ")
    if username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")

main()
