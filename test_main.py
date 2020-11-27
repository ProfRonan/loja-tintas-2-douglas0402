"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
import random
import math
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_main(self):
        """Função que testa se a saída do programa corresponde ao que foi especificado."""
        # Lista de valores que serão retornados pela função input.
        area = float(random.randint(1, 1000))
        input_returns = [area]
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            cobertura = 1 / 6  # l/m^2
            lata = 18  # l / unidade
            custo_lata = 80  # R$ / unidade
            galao = 3.6  # l / unidade
            custo_galao = 25  # R$ / unidade
            folga = 1.1
            qtd_litros = area * cobertura * folga
            qtd_lata = math.ceil(qtd_litros * 1 / lata)
            valor_lata = qtd_lata * custo_lata
            qtd_galao = math.ceil(qtd_litros * 1 / galao)
            valor_galao = qtd_galao * custo_galao
            qtd_latas_misto = math.floor(qtd_litros * 1 / lata)
            valor_latas_misto = qtd_latas_misto * custo_lata
            qtd_litros_falta = qtd_litros - qtd_latas_misto * 18
            qtd_galao_misto = math.ceil(qtd_litros_falta * 1 / galao)
            valor_galao_misto = qtd_galao_misto * custo_galao
            mock_print.assert_called_with(
                f'O valor gasto comprando apenas latas é de {valor_lata}.')
            mock_print.assert_called_with(f'Serão necessárias {qtd_lata} latas.')
            mock_print.assert_called_with(
                f'O valor gasto comprando apenas galões é de {valor_galao}.')
            mock_print.assert_called_with(f'Serão necessários {qtd_galao} galões.')
            mock_print.assert_called_with(
                f'O valor gasto comprando de forma que gere a menor quantidade\
                     de desperdício é de {valor_galao_misto + valor_latas_misto}.'
            )
            mock_print.assert_called_with(
                f'Serão necessárias {qtd_latas_misto} latas e {qtd_galao_misto} galões.'
            )


if __name__ == '__main__':
    unittest.main()
