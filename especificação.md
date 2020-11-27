# Especificação do exercício

Faça um script para uma loja de tintas.
O script deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

1. comprar apenas latas de 18 litros;
2. comprar apenas galões de 3,6 litros;
3. misturar latas e galões, de forma que o desperdício de tinta seja menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

O script deve exibir a saída da seguinte forma, substituindo `[valor]` e `[quantidades]` pelos números correspondentes:

```markdown
O valor gasto comprando apenas latas é de R$ [valor com duas casas decimais].
Serão necessárias [quantidade] latas.
O valor gasto comprando apenas galões é de R$ [valor com duas casas decimais].
Serão necessários [quantidade] galões.
O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ [valor com duas casas decimais].
Serão necessárias [quantidade] latas e [quantidade] galões.
```

Lembre-se de formatar a saída usando `f'string'`.
Utilize um `print` para cada linha acima.

## Exemplo

Entrada 1: `0`

Saída 1:

```markdown
O valor gasto comprando apenas latas é de R$ 0.00.
Serão necessárias 0 latas.
O valor gasto comprando apenas galões é de R$ 0.00.
Serão necessários 0 galões.
O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 0.00.
Serão necessárias 0 latas e 0 galões.
```

Entrada 2: `5`

Saída 2:

```markdown
O valor gasto comprando apenas latas é de R$ 80.00.
Serão necessárias 1 latas.
O valor gasto comprando apenas galões é de R$ 25.00.
Serão necessários 1 galões.
O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 25.00.
Serão necessárias 0 latas e 1 galões.
```

Entrada 3: `20`

Saída 3:

```markdown
O valor gasto comprando apenas latas é de R$ 80.00.
Serão necessárias 1 latas.
O valor gasto comprando apenas galões é de R$ 50.00.
Serão necessários 2 galões.
O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 50.00.
Serão necessárias 0 latas e 2 galões.
```

Entrada 4: `50`

Saída 4:

```markdown
O valor gasto comprando apenas latas é de R$ 80.00.
Serão necessárias 1 latas.
O valor gasto comprando apenas galões é de R$ 75.00.
Serão necessários 3 galões.
O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 75.00.
Serão necessárias 0 latas e 3 galões.
```

Entrada 5: `75`

Saída 5:

```markdown
O valor gasto comprando apenas latas é de R$ 80.00.
Serão necessárias 1 latas.
O valor gasto comprando apenas galões é de R$ 100.00.
Serão necessários 4 galões.
O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 100.00.
Serão necessárias 0 latas e 4 galões.
```

Entrada 6: `100`

Saída 6:

```markdown
O valor gasto comprando apenas latas é de R$ 160.00.
Serão necessárias 2 latas.
O valor gasto comprando apenas galões é de R$ 150.00.
Serão necessários 6 galões.
O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 105.00.
Serão necessárias 1 latas e 1 galões.
```

Entrada 7: `150`

Saída 7:

```markdown
O valor gasto comprando apenas latas é de R$ 160.00.
Serão necessárias 2 latas.
O valor gasto comprando apenas galões é de R$ 200.00.
Serão necessários 8 galões.
O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 155.00.
Serão necessárias 1 latas e 3 galões.
```
