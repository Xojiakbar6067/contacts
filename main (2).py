contact=['+998989889889','+998909909909','+998946600666', ]

while True:
    print('_____________________________','\n''1-добавит контакты', '\n''2-удалит контакты', '\n''3-изменит контакты', '\n''4-показат контакты','\n''5-остоновит программу')
    operator=int(input('выбирайте: '))

    if operator==1:
        add_to_contact=input('добавте контакт: ')
        contact.append(add_to_contact)
        print('\n''контакт', add_to_contact, 'добавлен')
    elif operator==2:
        a=len(contact)
        delete_contact=int(input('выберите номер контакта: '))
        if delete_contact<=a:
            contact.pop(delete_contact-1)
            print('\n''контакт под номером', delete_contact, 'удален')
        else:
            print(f'контакт под номером {delete_contact} нету в нашем списке')
    elif operator==3:
        a = len(contact)
        change_contact=int(input('укажите номер изменяемого: '))
        if change_contact<=a:
            contact[change_contact-1]=input('на что изменит: ')
            print('\n''контакт под номером', change_contact, 'изменён')
        else:
            print(f'контакт под номером {change_contact} нету в нашем списке')
    elif operator==4:
        k=0
        for i in contact:
            k+=1
            print(f'{k}).........{i}')
    elif operator==5:
        break
    else:
        print('не правилный указ')