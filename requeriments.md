# NexDex — Especificação de Requisitos de Software (ERS)

**Projeto:** NexDex  
**Tipo de sistema:** Gerenciamento de chamados de TI (Help Desk)  
**Versão do documento:** 1.0  
**Status:** Em desenvolvimento  
**Tecnologias atuais:** Python e SQLite
**Dev:** Tiago Emanuel dos Santos Vieira (SkyBl4ze) https://github.com/SkyBl4ze/nexdex

---

## 1. Introdução

### 1.1. Objetivo

Este documento tem como objetivo definir os requisitos funcionais e não funcionais do NexDex, um sistema destinado ao gerenciamento de chamados de suporte técnico em Tecnologia da Informação (TI).

A documentação estabelece as funcionalidades esperadas, as regras de negócio, as restrições técnicas e os critérios básicos de qualidade do sistema, servindo como referência para o desenvolvimento, os testes e futuras melhorias.

### 1.2. Escopo do sistema

O NexDex tem como finalidade centralizar o registro e o acompanhamento de solicitações de suporte técnico, permitindo organizar informações sobre problemas, solicitações e atividades relacionadas à infraestrutura de TI.

Na primeira etapa, o sistema será executado por meio de um terminal, utilizando Python para implementar a lógica da aplicação e SQLite para persistir os dados.

Em etapas futuras, o projeto poderá evoluir para uma aplicação web com autenticação, controle de permissões, painel administrativo e recursos adicionais de gerenciamento.

### 1.3. Público-alvo

O sistema destina-se principalmente a:

- Técnicos de suporte e profissionais de help desk.
- Equipes de Tecnologia da Informação.
- Solicitantes que necessitam registrar problemas ou solicitar serviços de TI.
- Administradores responsáveis pelo gerenciamento do ambiente de suporte.

O acesso por diferentes perfis de usuário será implementado em etapas posteriores.

### 1.4. Definições e siglas

- **NexDex:** nome do sistema de gerenciamento de chamados.
- **Help Desk:** serviço responsável por receber e tratar solicitações de suporte.
- **Chamado:** registro de uma solicitação, incidente ou problema técnico.
- **SQLite:** sistema de gerenciamento de banco de dados relacional.
- **CRUD:** operações de criação, consulta, atualização e exclusão de registros.
- **ERS:** Especificação de Requisitos de Software.
- **RF:** Requisito Funcional.
- **RNF:** Requisito Não Funcional.
- **ID:** identificador único de um registro.

---

## 2. Descrição geral

### 2.1. Perspectiva do produto

O NexDex é uma aplicação independente, inicialmente desenvolvida para execução local.

A arquitetura inicial é composta por:

1. Interface textual executada no terminal.
2. Camada de lógica de negócio implementada em Python.
3. Camada de persistência de dados utilizando SQLite.

A separação dessas responsabilidades deverá facilitar a manutenção e permitir uma futura migração para uma arquitetura com API e interface web.

### 2.2. Funções principais

O sistema deverá permitir:

- Registrar chamados de suporte técnico.
- Armazenar informações dos chamados em um banco de dados.
- Consultar chamados previamente registrados.
- Pesquisar chamados por identificador.
- Atualizar informações e estados dos chamados.
- Excluir registros conforme as regras definidas.
- Organizar chamados por categoria, prioridade e status.

As funcionalidades deverão ser implementadas progressivamente.

### 2.3. Restrições

- A primeira versão deverá utilizar Python como linguagem principal.
- O banco de dados inicial deverá ser SQLite.
- A aplicação deverá funcionar localmente por meio do terminal.
- A interface gráfica e a aplicação web não fazem parte do escopo inicial.
- A implementação deverá priorizar simplicidade, legibilidade e facilidade de manutenção.

---

## 3. Requisitos funcionais

Os requisitos funcionais descrevem as operações que o sistema deverá executar.

