import pyautogui
import time
import pyperclip
from PIL import Image
import pyscreeze
import pyttsx3
import pywintypes

#Configurando a engine de Text-To-Speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  
engine.setProperty('rate', 200)

pyautogui.PAUSE = 0.3
pyautogui.useImageNotFoundException()
#print(pyautogui.position())

MARCAS = {
    '1':'bosch',
    '72908817000416':'bosch',
    '72908817000173':'bosch',
    '145':'ascoval',
    '85203925000788':'ascoval',
    0:'ninguem',
    '98':'bosch',
    '166':'ascoval',
    '43021906000103':'ascoval',
    '15':'wika'
    }
GRUPOS = ['5','8','2','10027','10028','1','10000','9','10009','6','10010','3','4','10043','10002','10034']
SUBGRUPOS_INAT = {
    '5':['34','40','33','36','57','17','19','50','48'],
    '1':['10'],
    '10000':['29'],
    '6':['24','19']
    }
SUBGRUPOS_ALTER = {
    ('5','34'):'5'
    }
GRUPOS_INAT = ['9999', '10020','10004','10011']
CODIGOS = {
    'bosch': {
        '5': '10',
        '8': '61',
        '2': '13',
        '1': '12'
    },
    'ascoval': {
        '8': '61'
    },
    'wika': {
        '2': '43'
    },
    'ninguem': {
        '5': '47',
        '8': '48',
        '2': '49',
        '10027': '21',
        '10028': '59',
        '1': '50',
        '10000': '59',
        '9': '14',
        '10009':'60',
        '6':'17',
        '10010':'60',
        '3':'26',
        '4':'8',
        '10043':'38',
        '10002':'11',
        '10034':'39'
    }
}

#Começo do programa
pyautogui.click(x=603, y=1058)
#Looping do programa
while True:
    pyautogui.press('f3')
    time.sleep(15)
    try:
        pyautogui.locateCenterOnScreen('manutencao_produtos.png', confidence=0.8)
    except pyautogui.ImageNotFoundException:
        print("Erro! Tela de manutenção de produtos não encontrada.")
        engine.say("Erro, tela de manutenção de produtos não encontrada.")
        engine.runAndWait()
        aviso = pyautogui.confirm('Deseja continuar?', buttons=['Sim', 'Não'])
        if aviso == 'Sim':
            print("Continuando a execução...")
            continue
        else:
            print("Execução interrompida.")
            break
    #pyautogui.hotkey('ctrl', 'c')
    #produto = pyperclip.paste()
    try:
        marca = pyautogui.locateCenterOnScreen('marca.png', confidence=0.8)
        #pyautogui.click(marca)
    except pyautogui.ImageNotFoundException:
        #Marca possui conteúdo
        pyautogui.doubleClick(x=311, y=220)
        pyautogui.hotkey('ctrl', 'c')
        marca = pyperclip.paste()
    else:
        try:
            codigo = pyautogui.locateCenterOnScreen('codigo.png', confidence=0.8)
        except pyautogui.ImageNotFoundException:
            #Marca possui conteúdo
            pyautogui.doubleClick(x=35, y=366)
            pyautogui.hotkey('ctrl', 'c')
            marca = pyperclip.paste()
        else:
            marca = 0
    acao = True
    if marca in MARCAS.keys():
        pyautogui.doubleClick(x=321, y=134)
        pyautogui.hotkey('ctrl', 'c')
        grupo = pyperclip.paste()
        if grupo in GRUPOS:
            pyautogui.press('tab')
            pyautogui.hotkey('ctrl', 'c')
            subgrupo = pyperclip.paste()
            if subgrupo not in SUBGRUPOS_INAT.get(grupo, []):
                pyautogui.press('tab')
                marca_nome = MARCAS[marca]
                try:
                    pyautogui.write(CODIGOS[marca_nome][grupo])
                except KeyError:
                    pyautogui.write(CODIGOS['ninguem'][grupo])
                finally:
                    pyautogui.press('tab')
                    acao = False
            else:
                if (grupo, subgrupo) in SUBGRUPOS_ALTER.keys():
                    pyautogui.write(SUBGRUPOS_ALTER[(grupo, subgrupo)])
                    pyautogui.press('tab')
                    try:
                        pyautogui.write(CODIGOS[marca_nome][grupo])
                    except KeyError:
                        pyautogui.write(CODIGOS['ninguem'][grupo])
                    finally:
                        pyautogui.press('tab')
                        acao = False
                else:
                    print('Subgrupo cadastrado é INATIVO!')
                    engine.say("Subigrupo cadastrado é INATIVO!")
                    engine.runAndWait()
        else:
            if grupo in GRUPOS_INAT:
                print('Grupo cadastrado é INATIVO!')
                engine.say("Grupo cadastrado é INATIVO!")
                engine.runAndWait()
            else:
                print('Grupo cadastrado não listado.')
                engine.say("Grupo cadastrado não listado.")
                engine.runAndWait()
    else:
        print('Marca cadastrada não listada.')
        engine.say("Marca cadastrada não listada.")
        engine.runAndWait()
    if acao:
        aviso = pyautogui.confirm('Deseja continuar?', buttons=['Sim', 'Não'])
        if aviso == 'Sim':
            print("Continuando a execução...")
            pyautogui.press('f5')
            time.sleep(2)
            try:
                erro = pyautogui.locateCenterOnScreen('erro do ncm 0.png', confidence=0.8)
                pyautogui.press('enter')
                pyautogui.click(x=542, y=250)
                pyautogui.doubleClick(x=445, y=432)
                pyautogui.write('0')
                pyautogui.press('f5')
                time.sleep(6)
            except pyautogui.ImageNotFoundException:
                time.sleep(4)
        else:
            print("Execução interrompida.")
            break
    else:
        pyautogui.press('f5')
        time.sleep(2)
        try:
            erro = pyautogui.locateCenterOnScreen('erro do ncm 0.png', confidence=0.8)
            pyautogui.press('enter')
            pyautogui.click(x=542, y=250)
            pyautogui.doubleClick(x=445, y=432)
            pyautogui.write('0')
            pyautogui.press('f5')
            time.sleep(6)
        except pyautogui.ImageNotFoundException:
            time.sleep(4)
