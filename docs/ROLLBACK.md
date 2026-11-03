
# Plano de Rollback — TaskFlow

## 1. Objetivo

Este documento descreve o procedimento de rollback da aplicação TaskFlow.

O rollback consiste em retornar para uma versão anterior da aplicação quando uma nova versão apresentar falhas após sua publicação.

## 2. Versionamento

O projeto utiliza versionamento semântico para identificar as versões das imagens Docker.

O padrão utilizado é:

```text
vMAJOR.MINOR.PATCH
```

Exemplos:

- v1.0.0 — primeira versão;
- v1.1.0 — inclusão de novas funcionalidades;
- v1.1.1 — correção de erros.

## 3. Situação que exige rollback

O rollback poderá ser necessário quando:

- A aplicação apresentar erros após uma atualização;
- A interface deixar de funcionar;
- A aplicação não conseguir acessar o banco de dados;
- Uma nova versão apresentar falhas identificadas nos testes.

## 4. Procedimento de rollback

Primeiramente, identificar a versão anterior que estava funcionando corretamente.

Em seguida, substituir a versão atual pela anterior.

Exemplo: retornar da versão v1.1.0 para v1.0.0.

```bash
docker pull ghcr.io/USUARIO/REPOSITORIO:v1.0.0
```

Caso a implantação utilize Docker Compose com uma imagem configurada por variável de ambiente, atualizar a versão da imagem para v1.0.0 e executar:

```bash
docker compose up -d
```

Verificar se a aplicação voltou a funcionar:

```bash
docker compose ps
```

Consultar os registros:

```bash
docker compose logs
```

Acessar a aplicação:

http://localhost:5000

## 5. Cuidados com o banco de dados

O banco SQLite utiliza armazenamento persistente por meio de volume Docker.

O rollback da aplicação não deve apagar o volume de dados.

Não utilizar o comando:

```bash
docker compose down -v
```

Esse comando pode remover os volumes e causar perda dos dados armazenados.

## 6. Resultado esperado

Após o rollback, espera-se que:

- A versão anterior da aplicação esteja em execução;
- A interface volte a funcionar;
- As tarefas cadastradas permaneçam armazenadas;
- O serviço esteja disponível novamente.
