# Stoic - Documento de Requisitos

## Introdução

### Objetivo
O objetivo deste documento é delinear os requisitos funcionais e não funcionais para a aplicação "Stoic". "Stoic" é uma aplicação web projetada para fornecer aos usuários uma plataforma segura e intuitiva para o gerenciamento de diários.

### Escopo
"Stoic" será uma aplicação baseada na web utilizando Vue.js para o frontend, FastAPI para o backend e Docker para a conteinerização.

### Definições, Acrônimos e Abreviações
- **SPA**: Aplicação de Página Única (Single Page Application)
- **API**: Interface de Programação de Aplicações (Application Programming Interface)
- **CRUD**: Criar, Ler, Atualizar, Excluir (Create, Read, Update, Delete)
- **JWT**: Token de Acesso JSON (JSON Web Token)
- **Docker**: Plataforma de conteinerização

### Referências
- IEEE 830: Padrão para Especificações de Requisitos de Software
- [Documentação do Vue.js](https://vuejs.org/)
- [Documentação do FastAPI](https://fastapi.tiangolo.com/)
- [Documentação do Docker](https://docs.docker.com/)

## Descrição Geral

### Perspectiva do Produto
"Stoic" será uma aplicação autônoma para gerenciamento de diários com um frontend em Vue.js, backend em FastAPI e conteinerização com Docker.

### Funções do Produto
1. **Gerenciamento de Usuários**
   - Registrar e autenticar usuários
   - Recuperação e redefinição de senha
   - Gerenciamento de perfil de usuário

2. **Gerenciamento de Diários**
   - Criar, editar, excluir e visualizar diários

3. **Gerenciamento de Páginas**
   - Criar, editar, excluir e visualizar páginas dentro de um diário

4. **Gerenciamento de Entradas**
   - Escrever, editar, excluir e visualizar entradas no diário

5. **Funcionalidade de Pesquisa**
   - Pesquisar entradas por palavra-chave
   - Filtrar resultados por data, categoria e tags

6. **Categorização**
   - Criar, gerenciar e atribuir categorias

7. **Tagging**
   - Criar, gerenciar e atribuir tags

8. **Exportação/Importação**
   - Exportar diários e entradas para JSON ou PDF
   - Importar de JSON ou PDF

9. **Segurança**
   - Autenticação de usuários com JWT
   - Controle de acesso baseado em funções

10. **Sistema de Notificações**
    - Notificações por e-mail e na aplicação

### Classes e Características dos Usuários
- **Usuários Finais**: Indivíduos que gerenciam diários
- **Administradores**: Usuários que gerenciam configurações do sistema e contas de usuários

### Ambiente Operacional
- **Frontend**: Aplicação baseada em navegador utilizando Vue.js
- **Backend**: Serviço de API utilizando FastAPI
- **Conteinerização**: Docker
- **Banco de Dados**: PostgreSQL ou SQLite

### Restrições de Design e Implementação
- Conteinerização utilizando Docker
- Frontend com Vue.js
- Backend com FastAPI

### Documentação do Usuário
- **Manual do Usuário**: Instruções para usuários finais
- **Documentação da API**: Guias de desenvolvimento para uso da API

## Requisitos Funcionais

### Gerenciamento de Usuários
1. Registro, login e logout
2. Recuperação e redefinição de senha
3. Gerenciamento de perfil

### Gerenciamento de Diários
1. Criar, editar, excluir e visualizar diários

### Gerenciamento de Páginas
1. Criar, editar, excluir e visualizar páginas

### Gerenciamento de Entradas
1. Criar, editar, excluir e visualizar entradas

### Funcionalidade de Pesquisa
1. Pesquisa por palavra-chave
2. Filtros por data, categoria e tags

### Categorização
1. Criar, gerenciar e atribuir categorias

### Tagging
1. Criar, gerenciar e atribuir tags

### Exportação/Importação
1. Exportar para JSON ou PDF
2. Importar de JSON ou PDF

### Segurança
1. Autenticação com JWT
2. Controle de acesso baseado em funções

### Sistema de Notificações
1. Notificações por e-mail e na aplicação

## Requisitos Não Funcionais

### Requisitos de Desempenho
- Suportar até 1000 usuários simultâneos

### Requisitos de Segurança
- Criptografia de dados em trânsito e em armazenamento

### Requisitos de Usabilidade
- Interface amigável
- Frontend responsivo e acessível

### Requisitos de Confiabilidade
- Uptime de 99,9%
- Processos de backup e recuperação

### Requisitos de Manutenibilidade
- Código modular e bem documentado
- Testes automatizados

### Requisitos de Portabilidade
- Conteinerização com Docker para implantação

## Apêndices

### Glossário
- **Diário**: Coleção de páginas para entradas
- **Página**: Seção dentro de um diário
- **Entrada**: Nota individual dentro de uma página

### Referências
- [Documentação do Vue.js](https://vuejs.org/)
- [Documentação do FastAPI](https://fastapi.tiangolo.com/)
- [Documentação do Docker](https://docs.docker.com/)
