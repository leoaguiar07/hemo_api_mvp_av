
<h1 align="center">
    <img alt="Hemo" title="#Hemo" src="./img/topo.png" />
</h1>



<p align="center">
 <a href="#sobre-o-projeto">Sobre</a> •
 <a href="#arquitetura">Arquitetura</a> • 
 <a href="#modo-de-desenvolvimento">Como executar</a> • 
 <a href="#tecnologias">Tecnologias</a> • 
 <a href="#autor">Autor</a> • 
 <a href="#licença">Licença</a>
</p>


<h4 align="center"> 
	Em desenvolvimento
</h4>

## Sobre o projeto

O projeto tem como finalidade centralizar informações sobre hemocentros, coletas e doadores. Permitindo o cadastro de hemocentros, doações, doadores e possíveis doadores. Visualize os dados em um dashboard que mostra unidades doadas no dia, comparação de crescimento de possíveis doadores cadastrados e doadores que já realizaram doações, comparação entre estoque ideal de unidades de sangue e estoque real de unidades, número de doçãoes por dia de cada tipo sanguíneo. Os dados podem ser visualizados por hemocentro, por estado ou todo o país (todos os hemocentros cadastrados). 

Busque doadores cadastrados no sistema próximos aos hemocentros ou próximo a um endereço informado (PCM - ponto de coleta móvel). Selecione o hemocentro (ou PCM), informe a distância (Km) e escolha ação a ser realizada: enviar e-mail, enviar SMS ou enviar mensagem via Whatsapp/Telegram


Projeto desenvolvido para atender ao MVP da disciplina de Desenvolvimento Full Stack Avançado (PUC-RIO).


⚠️ Este projeto é divido em três partes, conforme <a href="#arquitetura">Arquitetura</a> mostrada abaixo.<br/>
Acesse o [Readme](https://github.com/leoaguiar07/hemo_front_mvp_av) para visualizar todos os detalhes.


---

##  Arquitetura


<h1 align="center">
    <img alt="Hemo" title="#Hemo" src="./img/mapa.png" />
</h1>

Este projeto é divido em três partes:
1. Frontend (A) ([Readme](https://github.com/leoaguiar07/hemo_api_mvp_av))
2. API (B) 
3. API (C) ([Readme](https://github.com/leoaguiar07/hemo_cep_api_mvp_av))


💡 O Frontend precisa que as APIs (B e C) estejam sendo executadas para funcionar perfeitamente.

---

### Pré-requisitos

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.


---

## Como executar o projeto (API (B))

### Modo de desenvolvimento

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.


#### Executando o servidor


Para executar a API  basta executar:

```
(env)$ python manage.py runserver 0.0.0.0:8000
```


#### Acesso no browser

Abra o [http://localhost:8000/api/v1/swagger/](http://localhost:8000/api/v1/swagger/) no navegador para verificar o status da API em execução.

---
### Através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile no terminal e seus arquivos de aplicação e
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t nome_da_sua_imagem .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -d -p 8000:8000 nome_da_sua_imagem
```

Uma vez executando, para acessar o front-end, basta abrir o [http://localhost:8000/api/v1/swagger/](http://localhost:8000/api/v1/swagger/) no navegador.

💡 O Frontend precisa que as APIs (B e C) estejam sendo executadas para funcionar perfeitamente.

---

##  Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

#### **Frontend (A)**  

[![My Skills](https://skillicons.dev/icons?i=html,css,javascript,bootstrap&perline=4)](https://skillicons.dev)

#### **API (B)**  

[![My Skills](https://skillicons.dev/icons?i=python,django,sqlite&perline=3)](https://skillicons.dev)


#### **API (C)**  

[![My Skills](https://skillicons.dev/icons?i=python,flask&perline=4)](https://skillicons.dev)

#### **Utilitários**

-   API:  **[ViaCep API](https://https://viacep.com.br/)**
-   Editor:  **[Visual Studio Code](https://code.visualstudio.com/)**
-   Teste de API:  **[Postman](https://www.postman.com/)**

---

## Autor

 <img style="border-radius: 50%;"  src="https://avatars.githubusercontent.com/u/131842850?s=400&amp;u=85e806ce0a66f202396de3ac457dc3d768f41e3f&amp;v=4" width="100" height="100" alt="@leoaguiar07">
 <br />
 <sub><b>Léo Aguiar</b></sub></a> 
 <br /><br />


[![Gmail Badge](https://img.shields.io/badge/-leorodriguesaguiar@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:tgmarinho@gmail.com)](mailto:leorodriguesaguiar@gmail.com)

---

## Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

Feito por Léo Aguiar [Entre em contato!](mailto:leorodriguesaguiar@gmail.com)
