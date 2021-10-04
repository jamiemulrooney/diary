import diary

selection = 0
while selection != '5':
    print('1. Add an entry')
    print('2. Display all entries')
    print('3. Display today\'s entries')
    print('4. Display this month\'s entries')
    print('5. Exit')


    selection = input('Choose option 1 - 5: ')

    if selection == '1':
        message = input('Enter message: ')   
        d = int(input('Enter day: '))     
        m = int(input('Enter month: '))     
        y = int(input('Enter year: '))

        t = input('Enter event type: single / group')
        names = []
        if t == 'group':
            name = ''
            while name != 'STOP':
                name = input('Enter name (STOP to end): ')
                names.append(name)

            # Remove the last name which will be STOP
            del names[-1]
        diary.add_entry(message, d, m, y, t, names)

    elif selection == '2':
        diary.display_all_entries()
        
    elif selection == '3':   
        d = int(input('Enter day: '))     
        m = int(input('Enter month: '))     
        y = int(input('Enter year: '))  
        diary.display_todays_entries(d, m, y)
    
    elif selection == '4':   
        m = int(input('Enter month: '))     
        y = int(input('Enter year: '))  
        diary.display_months_entries(m, y)




    

    
        
        
        
    
    
