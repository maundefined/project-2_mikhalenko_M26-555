import prompt

def welcome():
    """Приветствие и справочная информация."""
    print("Первая попытка запустить проект!\n***\n")

    while True:
        print("<command> exit - выйти из программы")
        print("<command> help - справочная информация")
        command = prompt.string("Введите команду: ")

        if command == "exit":
            break
        elif command == "help":
            print()