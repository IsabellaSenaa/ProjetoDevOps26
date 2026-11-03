
# Testes e Validação — TaskFlow

## 1. Objetivo

Este documento apresenta os procedimentos utilizados para validar o funcionamento da aplicação TaskFlow na segunda etapa do projeto de Integração DevOps.

Os testes verificam o funcionamento das funcionalidades principais, a execução da aplicação em contêiner Docker e a persistência dos dados.

## 2. Testes automatizados

A aplicação utiliza Pytest para executar testes automatizados.

Os testes existentes verificam:

- Criação de tarefas;
- Validação de título obrigatório;
- Conclusão de tarefas;
- Exclusão de tarefas.

### Executar os testes

No terminal, dentro da pasta principal do projeto, executar:

```bash
python -m pytest tests -v
```

## 3. Validação da imagem Docker

Para construir a imagem:

```bash
docker compose build
```

Para iniciar a aplicação:

```bash
docker compose up -d
```

Para verificar os contêineres:

```bash
docker compose ps
```

Para consultar os registros da aplicação:

```bash
docker compose logs
```

## 4. Teste de acesso à aplicação

Após iniciar os contêineres, acessar pelo navegador:

http://localhost:5000

Verificar se a interface do TaskFlow é exibida corretamente.

## 5. Teste de persistência

1. Acessar a aplicação.
2. Cadastrar uma nova tarefa.
3. Verificar se a tarefa aparece na listagem.
4. Reiniciar os contêineres:

```bash
docker compose restart
```

5. Acessar novamente a aplicação.
6. Verificar se a tarefa cadastrada continua aparecendo.

## 6. Resultado esperado

Espera-se que:

- Os testes automatizados sejam executados sem falhas;
- A imagem Docker seja construída corretamente;
- A aplicação seja iniciada pelo Docker Compose;
- A interface esteja acessível pelo navegador;
- Os dados permaneçam armazenados após a reinicialização dos contêineres.

## 7. Evidências

As evidências da execução deverão incluir:

- Resultado dos testes Pytest;
- Construção da imagem Docker;
- Contêiner em execução;
- Aplicação acessível no navegador;
- Persistência das tarefas após reinicialização.
