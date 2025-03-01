# wsBackend-Fabrica25.1
# Advice CRUD Application

Esta é uma aplicação Django que implementa um **CRUD** para gerenciar conselhos ("Advice"). Além das operações tradicionais (criar, ler, atualizar e excluir), o projeto permite buscar automaticamente um conselho a partir da [Advice Slip API](https://api.adviceslip.com/advice).

## Funcionalidades

A aplicação oferece as seguintes funcionalidades:

- **Listagem de Conselhos:** Exibe todos os conselhos cadastrados.
- **Detalhes de Conselhos:** Visualiza o detalhe de um conselho específico.
- **Criação de Conselhos:** Permite criar um novo conselho manualmente ou buscar um conselho automaticamente da **Advice Slip API**.
- **Atualização de Conselhos:** Edita um conselho existente.
- **Exclusão de Conselhos:** Remove um conselho do sistema.

## Tecnologias e Requisitos

Para rodar esse projeto, você precisará dos seguintes requisitos:

- **Python 3.8** ou superior.
- **Django** (última versão recomendada).
- Biblioteca **requests** para fazer chamadas HTTP para a API externa.

## Instalação e Configuração

### 1. Clone o Repositório ou Faça o Download dos Arquivos

Caso esteja usando um sistema de versionamento (como Git), clone o repositório:

```bash
git clone https://github.com/Gnomoph/Projeto-Advice-CRUD.git
cd Projeto-Advice-CRUD
Ou baixe o arquivo zip do repositório e extraia os arquivos em uma pasta no seu sistema.

2. Instalação das Dependências
Com o ambiente virtual ativado (caso esteja utilizando), instale as dependências do projeto:

bash
Copiar
Editar
pip install -r requirements.txt
3. Configuração do Banco de Dados
Depois de instalar as dependências, aplique as migrações do banco de dados para criar as tabelas necessárias:

bash
Copiar
Editar
python manage.py migrate
4. Criação de Superusuário (Opcional)
Se você quiser acessar o painel de administração do Django, crie um superusuário com o comando abaixo:

bash
Copiar
Editar
python manage.py createsuperuser
Siga as instruções para criar um usuário.

5. Iniciando o Servidor de Desenvolvimento
Agora você pode rodar o servidor de desenvolvimento:

bash
Copiar
Editar
python manage.py runserver
O servidor estará disponível em http://localhost:8000/. Você pode acessar a aplicação e começar a utilizar as funcionalidades.

Estrutura do Projeto
bash
Copiar
Editar
meuprojeto/
    manage.py                # Arquivo de gerenciamento do Django.
    meuprojeto/              # Configurações do projeto (settings, urls, wsgi, etc.).
advice/
    models.py                # Define o modelo Advice.
    forms.py                 # Contém o AdviceForm para criação e edição.
    views.py                 # Implementa as views para listar, detalhar, criar, atualizar e excluir conselhos.
    urls.py                  # Define as rotas do app.
templates/
    advice_list.html         # Template para listagem de conselhos.
    advice_detail.html       # Template para exibição de detalhes.
    advice_form.html         # Template para criação e atualização.
    advice_confirm_delete.html # Template para confirmação de exclusão.
Como Usar
Listar Conselhos
Acesse a raiz da aplicação para visualizar todos os conselhos cadastrados.

Criar Conselho
Você pode criar conselhos de duas maneiras:

Busca Automática: Clique em "Criar Novo Conselho (buscar da API)" para obter um conselho aleatório diretamente da Advice Slip API.
Criação Manual: Clique em "Criar Manualmente" para inserir um conselho manualmente.
Editar e Excluir
Após visualizar um conselho, você pode editar ou excluir o conselho utilizando os links "Editar" e "Excluir" que aparecem ao lado de cada conselho na listagem.

