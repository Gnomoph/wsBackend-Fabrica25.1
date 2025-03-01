# wsBackend-Fabrica25.1

# Advice CRUD Application

Esta é uma aplicação Django que implementa um CRUD para gerenciar conselhos ("Advice"). Além das operações tradicionais (criar, ler, atualizar e excluir), o projeto permite buscar automaticamente um conselho a partir da [Advice Slip API](https://api.adviceslip.com/advice).

## Funcionalidades

- **Listagem:** Exibe todos os conselhos cadastrados.
- **Detalhes:** Visualiza o detalhe de um conselho específico.
- **Criação:** Permite criar um novo conselho manualmente ou buscar um conselho automaticamente da Advice Slip API.
- **Atualização:** Edita um conselho existente.
- **Exclusão:** Remove um conselho do sistema.

## Requisitos

- Python 3.8 ou superior
- Django (última versão recomendada)
- Biblioteca `requests`

## Instalação e Configuração

### 1. Clone o Repositório ou Faça o Download dos Arquivos

Caso esteja usando um sistema de versionamento (por exemplo, Git), clone o repositório:
```bash
git clone https://seu-repositorio-url.git
