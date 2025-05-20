from playwright.sync_api import sync_playwright, Playwright
import pandas as pd
import re
import tqdm as tqdm

def run(playwright: Playwright):
    estados_uf = [
    "ac", "al", "am", "ap", "ba", "ce", "df", "es", "go",
    "ma", "mg", "ms", "mt", "pa", "pb", "pe", "pi", "pr",
    "rj", "rn", "ro", "rr", "rs", "sc", "se", "sp", "to"
]
    url = "https://cidades.ibge.gov.br/brasil/"
    chrome = playwright.chromium.launch(headless=True)
    page = chrome.new_page()
    df = pd.DataFrame()
    hide_unities = False
    for estado in estados_uf:
        df_estado = pd.DataFrame()
        page.goto(f"{url}{estado}/panorama")
        page.wait_for_timeout(2000)
        estado = page.locator('div[class = "h1__mobile__completo"]').inner_text().strip()
        df_estado["Estado"] = [estado]
        #print("Estado: ", estado)
        for i in tqdm.tqdm(range(27), desc=f"Coletando dados de {estado}"):
            nome = page.locator('td[class = "lista__nome"]').nth(i).inner_text().strip()
            val = page.locator('td[class = "lista__valor"]').nth(i).inner_text().strip()
            if hide_unities:
                val = re.findall(r'[\d\.,]+', val)[0]
            df_estado[nome] = [val] 
            #print("nome: ", nome)
            #print("val: ", val)
            #print(df_estado)
            if i == 3:
                table = page.locator('tr[class = "lista__cabecalho recolhido"]').nth(0).click()
            elif i == 11:
                table = page.locator('tr[class = "lista__cabecalho recolhido"]').nth(1).click()
            elif i == 17:
                table = page.locator('tr[class = "lista__cabecalho recolhido"]').nth(2).click()
            elif i == 23:
                table = page.locator('tr[class = "lista__cabecalho recolhido"]').nth(3).click()
        df = pd.concat([df, df_estado], ignore_index=True)
    print(df)
    if hide_unities:
        df.to_excel("dados_coletados.xlsx", index=False)
    else:
        df.to_excel("dados_coletados_und.xlsx", index=False)

    
with sync_playwright() as playwright:
    run(playwright)
