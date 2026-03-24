def shut_down():
    print("system is shutting down...")
def restart():
    print("restarting....")
def choice():
    print("1.shutdown")
    print("2.restart")
    choice=input("enter your choice:")
    if choice=="1":
        shut_down()
    elif choice=="2":
        restart()
    else:
        print("invalid choice")
choice()