# 💰 Caixa Express

<div align="center">

Sistema Desktop para automatização do envio de fechamento de caixa por e-mail.

**Versão 1.0.0**

Desenvolvido por **Dylan Ryan Pereira Santos**

</div>

---

## 📌 Sobre o Projeto

O **Caixa Express** foi desenvolvido para automatizar o processo de envio do fechamento diário de caixa das lojas.

O sistema elimina o envio manual de e-mails, padroniza os relatórios enviados e centraliza o gerenciamento de destinatários, configurações SMTP e histórico de envios em uma única aplicação.

---

## ✨ Funcionalidades

### 📤 Envio de Fechamento

- Envio automático por e-mail
- Relatório HTML profissional
- Versão texto para compatibilidade
- Pré-visualização do valor do caixa em dispositivos móveis
- Geração automática de protocolo

---

### 👥 Gerenciamento de Destinatários

- Cadastro
- Edição
- Exclusão
- Ativar / Desativar
- Agrupamento por setor
- Validação de e-mail
- Proteção contra e-mails duplicados

---

### ⚙ Configurações

- Nome da Loja
- Servidor SMTP
- Porta SMTP
- TLS
- SSL
- Timeout
- E-mail Remetente

---

### 📜 Histórico

- Registro completo dos envios
- Status
- Protocolo
- Data
- Hora
- Valor enviado
- Mensagem de retorno

---

### 📝 Logs

Registro completo de:

- Inicialização
- Encerramento
- Envio SMTP
- Erros
- Avisos
- Eventos importantes

---

### 🔐 Administração

- Login administrativo
- Proteção das telas administrativas

---

## 🖼 Capturas de Tela

> *(Adicionar capturas do sistema aqui)*

### Tela Inicial

*(Imagem)*

---

### Destinatários

*(Imagem)*

---

### Configurações

*(Imagem)*

---

### Histórico

*(Imagem)*

---

### Logs

*(Imagem)*

---

## 🏗 Arquitetura

```
CaixaExpress/

config/
core/
database/
logs/
ui/
    components/
    dialogs/
    pages/

main.py
```

---

## 🛠 Tecnologias Utilizadas

- Python 3.14
- CustomTkinter
- SQLite
- SMTP
- HTML
- Git
- GitHub

---

## 🚀 Como Executar

### Clone o projeto

```bash
git clone https://github.com/Neextage/caixaexpress.git
```

---

### Acesse a pasta

```bash
cd caixaexpress
```

---

### Crie o ambiente virtual

```bash
python -m venv .venv
```

---

### Ative o ambiente

Windows

```powershell
.venv\Scripts\activate
```

---

### Instale as dependências

```bash
pip install -r requirements.txt
```

---

### Execute

```bash
python main.py
```

---

## 📂 Banco de Dados

O sistema utiliza SQLite.

As tabelas principais são:

- recipients
- settings
- history
- users
- logs

---

## 🔒 Segurança

- Login administrativo
- TLS
- SSL
- Validação de e-mails
- Tratamento de exceções
- Registro de logs

---

## 📈 Roadmap

### Versão 1.0.0

- [x] Envio SMTP
- [x] HTML profissional
- [x] Histórico
- [x] Logs
- [x] Configurações
- [x] Login Administrativo
- [x] CRUD de Destinatários
- [x] Tela Sobre
- [x] Splash Screen
- [x] Executável
- [x] Instalador

---

## 📋 Changelog

Consulte o arquivo **CHANGELOG.md** para acompanhar todas as alterações realizadas durante o desenvolvimento.

---

## 👨‍💻 Desenvolvedor

**Dylan Ryan Pereira Santos**

Analista de Sistemas

Projeto desenvolvido utilizando Python, CustomTkinter e SQLite.

---

## 📄 Licença

Este projeto foi desenvolvido para uso interno da empresa.

Todos os direitos reservados.

© 2026 Dylan Ryan Pereira Santos
