
# import all required frameworks
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


maxCnt = 10

#inicialization of webdriver for Firefox Browser
driver = webdriver.Firefox()

def realizaLogin():

    driver.get("https://dsvdigital.prefeitura.sp.gov.br/#/login")
    element = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/input")
    element.clear()
    element.send_keys("35237331000124")
    element = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/input")
    element.send_keys("aqui@MOTTU")
    element.send_keys(Keys.RETURN)

#finding elements for cnt control
    time.sleep(1)
    cabecario = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h3")
    cnt = 0
    while cabecario != "Seleção de veículo":
        time.sleep(1)
        cabecario = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h3")
        cnt += 1
        if cnt > maxCnt:
            #print ("funcionou a func 0")
            
            localizaRenavam("1318144822")
            break

            #return 0
    print ("funcionou a func")
    #return 1

def localizaRenavam(renavam):
    if renavam.startswith('0'):
        renavam = str(int(renavam))

    time.sleep(2)

    element = driver.find_element(By.ID, "txtSearchRenavam")
    element.clear()
    element.send_keys(renavam)
    element = driver.find_element(By.ID, "btnLupa")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div/table/tbody/tr/td[5]/button")
    element.click()
    time.sleep(3)
    cabecario = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/h3")
    cnt = 0
    
    while cabecario != "Lista de Infrações":
        time.sleep(1)
        cabecario = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/h3")
        cnt += 1
        if cnt > maxCnt:
            return 0
        print("cnt> maxCnt")
    print("este printo nao passou pelo seu IF")

#Escolhe AIT referente a infração para clicar em: "Detalhes indicação de condutor"
def clickBtnPesquisarDetalhesIndicacao(ait):
    jsCode = ("bs = document.querySelectorAll('b'); " + "for(var i = 0; i< bs.length; i++){ " + "    x = bs[i]; " + "    if(x.innerText == 'A.I.T.:') { " + "        parNode = x.parentNode; " + "        if(parNode.innerText.includes('" + ait + "')) { " + "           while(parNode.className != 'row') { " + "                parNode = parNode.parentNode;  " + "           }" + "           break;" + "        }" + "    }" + "}" + "btns = parNode.querySelectorAll('a.btn-lista-autuacao'); " + "for(var i = 0; i < btns.length; i++) { " + "   b = btns[i]; " + "   if(b.innerText.includes('Detalhes Indicação de Condutor')) {" + "       b.click(); " + "   }" + "}" + "return 1;")
    print("E/STE MUST SAIR!  => ret = r.dom(jsCode)")

        
    #ret = r.dom(jsCode)

    #Modal
    time.sleep(1)
    cabecario = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/h3")
    cnt = 0

    while cabecario != "Consulta da Indicação de Condutor Infrator":
        time.sleep(1)
        cabecario = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/h3")
        cnt += 1
        if cnt % 3 == 0:

            print("E/STE MUST SAIR!  => ret = r.dom(jsCode)")
            #ret = r.dom(jsCode)    
        if cnt > maxCnt:
            return 0
    
    return 3

#def clickBtnPesquisarAit(ait):

def dowloadFormulario(renavam, ait, folder):
    driver.get("https://dsvdigital.prefeitura.sp.gov.br/#/app/selecaorenavampj")
    if (localizaRenavam(renavam) == 0):    
        return 0

    clickBtnPesquisarDetalhesIndicacao(ait)

    element = driver.find_element(By.XPATH, "button.col-lg-3.col-sm-3.btn.btn-warn.m-b")
    element.click()
    time.sleep(4)



realizaLogin()