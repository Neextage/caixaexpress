# Changelog

## v0.1.0

### Sprint 01

- Estrutura inicial criada.

## Sprint 01 - Etapa 02.1

- Criação do Theme Manager
- Criação do Version Manager
- Criação das constantes globais
- Atualização do main.py

## Sprint 02 - Etapa 01

- Implementado DatabaseManager.
- Criação automática do banco SQLite.
- Criação automática das tabelas.
- Integração com LoggerManager.

## Sprint 02 - Etapa 02

- Inserção automática dos destinatários padrão.
- Implementados métodos de consulta de destinatários.
- Implementados métodos de inclusão, alteração e remoção.
- Implementado controle de ativação/desativação de destinatários.

## Sprint 03 - Etapa 01

- Criada a janela principal da aplicação.
- Implementada a estrutura inicial da interface com CustomTkinter.
- Adicionadas área lateral e área de conteúdo.
- Centralização automática da janela.

## Sprint 03 - Etapa 02

- Implementada navegação principal da aplicação.
- Criada sidebar do Caixa Express.
- Criada tela pública de fechamento de caixa.
- Criadas estruturas iniciais das páginas administrativas.
- Implementado destaque visual da página selecionada.
- Separados componentes e páginas da interface.

## Sprint 03 - Etapa 03

- Integrado ConfigManager à interface gráfica.
- Implementado carregamento automático do nome da loja.
- Bloqueada alteração do nome da loja pela tela pública.
- Implementado campo monetário com formatação brasileira.
- Implementada validação do valor do fechamento.
- Implementado bloqueio do envio quando a loja não estiver configurada.

## Sprint 03 - Etapa 04

- Implementado AuthManager.
- Implementado hash PBKDF2-HMAC-SHA256 para senha administrativa.
- Criada janela de autenticação administrativa.
- Protegidas as páginas Destinatários, Configuração, Histórico, Logs e Testes.
- Mantida a tela Caixa com acesso público.
- Implementada sessão administrativa válida até o encerramento da aplicação.

## Sprint 04 - Etapa 01

- Integrado DatabaseManager à interface gráfica.
- Implementada listagem real dos destinatários cadastrados.
- Implementada organização visual por grupos.
- Implementados indicadores de destinatários ativos e inativos.
- Implementado controle de ativação e desativação.
- Implementada persistência do status no SQLite.
- Implementada atualização automática da página.