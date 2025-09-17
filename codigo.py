import pyautogui
import time

#pyautogui.click -> clicar em alum lugar
#pyautogui.press -> apertar 1 tecla
#pyautogui.write -> escrever um texto
#pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 0.5

#Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# digitar o site
pyautogui.write(" https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 2: Fazer login
# preencher email
pyautogui.click(x=448, y=413)
pyautogui.write("claytonfranca.fs@gmail.com")

# preencher a senha
pyautogui.press("tab")
pyautogui.write("senhasecreta")

# Botão logar
pyautogui.press("tab")
pyautogui.press("enter")

# espera de 3s
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas 

tabela = pandas.read_csv("produtos.csv")

    
print(tabela)

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    pyautogui.click(x=492, y=294)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") #Passar para o proximo compo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") #Passar para o proximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])     
    
    pyautogui.write(custo)  


    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)


    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos



