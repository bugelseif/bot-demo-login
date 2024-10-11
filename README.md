# Bot Demo Login

Este projeto é um exemplo de automação de login em sites usando BotCity e Python. O objetivo é demonstrar como automatizar o processo de login em uma página web e realizar testes de automação para simular interações com elementos de formulário, como campos de login e senha.

## Funcionalidades

- Realiza login automatizado em uma página de exemplo
- Preenche formulários de login com credenciais fornecidas na própria página
- Demonstra o uso básico do [framework web da BotCity](https://documentation.botcity.dev/pt/frameworks/web/)
- Faz integrações básicas com o [Orquestrador BotCity](https://documentation.botcity.dev/pt/maestro/maestro-sdk/)
- Exemplo prático de automação de testes de login em sites


## Para executar localmente
### Requisitos

Para rodar este projeto, você precisará dos seguintes softwares instalados:

- Python 3.7 ou Superior
- [BotCity | Framework web](https://pypi.org/project/botcity-framework-web/)
- [BotCity | SDK](https://pypi.org/project/botcity-maestro-sdk/)
- [Webdriver Manager for Python](https://pypi.org/project/webdriver-manager/)
- Navegador Firefox


### Crie e ative um ambiente virtual

   Para garantir que as dependências do projeto sejam isoladas de outros projetos Python, é recomendado usar um ambiente virtual.

   - No macOS/Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - No Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

### Instalação de Dependências

Instale as dependências do projeto com o seguinte comando:

```bash
python -m pip install -r requirements.txt
```

### Executa o arquivo principal

```bash
python bot.py
```

## Para executar via Runner

- [Conta community](https://developers.botcity.dev/) na BotCity
- Download e instalação do [BotCity Studio SDK](https://documentation.botcity.dev/pt/getting-started/botcity-studio-sdk/)
- Configuração de um [Runner](https://documentation.botcity.dev/pt/getting-started/botcity-studio-sdk/#configurando-um-botcity-runner)
- [Build e deploy](https://documentation.botcity.dev/pt/maestro/features/easy-deploy/) da automação na plataforma
- [Nova tarefa](https://documentation.botcity.dev/pt/maestro/features/new-task/)