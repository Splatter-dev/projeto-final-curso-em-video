import modules.colours as colour


def fileExists(fileName):
    """[Verifica se o arquivo existe]

    Args:
        fileName ([str]): [nome do arquivo a ser criado]

    Returns:
        [boolean]: [retorna True se o arquivo existir]
    """
    try:
        fileOpen = open(fileName, 'rt')
        fileOpen.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(fileName):
    """[Cria o arquivo se não existir]

    Args:
        fileName ([str]): [nome do arquivo]
    """
    try:
        createFile = open(fileName, 'wt+')
        createFile.close()
    except:
        print(f'{colour.red(f"Houve um erro ao criar o arquivo {fileName}")}')
    else:
        print(f'\n{colour.green(f"Arquivo {fileName} criado com sucesso.")}')


def openFile(fileName):
    """[Abre o arquivo]

    Args:
        fileName ([str]): [nome do arquivo]

    Returns:
        [type]: [Armazena numa lista em redlines e retorna]
    """
    try:
        fileOpen = open(fileName, 'rt')
    except:
        print("Erro ao ler o arquivo :(")
    else:
        openedFile = fileOpen.readlines()
        return openedFile
    finally:
        fileOpen.close()


def overWriteFile(fileName):
    """[Abre o arquivo em modo de escrita/sobre-escrita]

    Args:
        fileName ([nome do arquivo]): [description]

    Returns:
        [metodo]: [Metodo de sobre-escrever o arquivo(apaga tudo o que tem neme)]
    """
    try:
        overWriteFile = open(fileName, 'wt')
    except:
        print("Erro ao ler o arquivo :(")
    else:
        return overWriteFile


def readFile(fileName, show=""):
    openedFile = openFile(fileName)
    idGenerateId = 0
    for line in openedFile:
        valueRegistry = line.split(";")
        valueRegistry[2] = valueRegistry[2].replace("\n", "")
        idPerson = int(valueRegistry[0])
        name = valueRegistry[1]
        age = valueRegistry[2]
        if idPerson > idGenerateId:
            idGenerateId = idPerson
        if show:
            showData(idPerson, name, age)
    return idGenerateId


def showData(idPerson, name, age):
    print(
        f"{idPerson:<3}{name:<45}{age:>3} anos")


def idGenerate(fileName):
    """[Gera um ID para o cadastro a ser adicionado]

    Args:
        idPerson ([type]): [description]
        fileName ([type]): [description]

    Returns:
        [type]: [description]
    """
    idRegistry = readFile(fileName)
    try:
        idRegistry += 1
    except:
        print(f'{colour.red("Erro ao gerar o id")}')
    finally:
        return idRegistry


def registerPerson(fileName, idPerson, name='Desconhecido', age=0):
    try:
        registerPerson = open(fileName, 'at')
    except:
        print("Houve um erro na abertura do arquivo.")
    else:
        try:
            registerPerson.write(f"{idPerson};{name};{age}\n")
        except:
            print("Houve um erro ao registrar as informações.")
        else:
            personRregistred = str(
                f'\n{colour.purple(f"Novo registro de {name} cadastrado com sucesso.")}')
            return personRregistred
        finally:
            registerPerson.close()


def delRegistry(fileName, delId):
    count = 0
    try:
        openedFile = openFile(fileName)
        registerOverWrite = overWriteFile(fileName)
    except:
        print("Houve um erro na abertura do arquivo.")
    else:
        for pos, registry in enumerate(openedFile):
            if registry.find(f"{delId};") == 0:
                print(registry)
                openedFile.pop(pos)
            else:
                count += 1
                if count == len(openedFile):
                    print(
                        f"{colour.red(f'Nenhuma pessoa cadastrada com o id {delId}. Tente novamente.')}")
        for pos, registry in enumerate(openedFile):
            valueRegistry = registry.split(";")
            registerOverWrite.write(
                f"{valueRegistry[0]};{valueRegistry[1]};{valueRegistry[2]}")
    finally:
        registerOverWrite.close()
