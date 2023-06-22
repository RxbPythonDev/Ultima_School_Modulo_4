import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

opcoes = Options()
opcoes.add_argument('--headless')
navegador = Chrome(service=Service(ChromeDriverManager().install()), options=opcoes)
navegador.set_window_size(1280, 1080)
navegador.maximize_window()

navegador.get('http://127.0.0.1:8000')

time.sleep(1)
link_contato = navegador.find_element(By.LINK_TEXT, 'Contato')
link_contato.click()
time.sleep(1)
navegador.save_screenshot('contato.png')

campo_nome = navegador.find_element(By.ID, 'id_name')
campo_email = navegador.find_element(By.ID, 'id_email')
campo_mensagem = navegador.find_element(By.ID, 'id_message')

campo_nome.send_keys('gileno')
campo_email.send_keys('gileno@email.com')
campo_mensagem.send_keys('mensagem de teste')

time.sleep(1)

navegador.save_screenshot('campos_preenchidos.png')

botao = navegador.find_element(By.TAG_NAME, 'button')
botao.click()

time.sleep(1)

navegador.save_screenshot('sucesso.png')

navegador.close()