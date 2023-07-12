contacts = {'Duda': '+3806666666666', 'Budanov': '+380999999999'}


def main():
    while True:
        
        request = input().lower()
        if request == "good bye" or request == "close" or request == "exit":
            print('Good bye!')
            break
        elif request == "hello":
            print("How can I help you?")
        elif request == 'show all':
            print('show all')
        
        if request.split(' ')[0] == 'add':
            print('add')
        if request.split(' ')[0] == 'change':
            print('change')
        if request.split(' ')[0] == 'phone':
            number = find_phone_by_name(contacts, request.split(' ')[1])
            print(number)

        
def find_phone_by_name(contacts, name):
    for i in contacts:
        if i.lower() == name:
            print(contacts[i])


if __name__ == '__main__':

    main()