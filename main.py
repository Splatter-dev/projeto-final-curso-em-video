import modules.menu as menu
import modules.validacao as option
import modules.arquivo as arquivo
from pathlib import Path


optionOut = 5  # Var para iniciar o looping
filePath = Path('arquivos/')
file = filePath / 'cadastro.txt'


if not arquivo.fileExists(file):
    arquivo.createFile(file)


while optionOut != 4 or optionOut == None:
    """[
        O valor 4 atribuido a optionOut é só para iniciar o looping
        O None é passado como parametro pelo retorno da função optionValidation
        Enquanto for None o looping continua, se não é opção 3, quebra o looping e encerra o programa
    ]
    """
    menu.mainMenu()
    optionSelected = option.optionValidation("Digite uma opção:")
    menu.subMenus(optionSelected, file)
    if optionSelected == 4:
        optionOut = 4
    if optionSelected == None:
        optionOut = None

