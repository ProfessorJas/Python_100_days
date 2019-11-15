# prompt -> no default value
# retries -> default value: 4
# reminder -> default value: 'Please try again!'
def def_param_fun(prompt, retries = 4, reminder='Please try again!'):
    while True:
        ok = input(prompt)      # get kbd input

        if ok in ('y', 'ye', 'yes'):
            return True
        
        if ok in ('n', 'no', 'nop', 'nope'):
            return False

        retries -= 1

        if retries < 0:
            raise ValueError('Invalid user response')

        print(reminder)

if __name__ == "__main__":
    def_param_fun('Do you really wanna quit?')      

    def_param_fun('Do you really wanna quit?', 2)

    def_param_fun('Do you really wanna quit?', 2, 'Just type yes or no!!')

    # def_param_fun()       # ERROR! need at least one parameter for 'prompt'