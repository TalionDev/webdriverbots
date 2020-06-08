#importando as parada
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import asyncio

print("os brabo")
print("bot supremo do zap pressione 1")
print("bot supremo discord pressione 2")

option = input("qual vai ser? ")
option = int(option)

if (option == 1):
    print("bot supremo do zap")
    print("para ficar mudando o seu recado pressione 1")
    print("para ficar floodando qualquer mensagem pressione 2")

    option = input("qual vai ser? ")
    option = int(option)
    if (option == 1):
        print("tu escolheu mudar o recado")
        time.sleep(1)
        driver = webdriver.Chrome()

        # abrindo o zap // nessa hora tu pega a camera de QR code do wpp web e abre o seu zap
        driver.get("https://web.whatsapp.com/")

        # cooldown brabo
        time.sleep(4)

        msg1 = input("recado q tu quer meter: ")
        msg2 = input("recado q tu quer meter: ")
        msg3 = input("recado q tu quer meter: ")

        num = input("quantas vezes: ")
        num = int(num)  # transformando a variavel num em inteiro pq o python eh pau no cu e n faz automaticamente
        a = []
        # localizando o path no html e clicando nele
        driver.find_element_by_class_name("_1BjNO").click()
        time.sleep(1)


        def cuzin():
            a = driver.find_elements_by_xpath("//span[@data-icon='pencil']")
            a[1].click()
            driver.find_element_by_xpath("//div[@contenteditable='true']").send_keys(
                Keys.BACKSPACE * 10 + msg1 + Keys.ENTER)
            time.sleep(4)
            a = driver.find_elements_by_xpath("//span[@data-icon='pencil']")
            a[1].click()
            driver.find_element_by_xpath("//div[@contenteditable='true']").send_keys(
                Keys.BACKSPACE * 10 + msg2 + Keys.ENTER)
            time.sleep(4)
            a = driver.find_elements_by_xpath("//span[@data-icon='pencil']")
            a[1].click()
            driver.find_element_by_xpath("//div[@contenteditable='true']").send_keys(
                Keys.BACKSPACE * 10 + msg3 + Keys.ENTER)
            time.sleep(4)


        i = 0
        while (i <= num):
            cuzin()
            i = i + 1
    elif (option == 2):
        print("tu escolheu floodar qualquer coisa")
        time.sleep(1)
        # falando pro selenium que eu quero uma variavel setada como webdriver usando o driver do chrome
        driver = webdriver.Chrome()

        # abrindo o zap // nessa hora tu pega a camera de QR code do wpp web e abre o seu zap
        driver.get("https://web.whatsapp.com/")

        # cooldown brabo
        time.sleep(4)

        # variaveis neh rapazeada
        i = 0  # variavel de controle padrao pro while, sim eu odeio for
        name = input('nome do contato q tu quer spammar: ')
        msg = input("msg q tu quer spammar: ")
        num = input("quantas vezes: ")
        num = int(num)  # transformando a variavel num em inteiro pq o python eh pau no cu e n faz automaticamente

        # localizando o path no html e clicando nele
        driver.find_element_by_xpath("//span[@title='" + name + "']").click()


        # criando uma funçao q localiza os path no html, enviando string e depois dando enter
        def cuzin():
            a = driver.find_elements_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")
            a[1].send_keys(" " + msg + Keys.ENTER)


        # executando a funçao ate bater o num q foi setado
        while (i <= num):
            cuzin()
            i = i + 1

