Olá, bem vindo à versão 1.0 do buscador automático de vagas de emprego. Veja abaixo uma descrição mais detalhada.

Esse é um projeto em python que utiliza a ferramenta selenium para automatizar uma busca de empregos, de acordo com o cargo e local informado pelo usuário, em um site específico, o indeed.
![demonstração do funcionamento](https://github.com/daniel-antunes-da-silva/bot-vagas-de-emprego/assets/132831685/e456a92c-7d16-48d2-bd04-5be819ee0d01)

O script automatiza todo o site, aceitando os cookies, passando páginas, e fechando a janela de pop-up (que normalmente aparece na segunda página).

Solicitação de cookies que é exibida logo ao entrar no site:
![cookies](https://github.com/daniel-antunes-da-silva/bot-vagas-de-emprego/assets/132831685/d8c63aca-b173-4a50-941d-5c757504e045)

Pop-up que é exibido na segunda página:
![popup](https://github.com/daniel-antunes-da-silva/bot-vagas-de-emprego/assets/132831685/cd988a96-5863-4814-aeaa-973b8309f463)

Enquanto as páginas são acessadas, os titulos de cada vaga e o link de cada uma são armazenados em um arquivo de texto, que pode ser convertido em PDF para tornar os links clicáveis.
Obs: (os links são do próprio site do indeed referente à vaga, não são os links para página de candidatura em si).

Veja um exemplo da exibição em PDF:
![Exibição vagas em pdf](https://github.com/daniel-antunes-da-silva/bot-vagas-de-emprego/assets/132831685/10acbb44-3131-4973-a49f-82d7316162ed)

Quando não há mais páginas, o programa é encerrado e o navegador é fechado automaticamente.

O arquivo "monitoramento_vagas.py" é o que deve ser executado para o script funcionar. Já o arquivo "funcoes.py", apesar do nome, contém apenas uma função no momento dessa primeira versão.
