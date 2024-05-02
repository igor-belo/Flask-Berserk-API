
## API de Personagens de Berserk

Esta é uma API simples desenvolvida em Python usando o framework Flask. Ela permite visualizar, adicionar, atualizar e excluir informações sobre os personagens do mangá Berserk.

## Como Usar

### Pré-requisitos

1. Python 3.x instalado.
2. Flask instalado 
``` 
pip install Flask 
```

### Executando a API

* Execute a aplicação *app.py*

A API será executada em "http://localhost:5000".

### Rotas Disponíveis

* **GET/personagens:** Retorna uma lista com todos os personagens de Berserk.
* **POST/personagens:** Adiciona um novo personagem à lista.
* **GET/personagens/<id>:** Retorna os detalhes de um personagem específico pelo seu ID.
* **PUT/personagens/<id>:** Atualiza os detalhes de um personagem existente pelo seu ID.
* **DELETE/personagens/<id>:** Exclui um personagem pelo seu ID.

### Os dados dos personagens são representados em formato JSON com os seguintes campos:

* **id:** ID único do personagem (inteiro)
* **nome:** Nome do personagem (string)
* **descricao:** Descrição do personagem (string)

### Exemplo de objeto JSON de um personagem:
```json
{
    "id": 1,
    "name": "Guts",
    "description": "Guts é o protagonista do mangá, um guerreiro solitário em busca de vingança e propósito em um mundo sombrio e violento, ele carrega uma espada enorme chamada de Dragon Slayer e possui uma armadura chamada de berserker armor que foi lhe dada pelo skull knight. Guts é realmente um personagem marcante, ele representa a luta constante contra adversidades em um mundo hostil."
}
```

### Tecnologias usadas

![Python](https://img.shields.io/badge/Python-306998?style=for-the-badge&logo=python&logoColor=FFE873)&nbsp;
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)&nbsp;

### Contribuindo

Sinta-se à vontade para contribuir fazendo um fork e enviando pull requests com melhorias, correções de bugs, ou adição de novos recursos.

### Creditos

Este projeto foi criado por **Igor Belo**

Sinta-se a vontade para entrar em contato:

<div align="left"> 
  <a href="https://www.linkedin.com/in/igor-belo/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"  target="_blank"></a> 
  <a href="https://www.instagram.com/igor_belo.py/" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
  <a href = "mailto:igorbello170@gmail.com"> <img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>
