# Especificação do exercício

Faça um script para uma loja de tintas.
O script deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

1. comprar apenas latas de 18 litros;
2. comprar apenas galões de 3,6 litros;
3. misturar latas e galões, de forma que o desperdício de tinta seja menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

O script deve exibir a saída da seguinte forma, substituindo `(valor)` e `(quantidades)` pelos números correspondentes:

```markdown
O valor gasto comprando apenas latas é de (valor).
Serão necessárias (quantidade) latas.
O valor gasto comprando apenas galões é de (valor).
Serão necessários (quantidade) galões.
O valor gasto comprando de forma que gere a menor quantidade de desperdício é de (valor).
Serão necessárias (quantidade) latas e (quantidade) galões.
```

Lembre-se de formatar a saída usando `f'string'`.
Utilize um `print` para cada linha acima.
