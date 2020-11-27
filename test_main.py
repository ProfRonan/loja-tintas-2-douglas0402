"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import call, patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_0(self):
        """Função que testa com area 0."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['0']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'O valor gasto comprando apenas latas é de R$ 0.00.',
                'Serão necessárias 0 latas.',
                'O valor gasto comprando apenas galões é de R$ 0.00.',
                'Serão necessários 0 galões.',
                'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 0.00.',
                'Serão necessárias 0 latas e 0 galões.'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)

    def test_5(self):
        """Função que testa com area 5."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['5']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'O valor gasto comprando apenas latas é de R$ 80.00.',
                'Serão necessárias 1 latas.',
                'O valor gasto comprando apenas galões é de R$ 25.00.',
                'Serão necessários 1 galões.',
                'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 25.00.',
                'Serão necessárias 0 latas e 1 galões.'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)

    def test_20(self):
        """Função que testa com area 20."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['20']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'O valor gasto comprando apenas latas é de R$ 80.00.',
                'Serão necessárias 1 latas.',
                'O valor gasto comprando apenas galões é de R$ 50.00.',
                'Serão necessários 2 galões.',
                'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 50.00.',
                'Serão necessárias 0 latas e 2 galões.'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)

    def test_50(self):
        """Função que testa com area 50."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['50']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'O valor gasto comprando apenas latas é de R$ 80.00.',
                'Serão necessárias 1 latas.',
                'O valor gasto comprando apenas galões é de R$ 75.00.',
                'Serão necessários 3 galões.',
                'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 75.00.',
                'Serão necessárias 0 latas e 3 galões.'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)

    def test_75(self):
        """Função que testa com area 75."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['75']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'O valor gasto comprando apenas latas é de R$ 80.00.',
                'Serão necessárias 1 latas.',
                'O valor gasto comprando apenas galões é de R$ 100.00.',
                'Serão necessários 4 galões.',
                'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 100.00.',
                'Serão necessárias 0 latas e 4 galões.'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)

    def test_100(self):
        """Função que testa com area 100."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['100']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'O valor gasto comprando apenas latas é de R$ 160.00.',
                'Serão necessárias 2 latas.',
                'O valor gasto comprando apenas galões é de R$ 150.00.',
                'Serão necessários 6 galões.',
                'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 105.00.',
                'Serão necessárias 1 latas e 1 galões.'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)

    def test_150(self):
        """Função que testa com area 150."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['150']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'O valor gasto comprando apenas latas é de R$ 160.00.',
                'Serão necessárias 2 latas.',
                'O valor gasto comprando apenas galões é de R$ 200.00.',
                'Serão necessários 8 galões.',
                'O valor gasto comprando de forma que gere a menor quantidade de desperdício é de R$ 155.00.',
                'Serão necessárias 1 latas e 3 galões.'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
