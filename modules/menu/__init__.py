import modules.colours as colour
import modules.file_func as file
import modules.validation as validation
from time import sleep


def mainMenu():
    sleep(.5)
    print("-"*60)
    print("MENU PRINCIPAL".center(60))
    print("-"*60)
    print(f"{colour.yellow('1')} - {colour.blue('Ver pessoas cadastradas')}")
    print(f"{colour.yellow('2')} - {colour.blue('Cadastrar nova pessoa')}")
    print(f"{colour.yellow('3')} - {colour.blue('Deletar um cadastro')}")
    print(f"{colour.yellow('4')} - {colour.blue('Sair do sistema')}")
    print("-"*60)


def subMenus(option, fileName=""):
    if option == 1:
        sleep(.5)
        print("-"*60)
        print(f"PESSOAS CADASTRADAS".center(60))
        print("-"*60)
        file.readFile(fileName, show=True)
    elif option == 2:
        sleep(.5)
        print("-"*60)
        print(f"NOVO CADASTRO".center(60))
        print("-"*60)
        name = validation.strValidation("Nome: ")
        age = validation.intValidation("Idade: ")
        idPerson = file.idGenerate(fileName)
        registredPerson = file.registerPerson(fileName, idPerson, name, age)
        print(registredPerson)
    elif option == 3:
        sleep(.5)
        print("-"*60)
        print(f"APAGAR CADASTRO".center(60))
        print("-"*60)
        registry = file.readFile(fileName, show=True)
        idToDelete = validation.intValidation(
            "\nDigite o número do cadastro que você deseja apagar: ")
        file.delRegistry(fileName, idToDelete)
    elif option == 4:
        sleep(.5)
        print("-"*60)
        print(f"Saindo do sistema... Até logo :)".center(60))
        print("-"*60)
