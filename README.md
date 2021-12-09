# **Considerações iniciais**
* Necessário configurar credenciais para API GMAIL
* Necessário criar par de chaves RS256

# 1. Cadastro

## Requisição

Requisição para fazer cadastro de usuário no sistema.

- Parâmetros para cadastro:
    - login
    - email

<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>POST</td>
<td>/cadastro</td>
</tr>
</tbody>
</table> 


<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Content-Type</td>
<td>application/json</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Request Body</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>

```json
{
"login" : "nome_de_login",
"email" : "exemplo@email.com"
}
```

</td>
</tr>
</tbody>
</table>



## Resposta

Quando feito com dados válidos, o sistema deve criar o usuário, mandar um email com sua chave de acesso e retornar o status Code 201 Created (Criado).

<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
    "message" : "Usuario criado com sucesso!"
}
```

</td>
</tr>
</table>

# 2. Login

## Requisição

<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>POST</td>
<td>/login</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Content-Type</td>
<td>application/json</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Request Body</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>

```json
{
"login" : "nome_de_login",
"apiKey" : "apiKeyexemploAOka63m5sn4diAU541"
}
```

</td>
</tr>
</tbody>
</table>



## Resposta

Caso os dados estejam corretos, será retornado um token de acesso e status Code 200 OK.

<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
 "access_token" : "Token.de.acesso"
}
```

</td>
</tr>
</table>



Caso algum dado esteja incorreto, será retornado status Code 401 Unauthorized (Não autorizado).

<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 401 </td>
<td>

```json
{
 "message" : "Dados inválidos"
}
```

</td>
</tr>
</table>



# 3. Logout

## Requisição

<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>POST</td>
<td>/logout</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Content-Type</td>
<td>application/json</td>
</tr>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, o usuário sairá da sessão atual e retornará status Code 200 OK.

<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
    "message": "Logout feito com sucesso!"
}
```

</td>
</tr>
</table>

# 4.Relatórios
## Requisição
<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/relatorios</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Content-Type</td>
<td>application/json</td>
</tr>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, será retornado uma lista com todos os relatórios e status Code 200 OK.

<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
    "relatorios": [
        {
            "commit_id": 1,
            "id_estacao": 3,
            "nome_estacao": "Nome",
            "dataHora": "2021-10-01 17:18:00",
            "umidade": 120,
            "pressaoAtmosferica": 200,
            "direcaoVento": 2,
            "velocidadeVento": 5,
            "pluviometro": 3,
            "radiacaoSolar": 3,
            "temperaturaAr": 25,
        }
    ]
}
```

</td>
</tr>
</table>

- <font color='#e91f1f'> **obs: esses dados são meramente ilustrativos** </font>

## Requisição
Postagem de relatórios poderá ser feito somente por estações. Os relatórios devem vir numa lista caso haja problemas de conexão e precise armazenar mais de um relatório.
<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>POST</td>
<td>/relatorios</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Content-Type</td>
<td>application/json</td>
</tr>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th><strong>Request Body</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>

```json
{
    "lista": [
        {
            "dataHora": "2021-10-01 17:18:00",
            "id_estacao": 3,
            "umidade": 120,
            "pressaoAtmosferica": 200,
            "direcaoVento": 2,
            "velocidadeVento": 5,
            "pluviometro": 3,
            "radiacaoSolar": 3,
            "temperaturaAr": 25,
        }
    ]
}

```

</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token e dados estejam válidos, será retornado uma lista com todos os relatórios postados e status Code 200 OK.

<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
    [
    {
        "dataHora": "2021-10-01 17:18:00",
        "id_estacao": 3,
        "umidade": 120,
        "pressaoAtmosferica": 200,
        "direcaoVento": 2,
        "velocidadeVento": 5,
        "pluviometro": 3,
        "radiacaoSolar": 3,
        "temperaturaAr": 25,
    }
]
}
```

</td>
</tr>
</table>

- <font color='#e91f1f'> **obs: esses dados são meramente ilustrativos** </font>

# 5. Estações
## Requisição
<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/estacoes</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, será retornado uma lista com todos as estações contendo suas informações e relatórios e status Code 200 OK.

<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
    "estacoes": [
        {
            "id_estacao": 1,
            "nome": "Estacao 1",
            "relatorios": []
        },
        {
            "id_estacao": 2,
            "nome": "Estacao 2",
            "relatorios": []
        }
    ]
}
```

