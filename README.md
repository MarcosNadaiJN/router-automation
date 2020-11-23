# Automação de Acesso e Configuração de Roteadores

Atualmente no mercado, estão disponiveis diversas marcas e modelos de roteador WIFI, em todos eles, é necessario relizar uma serie de configurações, e na maioria dos casos, a configuração é a mesma, com excessão de SSID e Senha WIFI, porem, nos modelos mais novos, muitos deles, não possuem a opção de acesso via SSH, para que essas configurações possam ser feitas de forma mais rapida.

Pensando nisso, crie alguns scripts, que utilizando o Python junto com o Selenium, ira acessar o roteador e configura-lo via interface WEB, atualmente, o roteador suportado é o TP-LINK C60, pois é o unico modelo que tenho acesso, mas caso seja necessario adicionar um novo modelo ao script, basta criar as funções do modelo desejado em um novo arquivo, e adicionar a ordem de execução destas funções, no arquivo "script_por_roteador".
