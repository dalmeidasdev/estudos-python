# Colocando cores no terminal
# Link do vídeo: https://youtu.be/0hBIhkcA8O8?si=Fy54QB276sanCWSq

# Sempre que quiser representar uma cor em Python sem usar módulos use \033[estilo; texto; fundo m

# Estilos:                           # Cores                    # Fundo
# 0: sem estilo                      # 30: Branco               # 40: Branco
# 1: negrito                         # 31: Vermelho             # 41: Vermelho
# 4: underline                       # 32: Verde                # 42: Verde
# 7: inverte texto com o fundo       # 33: Amarelo              # 43: Amarelo
                                     # 34: Azul                 # 44: Azul
                                     # 35: Magenta              # 45: Magenta
                                     # 36: Ciano                # 46: Ciano
                                     # 37: Cinza                # 47: Cinza

print('\033[0;30;41mTeste\033[m')
print('\033[4;33mTeste\033[m')