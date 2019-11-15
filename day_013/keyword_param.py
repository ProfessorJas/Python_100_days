def key_fun(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This function wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

if __name__ == "__main__":
    key_fun(voltage=1000)           # 1 keyword argument

    key_fun(1234, 'jajaja')           # 2 positional arguments

    key_fun(voltage=1234567, action="VOOOOOOOOOOM")     # 2 keyword arguments

    key_fun(action="VOOOOOOOOOOM", voltage=1234567)     # 2 keyword arguments

    key_fun('a million', 'bereft of life', 'jump')      # 3 positional arguments

    key_fun('a thousand', state="pushing up the daisies")   # 1 positional, 1 keyword