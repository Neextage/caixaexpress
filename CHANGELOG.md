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

## Sprint 04 - Etapa 02

- Implementada tela administrativa de configurações.
- Implementada edição do nome da loja pela interface.
- Implementada configuração do servidor SMTP.
- Implementada configuração de porta, remetente e senha SMTP.
- Implementadas opções TLS e SSL.
- Implementada configuração de timeout.
- Implementadas validações dos campos de configuração.
- Implementada gravação das configurações no config.ini.
- Implementada atualização automática do nome da loja na tela Caixa.

## Sprint 04 - Etapa 03

- Implementada camada de histórico no DatabaseManager.
- Implementado registro de tentativas de envio no SQLite.
- Implementada tela administrativa de Histórico.
- Implementados indicadores de total, sucessos e erros.
- Implementada listagem dos registros de envio.
- Implementada formatação monetária brasileira no histórico.
- Implementada atualização manual e automática da listagem.
- Validada persistência dos registros de histórico.

## Sprint 04 - Etapa 04

- Implementada tela administrativa de Logs.
- Integrado LoggerManager à interface gráfica.
- Implementada leitura do arquivo caixaexpress.log.
- Implementados indicadores de informações, avisos e erros.
- Implementados filtros por nível de log.
- Implementada atualização da visualização.
- Implementada limitação de 500 registros exibidos.
- Implementada ordenação dos registros mais recentes primeiro.
- Validada leitura dos logs reais da aplicação.

## Sprint 04 - Etapa 05

- Implementado SMTPManager.
- Implementado teste de conexão e autenticação SMTP.
- Implementado envio controlado de e-mail de teste.
- Implementada interface administrativa para testes SMTP.
- Implementada visualização das configurações SMTP utilizadas.
- Implementada execução dos testes em thread para evitar travamento da interface.
- Implementado tratamento amigável de erros SMTP, SSL/TLS, timeout e conexão.
- Integrado o resultado dos testes ao LoggerManager.
- Validada conexão SMTP utilizando STARTTLS.
- Validado envio real de e-mail de teste.
- Validado recebimento do e-mail de teste.
- Removido config/config.ini do versionamento Git.
- Adicionado config/config.ini ao .gitignore.
- Removido config/config.ini de todo o histórico Git.
- Reescrito e atualizado o histórico remoto do repositório sem o arquivo de configuração sensível.

## Sprint 04 - Conclusão

- Implementado gerenciamento administrativo de destinatários.
- Implementada tela completa de configurações.
- Implementado histórico persistente de envios.
- Implementada visualização e filtragem dos logs da aplicação.
- Implementada ferramenta administrativa de diagnóstico SMTP.
- Validada comunicação real com o servidor SMTP.
- Validado envio e recebimento de e-mails de teste.
- Reforçada a proteção das configurações e credenciais locais.
- Sprint 04 concluída e validada.

## Sprint 05 - Etapa 01

- Implementado HTMLBuilder.
- Implementada geração do relatório de fechamento em HTML.
- Implementada exibição do nome da loja no relatório.
- Implementada formatação monetária no padrão brasileiro.
- Implementadas data e hora automáticas do fechamento.
- Implementada proteção do nome da loja contra interpretação de HTML.
- Validada geração do conteúdo HTML pelo terminal.
- Validado visualmente o modelo do relatório no navegador.