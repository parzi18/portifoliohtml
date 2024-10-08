from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Op
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

class bot:
    
    def botWPP(self):
     options = Op()
     options.add_experimental_option("detach", True)
     options.add_argument("--allow-runing-insecure-content")
     options.add_argument("--allow-insecure-localhost")
     options.add_argument(f"--user-data-dir={'C:\\Users\\Pedro\OneDrive\\Área de Trabalho\\bot whatsapp\\cookies'}")
     options.add_argument("--no-fist-run")
     options.add_argument("--desable-renderer-backgrounding")
     options.add_argument("--desablebackgrounding-occluded-windows")
     options.add_argument("--desable-hang-monitor")
     options.add_experimental_option('prefs',{
    'excludeSwitches' : ['enable-lodding'], 
    'download.default_directory': 'C:\\Users\\Pedro\\OneDrive\\Área de Trabalho\\bot whatsapp\\download',
    })
      #def lista_de_conversa(self):
        
     self.driver = webdriver.Chrome(options=options)
     self.driver.get("https://web.whatsapp.com/")
     self.wait = WebDriverWait(self.driver, 120)
     self.Action_Chains = ActionChains(self.driver)
    
    
    #def conversas_nao_lidas(self):
    
     lista_de_conversa = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Lista de conversas']")))
     print(f"a lista foi carregada com sucesso: {lista_de_conversa}")
     
     
     
iniciar = bot()
iniciar.botWPP()
