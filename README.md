> Bot para Discord focado no gerenciamento remoto de servidores Minecraft via **RCON**.

O **bot-mc-rcon-discord** permite que administradores e moderadores executem comandos no servidor Minecraft diretamente pelo Discord, dispensando o acesso contínuo ao console do servidor ou ao painel de hospedagem.

---

## 🚀 Funcionalidades

* ⚙️ **Execução de comandos RCON:** Rode qualquer comando do console diretamente pelo Discord.
* 💬 **Mensagens globais:** Envie avisos formatados com tag para todos os jogadores online.
* ⚡ **Comandos Slash (`/`):** Interface moderna, intuitiva e com suporte a autocompletar.
* 🛡️ **Controle centralizado:** Gerencie permissões e acessos ao servidor em um só lugar.

---

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter instalado no seu ambiente:

* [Python 3.12](https://www.python.org/downloads/) ou superior.
* [UV](https://docs.astral.sh/uv/guides/install-python/) (gerenciador rápido de pacotes e ambientes Python).
* Servidor Minecraft com a opção **RCON habilitada** no `server.properties`.

---

## ⚙️ Configuração

### 1. Servidor Minecraft
No arquivo `server.properties` do seu servidor Minecraft, certifique-se de habilitar e configurar o RCON:

```properties
enable-rcon=true
rcon.port=25575
rcon.password=SUA_SENHA_RCON_AQUI
```

### 2. Arquivo `.env`
Crie um arquivo `.env` na **raiz do projeto** contendo as seguintes variáveis:

```env
RCON_HOST=127.0.0.1
RCON_PORT=25575
RCON_PASSWORD=SUA_SENHA_RCON_AQUI
BOT_TOKEN=SEU_TOKEN_DO_BOT_DISCORD
```

---

## 🏁 Como Executar

Com o `uv` instalado, rode os comandos abaixo no terminal na pasta do projeto:

```bash
# Sincroniza e instala as dependências
uv sync

# Executa o bot
uv run src/main.py
```

---

## 📜 Comandos Slash (`/`)

| Comando | Parâmetros | Descrição |
| :--- | :--- | :--- |
| `/rcon execute` | `command` *(texto)* | Executa um comando direto no console do servidor (ex: `time set day`, `op player`). |
| `/rcon say` | `message` *(texto)* | Envia uma mensagem global para o chat do jogo formatada com a tag do usuario disc. |