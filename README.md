# autorun-algorithm

A infecção por autorun é um tipo de ataque que se aproveita da funcionalidade de autorun de dispositivos de armazenamento, como pen drives ou discos externos, para instalar malware no dispositivo alvo sem o conhecimento ou consentimento do usuário.
Esse código cria um arquivo autorun.inf com instruções para abrir o arquivo malicioso e copia esse arquivo e o arquivo malicioso para um pen drive. 
Quando o pen drive é conectado a um dispositivo alvo, o arquivo autorun.inf é lido e o arquivo malicioso é executado, infectando o dispositivo.
