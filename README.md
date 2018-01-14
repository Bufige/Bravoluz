# Bravoluz
Web Scraping para coletar dados do Bravoluz. Projeto pago, é simples e fácil de modificar para coletar mais dados.


# Explicação da lógica utilizada
### Projeto foi feito em modulos.
- get_links.py, É para coletar todos os links da categoria atual.
- get_products_info.py, É para coletar os dados de cada produto da categoria.
- post_excel.py, É para passar os dados coletados para um arquivo do excel.

# Objetivo

Este foi um projeto pago. O contratante apenas queria essa determinada categoria de produtos a serem coletados. Eu resolvi postar pois eu essa versão é mais limpa que o meu projeto anterior de prova de conceito do mercado-livre. Neste projeto, é trabalhado o conceito de modularização, o que facilita nossa vida a medida que a complexidade do projeto aumenta e também foi feito utilizado melhores práticas para coletar dados. No outro projeto, eu fiz utilizando o selenium, apesar de não ser necessário, neste também não era, então fiz da forma que deveria ser feito.



# Instalação

Basta ter o pip instalado, com isso, é necessário apenas fazer:
* > **pip install -r requirements.txt**


## Feito agora basta fazer: python main.py para rodar !