| ID | Requisito | Descrição | Prioridade |
|---|---|---|---|
| RF01 | Criar chamado | Permitir o registro de um novo chamado com as informações necessárias. | Alta |
| RF02 | Gerar identificador | Atribuir um identificador único a cada chamado. | Alta |
| RF03 | Persistir dados | Armazenar os chamados no banco de dados SQLite. | Alta |
| RF04 | Listar chamados | Recuperar e exibir os chamados cadastrados. | Alta |
| RF05 | Consultar chamado | Localizar um chamado específico por seu identificador. | Alta |
| RF06 | Atualizar chamado | Permitir a alteração dos dados de um chamado. | Média |
| RF07 | Alterar status | Permitir a atualização do estado de atendimento de um chamado. | Alta |
| RF08 | Excluir chamado | Permitir a remoção de um chamado conforme as regras estabelecidas. | Média |
| RF09 | Validar entradas | Impedir o registro de informações inválidas ou campos obrigatórios vazios. | Alta |
| RF10 | Categorizar chamados | Classificar chamados por categoria. | Média |
| RF11 | Definir prioridade | Permitir a classificação da prioridade do chamado. | Alta |
| RF12 | Informar solicitante | Registrar quem abriu o chamado. | Média |
| RF13 | Atribuir técnico | Permitir associar um técnico responsável ao chamado. | Média |
| RF14 | Registrar datas | Armazenar as datas de criação e atualização dos chamados. | Média |
| RF15 | Apresentar mensagens | Informar ao usuário o resultado das operações realizadas. | Alta |

**Observação:** a existência de um requisito nesta tabela não significa que ele já esteja implementado. Os requisitos representam o comportamento esperado para a versão planejada do sistema.

---

## 4. Requisitos não funcionais

Os requisitos não funcionais definem características de qualidade, segurança e operação.

| ID | Requisito | Descrição |
|---|---|---|
| RNF01 | Usabilidade | O menu do terminal deverá apresentar opções claras e mensagens compreensíveis. |
| RNF02 | Persistência | Os dados deverão continuar disponíveis após o encerramento da aplicação. |
| RNF03 | Integridade | O sistema deverá preservar a consistência dos registros armazenados. |
| RNF04 | Manutenibilidade | O código deverá ser organizado em módulos e funções com responsabilidades definidas. |
| RNF05 | Portabilidade | A aplicação deverá utilizar recursos compatíveis com os ambientes Python suportados. |
| RNF06 | Tratamento de erros | Erros de entrada e falhas previsíveis de banco de dados deverão ser tratados adequadamente. |
| RNF07 | Segurança | As operações com o banco deverão utilizar consultas parametrizadas para reduzir riscos de injeção SQL. |
| RNF08 | Desempenho | As consultas deverão apresentar resultados em tempo adequado para o volume de dados previsto para a aplicação. |
| RNF09 | Evolutividade | A arquitetura deverá permitir a inclusão futura de uma API e de uma interface web. |
| RNF10 | Documentação | O projeto deverá possuir instruções de instalação, execução e utilização. |

---

## 5. Regras de negócio

As regras de negócio estabelecem condições que deverão ser respeitadas durante a utilização do sistema.

- **RN01 — Identificação:** todo chamado deverá possuir um identificador único.
- **RN02 — Título:** o título do chamado deverá ser obrigatório.
- **RN03 — Descrição:** o chamado deverá conter uma descrição do problema ou da solicitação.
- **RN04 — Categoria:** cada chamado deverá possuir uma categoria válida.
- **RN05 — Prioridade:** cada chamado deverá possuir uma prioridade definida conforme os valores aceitos pelo sistema.
- **RN06 — Status inicial:** um novo chamado deverá ser criado com o status padrão “Aberto”.
- **RN07 — Atualização:** as alterações realizadas deverão ser persistidas no banco de dados.
- **RN08 — Exclusão:** um chamado somente deverá ser excluído após a identificação correta do registro.
- **RN09 — Consistência:** um chamado inexistente não poderá ser alterado ou excluído.
- **RN10 — Responsabilidade:** quando houver atribuição de técnicos, o sistema deverá identificar o responsável pelo atendimento.

As regras relacionadas a técnicos, usuários e permissões dependerão da implementação desses recursos.

---

## 6. Modelo de dados

### 6.1. Entidade Chamado

A entidade `chamados` representa os registros de solicitações de suporte.

| Campo | Tipo sugerido | Descrição |
|---|---|---|
| `id` | INTEGER | Identificador único e chave primária. |
| `titulo` | TEXT | Título resumido do chamado. |
| `descricao` | TEXT | Detalhamento do problema ou solicitação. |
| `categoria` | TEXT | Classificação do chamado. |
| `prioridade` | TEXT ou INTEGER | Nível de prioridade. |
| `status` | TEXT | Estado atual do atendimento. |
| `solicitante` | TEXT ou INTEGER | Identificação de quem abriu o chamado. |
| `tecnico` | TEXT ou INTEGER | Identificação do técnico responsável. |
| `data_criacao` | TEXT | Data e horário de criação. |
| `data_atualizacao` | TEXT | Data e horário da última atualização. |