elif (option == 2):
    print("bot supremo do discord")
    print("para ficar mudando o status rapidamente (baladinha) pressione 1")
    print("para ficar mudando o seu recado pressione 2")
    print("para ficar floodando qualquer mensagem pressione 3")

    option = input("qual vai ser? ")
    option = int(option)

    if (option == 1):
        print("tu escolheu baladinha")
        time.sleep(1)
        driver = webdriver.Chrome()

        driver.get("https://discord.com/channels/@me")

        email = input("email da conta: ")
        senha = input("senha da conta: ")
        num = input("quantas vezes: ")
        num = int(num)
        cd = input(
            "cooldown entre as mudanças em segundos (números mto baixos podem não funcionar) // recomendado 1 segundo: ")
        cd = int(cd)

        # login
        driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(senha)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(6)


        def cuzin():
            driver.find_element_by_xpath("//div[@class='avatar-SmRMf2 wrapper-3t9DeA']").click()
            time.sleep(cd)
            driver.find_element_by_xpath("//div[@id='status-picker-online']").click()
            driver.find_element_by_xpath("//div[@class='avatar-SmRMf2 wrapper-3t9DeA']").click()
            time.sleep(cd)
            driver.find_element_by_xpath("//div[@id='status-picker-idle']").click()
            driver.find_element_by_xpath("//div[@class='avatar-SmRMf2 wrapper-3t9DeA']").click()
            time.sleep(cd)
            driver.find_element_by_xpath("//div[@id='status-picker-dnd']").click()
            driver.find_element_by_xpath("//div[@class='avatar-SmRMf2 wrapper-3t9DeA']").click()
            time.sleep(cd)
            driver.find_element_by_xpath("//div[@id='status-picker-invisible']").click()


        i = 0

        while (i <= num):
            cuzin()
            i = i + 1

    elif (option == 2):
        print("tu escolheu mudar os recados psicodelicamente")
        driver = webdriver.Chrome()
        driver.get("https://discord.com/channels/@me")

        email = input("email da conta: ")
        senha = input("senha da conta: ")
        num = input("quantas vezes: ")
        num = int(num)
        msg1 = input("recado 1: ")
        msg2 = input("recado 2: ")
        msg3 = input("recado 3: ")
        cd = input(
            "cooldown entre as mudanças em segundos (números mto baixos podem não funcionar) // recomendado 2 segundos: ")
        cd = int(cd)

        # login
        driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(senha)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(6)


        def cuzin():
            driver.find_element_by_xpath("//div[@class='avatar-SmRMf2 wrapper-3t9DeA']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//div[@aria-label='Editar status personalizado']").click()
            time.sleep(0.3)
            driver.find_element_by_xpath("//input[@placeholder='O suporte chegou!']").send_keys(
                Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + msg1 + Keys.ENTER)

            time.sleep(cd)

            driver.find_element_by_xpath("//div[@class='avatar-SmRMf2 wrapper-3t9DeA']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//div[@aria-label='Editar status personalizado']").click()
            time.sleep(0.3)
            driver.find_element_by_xpath("//input[@placeholder='O suporte chegou!']").send_keys(
                Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + msg2 + Keys.ENTER)

            time.sleep(cd)

            driver.find_element_by_xpath("//div[@class='avatar-SmRMf2 wrapper-3t9DeA']").click()
            time.sleep(0.5)
            driver.find_element_by_xpath("//div[@aria-label='Editar status personalizado']").click()
            time.sleep(0.3)
            driver.find_element_by_xpath("//input[@placeholder='O suporte chegou!']").send_keys(
                Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + msg3 + Keys.ENTER)

            time.sleep(cd)


        i = 0

        while (i <= num):
            cuzin()
            i = i + 1

    elif (option == 3):
        # falando pro selenium que eu quero uma variavel setada como webdriver usando o driver do chrome
        driver = webdriver.Chrome()
        driver2 = webdriver.Chrome()
        driver3 = webdriver.Chrome()
        # abrindo o zap // nessa hora tu pega a camera de QR code do wpp web e abre o seu zap
        driver.get("https://discord.com/channels/@me")
        driver2.get("https://discord.com/channels/@me")
        driver3.get("https://discord.com/channels/@me")

        email = input("email da conta: ")
        senha = input("senha da conta: ")
        name = input('nome de quem tu quer spammar (chat, server, dm, sla): ')
        msg = input('a msg que tu quer spammar (pode ser link de img/gif): ')
        num = input("quantas vezes: ")
        num = int(num)  # transformando a variavel num em inteiro pq o python eh pau no cu e n faz automaticamente
        cd = input(
            "cooldown entre as msg em segundos (números mto baixos podem não funcionar) // recomendado 1 segundo: ")
        cd = int(cd)
        # login
        driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(senha)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(6)
        driver2.find_element_by_xpath("//input[@name='email']").send_keys(email)
        driver2.find_element_by_xpath("//input[@name='password']").send_keys(senha)
        driver2.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(6)
        driver3.find_element_by_xpath("//input[@name='email']").send_keys(email)
        driver3.find_element_by_xpath("//input[@name='password']").send_keys(senha)
        driver3.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(6)  # cooldown do login

        # procurando o cara e dando enter
        driver.find_element_by_xpath("//button[@class='searchBarComponent-32dTOx']").click()
        driver.find_element_by_xpath("//input[@placeholder='Aonde você gostaria de ir?']").send_keys(name + Keys.ENTER)

        # procurando o cara e dando enter
        driver2.find_element_by_xpath("//button[@class='searchBarComponent-32dTOx']").click()
        driver2.find_element_by_xpath("//input[@placeholder='Aonde você gostaria de ir?']").send_keys(name + Keys.ENTER)

        driver3.find_element_by_xpath("//button[@class='searchBarComponent-32dTOx']").click()
        driver3.find_element_by_xpath("//input[@placeholder='Aonde você gostaria de ir?']").send_keys(name + Keys.ENTER)


        # criando uma funçao q localiza os path no html, enviando string e depois dando enter
        async def cuzin():
            try:
                time.sleep(cd)
                driver.find_element_by_xpath(
                    "//div[@class='markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP']").send_keys(
                    msg + Keys.ENTER + Keys.ENTER + Keys.ENTER)
                driver2.find_element_by_xpath(
                    "//div[@class='markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP']").send_keys(
                    msg + Keys.ENTER + Keys.ENTER + Keys.ENTER)
                driver3.find_element_by_xpath(
                    "//div[@class='markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP']").send_keys(
                    msg + Keys.ENTER + Keys.ENTER + Keys.ENTER)
                time.sleep(cd)
            except ElementNotInteractableException:
                driver.find_element_by_xpath(
                    "//button[@class='primaryButton-3oJYZH button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeXlarge-2yFAlZ grow-q77ONN']").send_keys(
                    Keys.ENTER + Keys.ENTER + Keys.ENTER + Keys.ENTER)
                driver2.find_element_by_xpath(
                    "//button[@class='primaryButton-3oJYZH button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeXlarge-2yFAlZ grow-q77ONN']").send_keys(
                    Keys.ENTER + Keys.ENTER + Keys.ENTER + Keys.ENTER)
                driver3.find_element_by_xpath(
                    "//button[@class='primaryButton-3oJYZH button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeXlarge-2yFAlZ grow-q77ONN']").send_keys(
                    Keys.ENTER + Keys.ENTER + Keys.ENTER + Keys.ENTER)
                time.sleep(2 * cd)


        # executando a funçao ate bater o num q foi setado
        async def sla():
            i = 0
            while (i <= num):
                await cuzin()
                i = i + 1


        asyncio.run(sla())