</td>
</tr>
</table>

# 6. Estação {nome}
## Requisição
<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/estacao/{nome}</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, será retornado a estação contendo suas informações e relatórios e status Code 200 OK.

Exemplo de resposta para '/estacao/Estacao 1'
<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
    "id_estacao": 1,
    "nome": "Estacao 1",
    "relatorios": []
}
```

</td>
</tr>
</table>

## Requisição
Esse recurso poderá ser utilizado apenas por usuário administrador

<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>POST</td>
<td>/estacao/{nome}</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, será retornado os dados da estação criada e status Code 201 Created.

Exemplo de resposta para '/estacao/Estacao 1'
<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 201 </td>
<td>

```json
{
    "id_estacao": 1,
    "nome": "Estacao 1",
    "relatorios": []
}
```

</td>
</tr>
</table>

## Requisição
Esse recurso poderá ser utilizado apenas por usuário administrador

<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>DELETE</td>
<td>/estacao/{nome}</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, a estação de nome escolhido será deletado e retornará status Code 200 OK.
<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
    "message": "Estação deletada com sucesso"
}
```

</td>
</tr>
</table>

# 7. Usuarios/estacoes
## Requisição
Esse recurso poderá ser utilizado apenas por usuário administrador
<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/usuarios/estacoes</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, será retornado a lista de informações de usuários que devem ser utilizados em estações e status Code 200 OK.
<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
    "estacoes": [
        {
            "user_id": 1,
            "login": "Estacao 1",
            "apiKey": "ApiKeyexemplo1237svgsad8v78"
        },
        {
            "user_id": 2,
            "login": "Estacao 2",
            "apiKey": "ApiKeyexemploan2hbgh839bhaa"
        }
    ]
}
```

</td>
</tr>
</table>

# 8. Usuarios/{user_id}
## Requisição
Esse recurso poderá ser utilizado apenas por usuário administrador
<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/usuarios/{user_id}</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, será retornado informações do usuário e status Code 200 OK.
<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
    "user_id": 1,
    "login": "Usuario",
    "apiKey": "ApiKeyexemplo1254svgsad8v78"
}
```

</td>
</tr>
</table>

## Requisição
Esse recurso poderá ser utilizado apenas por usuário administrador
<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>DELETE</td>
<td>/usuarios/{user_id}</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, o usuário identificado pelo {user_id} será deletado e retornará status Code 200 OK.
<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
[
    {
        "message": "Usuario deletado"
    }
]
```

</td>
</tr>
</table>

# 8. Adm_relatorio/{commit_id}
## Requisição
Esse recurso poderá ser utilizado apenas por usuário administrador
<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>GET</td>
<td>/adm_relatorio/{commit_id}</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, será retornado o relatório e status Code 200 OK.

Exemplo de resposta para '/adm_relatorio/1'
<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
{
    "commit_id": 1,
    "id_estacao": 3,
    "nome_estacao": "Estação_3",
    "dataHora": "2021-10-01 17:18:00",
    "umidade": 120,
    "pressaoAtmosferica": 200,
    "direcaoVento": 2,
    "velocidadeVento": 5,
    "pluviometro": 3,
    "radiacaoSolar": 3,
    "temperaturaAr": 3,
}
```

</td>
</tr>
</table>

- <font color='#e91f1f'> **obs: esses dados são meramente ilustrativos** </font>

## Requisição
Esse recurso poderá ser utilizado apenas por usuário administrador
<table>
<thead>
<tr>
<th><strong>Method</strong></th>
<th><strong>URL</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>DELETE</td>
<td>/adm_relatorio/{commit_id}</td>
</tr>
</tbody>
</table> 

<table>
<thead>
<tr>
<th><strong>Headers</strong></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Authorization</td>
<td>Bearer {access_token}</td>
</tr>
</tbody>
</table>

## Resposta
Caso o access_token esteja válido, o relatório identificado pelo {commit_id} será deletado e retornará status Code 200 OK.

Exemplo de resposta para '/adm_relatorio/1'
<table>
<tr>
<td> <strong>Status</strong> </td> <td> <strong>Response</strong> </td>
</tr>
<tr>
<td> 200 </td>
<td>

```json
[
    {
        "message": "Relatorio deletado"
    }
]
```

</td>
</tr>
</table>
