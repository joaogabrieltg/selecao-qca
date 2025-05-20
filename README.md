# 📊 Seleção QCA - Coleta de Dados dos Estados Brasileiros

Este projeto foi desenvolvido como parte de um processo seletivo de estágio e tem como objetivo automatizar a coleta de dados do site do IBGE utilizando a biblioteca [Playwright](https://playwright.dev/python/).

## 🎯 Objetivo

Extrair informações de **todos os estados brasileiros**, diretamente do portal do IBGE, sem utilizar nenhuma API dos tópicos:
- **População**
- **Trabalho e Rendimento**
- **Educação**
- **Economia**
- **Saúde**
- **Meio Ambiente**
- **Território**

As informações foram obtidas a partir da página de panorama de cada estado:  
🔗 [https://cidades.ibge.gov.br/](https://cidades.ibge.gov.br/)

## 📁 Estrutura dos Arquivos

- `ibge_scraper.py`: Script principal com toda a lógica de navegação, extração e exportação.
- `dados_coletados_und.xlsx`: Planilha com os dados coletados, incluindo unidades de medida.
- `dados_coletados.xlsx`: Planilha com apenas os valores numéricos (sem unidades).
- `requirements.txt`: Dependências do projeto.