def variable_fun(kind, *arguments, **keywords):
    print('first args:', kind, ';')

    print("-" * 40)

    for arg in arguments:
        print(arg)

    print("-" * 40)

    for key in keywords:
        print(key, ":", keywords[key])

if __name__ == "__main__":
    variable_fun("an amigo", "hola", "adios",
            mom="amigo",
            dad="amigo",
            child="amigo")

    print("=" * 40)

    list01 = ["hello xiaoming", "nice to meet you!"]
    dict01 = {'mother': 'xiaoma', 'father': 'xiaoba', 'son': 'see you'}
    variable_fun("xiaoming", *list01, **dict01)