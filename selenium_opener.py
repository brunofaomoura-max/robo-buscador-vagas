from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def abrir_vagas_no_navegador(vagas):
    if not vagas:
        print("Nenhuma vaga nova para abrir.")
        return

    print(f"\nAbrindo {len(vagas)} vaga(s) no navegador...")

    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opcoes
    )

    # abre a primeira vaga na aba principal
    driver.get(vagas[0]["url"])
    time.sleep(1)

    # abre o resto em novas abas
    for vaga in vagas[1:]:
        driver.execute_script(f"window.open('{vaga['url']}');")
        time.sleep(0.5)

    input("\nPressione ENTER quando terminar de ver as vagas...")
    driver.quit()