Olá, bem vindo à versão 1.0 do buscador automático de vagas de emprego. Veja abaixo uma descrição mais detalhada.

Esse é um projeto em python que utiliza a ferramenta selenium para automatizar uma busca de empregos, de acordo com o cargo e local informado pelo usuário, em um site específico, o indeed.
![demonstração do funcionamento.png](..%2F..%2F..%2FPictures%2Fdemonstra%E7%E3o%20do%20funcionamento.png)
O script automatiza todo o site, aceitando os cookies, passando páginas, e fechando a janela de pop-up (que normalmente aparece na segunda página).

Solicitação de cookies que é exibida logo ao entrar no site:
![cookies.PNG](cookies.PNG)

Pop-up que é exibido na segunda página:
![popup.PNG](popup.PNG)

Enquanto as páginas são acessadas, os titulos de cada vaga e o link de cada uma são armazenados em um arquivo de texto, que pode ser convertido em PDF para tornar os links clicáveis.
Obs: (os links são do próprio site do indeed referente à vaga, não são os links para página de candidatura em si).

Veja um exemplo da exibição em PDF:
![Exibição vagas em pdf.png](Exibi%E7%E3o%20vagas%20em%20pdf.png)

Quando não há mais páginas, o programa é encerrado e o navegador é fechado automaticamente.

O arquivo "monitoramento_vagas.py" é o que deve ser executado para o script funcionar. Já o arquivo "funcoes.py", apesar do nome, contém apenas uma função no momento dessa primeira versão.
