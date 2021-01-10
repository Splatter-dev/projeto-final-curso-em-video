import modules.colours as colour


def optionValidation(msg):
    """[Validação da opção selecionada]

    Args:
        msg ([str]): [Mensagem para selecionar a opção]

    Returns:
        [Int/None]: [Retorna None se não passar na validação]
    """
    while True:
        try:
            optionSelected = int(input(f"{colour.yellow(msg)} "))
        except (ValueError, TypeError):
            print(
                f"{colour.red('ERRO: Por favor, digite um número inteiro válido. ')}")
            return None
            break
        if optionSelected > 4 or optionSelected < 1:
            print(f"{colour.red('ERRO: Por favor, digite uma opção válida. ')}")
            return None
            break
        else:
            return optionSelected
            break


def intValidation(msg):
    """[Validação da Idade]

    Args:
        msg ([str]): [Passa a mensagem de entrada "Idade:"]

    Returns:
        [type]: [Retorna um valor de idadr(int) validado. Não pode ser menor que 0]
    """
    while True:  # Primeiro looping(principal) avalia se a variavel age tem algum except, se não for quebra o looping.
        try:
            while True:  # Segundo looping avalia se a var age é menor que 0, se não for quebra o looping.
                age = int(input(f"{colour.yellow(msg)} "))
                if age < 0:
                    print(
                        f"{colour.red('ERRO: Por favor, digite números correspondentes a idade. ')}")
                else:
                    break
        except (ValueError, TypeError):
            print(
                f"{colour.red('ERRO: Por favor, digite números correspondentes a idade. ')}")
        else:
            return age
            break


def strValidation(msg):
    """[Validação do nome]

    Args:
        msg ([str]): [Passa a mensagem de entrada "Nome:"]

    Returns:
        [str]: [Retorna o nome validado]
    """
    while True:
        try:
            name = str(input(f"{colour.yellow(msg)} ")).strip()
            # Remove os espaços entre os nomes, exep: JoseCarlos
            nameWithoutSpace = name.replace(" ", "")
        except (ValueError, TypeError):
            print(f"{colour.red('ERRO: Por favor, digite o nome novamente.')}")
        if not nameWithoutSpace.isalpha():  # Verifica é alphanumerico(ABCÁ...Z)
            print(f"{colour.red('ERRO: Por favor, verifique o nome digitado.')}")
        else:
            return name
            break


def idToDeleteValidation(msg):
    """[Validação da Idade]

    Args:
        msg ([str]): [Passa a mensagem de entrada "Idade:"]

    Returns:
        [type]: [Retorna um valor de idadr(int) validado. Não pode ser menor que 0]
    """
    while True:
        try:
            while True:
                age = int(input(f"{colour.yellow(msg)} "))
                if age < 0:
                    print(
                        f"{colour.red('ERRO: Por favor, digite números correspondentes aos ids. ')}")
                else:
                    break
        except (ValueError, TypeError):
            print(
                f"{colour.red('ERRO: Por favor, digite números correspondentes aos ids. ')}")
        else:
            return age
            break
