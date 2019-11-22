try:
    from pickle import dump, load

    ## Define User class, uname -> Username, pwd -> Password
    class User:
        def __init__(self, uname=None, pwd=None):
            self.uname = uname
            self.pwd = pwd

        # update() method to modify the username and password
        def update(self, uname, pwd):
            self.uname = uname
            self.pwd = pwd

        # __repr() method is the toString() method
        def __repr__(self):
            return 'username = %s\tpassword = %s' % (self.uname, self.pwd)

        # User ends

    ## showall() method show the registered user info
    def showall():
        global userlist         # Declare using global userlist

        if len(userlist) == 0:
            print('\tThere is no user!')
        else:
            print('\tRegistered User are Listed below')

            n = 0

            for x in userlist:
                n += 1
                print('\t%s. ' % n, x)

        input('\n\tPress Enter to Continue...\n')
        ## showall() ends

    ## check_update()
    def check_update():
        global userlist         # declare global userlist
        
        uname = input('\t Please enter the name you would like to search: ')

        index = find(uname)

        if index == -1:
            print('\t%s does not exist!' % uname)
        else:
            # User has already registered. Modify or Delete
            print('\t%s has registered!')
            print('\tPlease select the option: ')
            print('\t 1. Modify the user')
            print('\t 2. Delete the user')

            op = input('\t Please enter the corresponding number: ')

            if op == '2':
                # Delete the user
                del userlist[index]
                print('Delete Successfully...')
            else:
                # Modify the user
                uname = input('\tPlease enter the new username')

                if uname == '':
                    print('Invalid Username!')
                else:
                    # check whether has the existed username
                    if find(uname) >= -1:
                        print('\tUsername has already existed!')
                    else:
                        pwd = input('\tPlease enter the password: ')
                        if pwd == '':
                            print('Invalid password!')
                        else:
                            userlist[index].update(uname, pwd)
                            print('\n\tSucceed in Modifing the User')

        input('\n\t Press Enter to Conitnue...\n')
        ## check_update() finishes

    ## adduser() adds new user
    def adduser():
        global userlist             # declare userlist
        
        uname = input('\t Please enter the username')

        if uname == '':
            print('\tInvalid username')
        else:
            # check duplicates
            if find(uname) > -1:
                print('Username existed...')
            else:
                pwd = input('\tPlease Enter the new password')

                if pwd == '':
                    print('\tInvalid password')
                else:
                    userlist.append(User(uname, pwd))
                    print('\Succeed in Adding a new User!')

        input('\n\t press Enter to Continue')
        ## adduser() method finishes

    ## find(namekey) check whether there exists a user with the username namekey
    def find(namekey):
        global userlist         # Using the global list object

        n = -1

        for x in userlist:
            n += 1
            if x.uname == namekey:
                break
            else:
                n = -1
            
            return n
        
        ## find() ends

    ## save() method saves the current user info
    def save():
        global userlist

        myfile = open(r'userdata.bin', 'wb')        # open the file
        dump(userlist, myfile)                      # write the dictionary object to the file
        myfile.close()                              # close the file

        print('\tSucceed in Saving the User Info')
        input('\n\tPress Enter to Continue...')

    # when the program starts, load the user data
    myfile = open(r'userdata.bin', 'rb')            # open the file
    x = myfile.read()                               # read a byte and check whether the file is empty or not

    if x == b'':
        myfile.seek(0)
        userlist = load(myfile)                     # load the userlist from the file

    myfile.close()                                  # close the file

    # User the infinite loop to show the menu
    while True:
        print('User System')
        print('\t1. Show All Registered User')
        print('\t2. Search/Modify/Delete User Info')
        print('\t3. Add New User')
        print('\t4. Save User Info')
        print('\t5. Quit')

        no = input('Please enter the number: ')

        if no == '1':
            showall()               # Show all info
        elif no == '2':
            check_update()          # Excute search/modify/delete command
        elif no == '3':
            adduser()               # Add new user
        elif no == '4':             
            save()                  # Save user info
        elif no == '5':
            print('Thank you!')
            break
except Exception as ex:
    from traceback import print_tb      # import print_tb to print err message
    from datetime import datetime       # import datetime to write to the log

    log = open('Logging_Error.txt', 'a')    # open the log
    x = datetime.today()                # get the current date

    # log info
    print('\nError...')
    print('Date: ', x)
    print('Error info: ', ex)
    print('Backtracing...:')
    print_tb(ex.__traceback__)

    # Write to log
    print('\nError: ', file=log)
    print('Date: ', x, file=log)
    print('Error Info: ', ex.args[0], file=log)
    print('Stack Trace: ', file=log)

    print_tb(ex.__traceback__, file=log)

    log.close()                 # close the log
    
    print('Error happend. Quit the system')