Os campos adicionais representam uma proposta de evolução do modelo. Os tipos definitivos e a obrigatoriedade de cada campo deverão ser definidos na implementação.

### 6.2. Persistência

Os dados deverão ser armazenados em um banco SQLite local. As operações de inserção, consulta, atualização e exclusão deverão ser realizadas por meio das funcionalidades disponibilizadas pelo módulo `sqlite3` do Python.

A estrutura do banco deverá ser mantida consistente com o modelo de dados adotado pelo sistema.

---

## 7. Fluxos principais

### 7.1. Abertura de chamado

1. O usuário seleciona a opção de criação de chamado.
2. O sistema solicita as informações necessárias.
3. Os dados informados são validados.
4. O sistema registra o chamado no banco de dados.
5. O sistema informa se a operação foi concluída.

### 7.2. Consulta de chamados

1. O usuário seleciona a opção de consulta.
2. O sistema recebe o identificador ou solicita a listagem geral.
3. O banco de dados é consultado.
4. Os resultados são apresentados no terminal.
5. Caso nenhum registro seja encontrado, o sistema informa a situação.

### 7.3. Atualização de status

1. O usuário informa o identificador do chamado.
2. O sistema verifica se o registro existe.
3. O usuário seleciona o novo status.
4. O sistema valida a alteração.
5. A atualização é persistida e seu resultado é informado.

### 7.4. Exclusão de chamado

1. O usuário informa o identificador do chamado.
2. O sistema verifica a existência do registro.
3. O sistema solicita confirmação antes da exclusão.
4. A operação é realizada.
5. O sistema informa o resultado.

---

## 8. Critérios de aceitação

O sistema será considerado funcional para sua primeira etapa quando atender aos seguintes critérios:

- [ ] Permitir o cadastro de chamados com dados válidos.
- [ ] Armazenar os registros no SQLite.
- [ ] Recuperar os dados armazenados após reiniciar a aplicação.
- [ ] Listar os chamados cadastrados.
- [ ] Consultar um chamado pelo identificador.
- [ ] Tratar tentativas de consulta a registros inexistentes.
- [ ] Validar os campos obrigatórios.
- [ ] Permitir a alteração do status.
- [ ] Tratar erros previsíveis de entrada e persistência.
- [ ] Disponibilizar instruções para executar o projeto.

Os itens deverão ser marcados conforme forem implementados e testados.

---

## 9. Evolução planejada

A evolução do NexDex será dividida em etapas para manter o desenvolvimento incremental.

**Etapa 1 — Back-end local**

- Implementação das operações de gerenciamento de chamados.
- Persistência com SQLite.
- Interação pelo terminal.
- Validação de dados e tratamento de erros.
- Organização do código em módulos.

**Etapa 2 — API**

- Introdução do FastAPI.
- Disponibilização de endpoints para operações com chamados.
- Validação das requisições.
- Padronização das respostas e dos erros.

**Etapa 3 — Autenticação e permissões**

- Cadastro e autenticação de usuários.
- Perfis de solicitante, técnico e administrador.
- Controle de acesso às operações.
- Associação de chamados a solicitantes e técnicos.

**Etapa 4 — Interface web**

- Desenvolvimento de uma interface para gerenciamento dos chamados.
- Painel de acompanhamento.
- Filtros por status, categoria e prioridade.
- Exibição de indicadores e estatísticas.

**Etapa 5 — Recursos avançados**

- Comentários e comunicação sobre chamados.
- Histórico de alterações.
- Gerenciamento de setores e equipamentos.
- Anexos e documentação dos atendimentos.
- Relatórios e melhorias operacionais.

As etapas futuras são propostas de evolução, não funcionalidades já disponíveis.

---

## 10. Considerações finais

O NexDex tem como objetivo evoluir de uma aplicação de terminal para um sistema de gerenciamento de chamados de TI mais completo, mantendo uma arquitetura organizada e preparada para expansão.

Esta especificação deverá ser revisada conforme novas decisões de projeto forem tomadas, os requisitos forem implementados e os testes revelarem necessidades adicionais.

**Documento:** Especificação de Requisitos de Software — NexDex  
**Versão:** 1.0  
**Situação:** Documento inicial para orientar o desenvolvimento.
