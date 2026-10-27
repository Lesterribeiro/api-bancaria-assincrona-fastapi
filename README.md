# API Bancária Assíncrona de Alta Performance com FastAPI

Microserviço financeiro assíncrono projetado e implementado em Python utilizando o framework **FastAPI** para o gerenciamento de contas correntes e registro automatizado de operações de depósitos e saques bancários.

O projeto foi estruturado seguindo rigorosamente os padrões de engenharia de software e arquitetura assíncrona orientada a objetos (ORM).

---

## Objetivos e Funcionalidades do Negócio

A API foi projetada para atuar em barramentos de alta concorrência e responde nativamente a 2 dores centrais do ecossistema bancário:
**Cadastro e Processamento de Transações:** Processa de forma assíncrona operações de entrada (`DEPOSIT`) e saída (`WITHDRAWAL`) de fundos em contas correntes.
**Exibição Corrente de Extratos:** Endpoint dedicado para varredura histórica e exibição cronológica de todas as movimentações de uma conta.

---

## Engenharia de Dados e Regras de Validação de TI

Para assegurar a integridade e conformidade contábil das transações, a camada de negócios valida rigidamente as seguintes premissas em segundo plano:

### Proteção de Saldo contra Descoberto (Saques)
O sistema avalia a mutação do saldo antes de autorizar a persistência de um evento de retirada. Se o montante solicitado for superior ao saldo atual da conta correspondente, a operação é abortada através do disparo de uma exceção regulamentada.

### Bloqueio de Operações com Valores Negativos
Para mitigar fraudes de inversão de sinal ou entradas inconsistentes, os endpoints recusam chamadas onde o argumento `amount` seja menor ou igual a zero, mitigando riscos de lavagem de dados na base.

### Abstração Assíncrona e Modelo Relacional (ORM)
A persistência utiliza **SQLAlchemy 2.0 Async** associado ao driver `aiosqlite`. A modelagem de dados foi desenhada sob a relação de cardinalidade `1:N` (Uma conta pode possuir múltiplas transações indexadas por chaves estrangeiras), garantindo isolamento ACID durante o processamento de concorrência massiva.

---

## Organização do Repositório

```text
/
├── src/
│   ├── controllers/           # Roteamento e endpoints da API (Transações e Extratos)
│   ├── models/                # Definição técnica das tabelas do banco de dados (SQLAlchemy)
│   ├── config.py              # Mapeamento e parseamento das variáveis de ambiente (.env)
│   └── main.py                # Inicialização da aplicação e roteador global
├── .env.example               # Exemplo de credenciais e caminhos locais
├── .gitignore                 # Filtro de segurança contra vazamento de chaves privadas
├── vercel.json                # Manifesto de parametrização e deploy na nuvem Serverless
└── README.md                  # Documentação principal do projeto
```

---

## Implantação e Documentação Online (OpenAPI / Swagger)

A aplicação encontra-se homologada e configurada com suporte a deploys rápidos na nuvem da Vercel através do manifesto do servidor de aplicação.

* **Link da Documentação Interativa (Swagger UI):** https://vercel.app
