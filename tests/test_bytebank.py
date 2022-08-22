import pytest
from bytebank import Funcionario


class TestClass:
    def test_when_age_receive_a_date_should_return_value_22(self):
        date = '13/03/2000'
        receive = 22

        employee_test = Funcionario('Jhon Doe', date, 1500)
        result = employee_test.idade()

        assert result == receive

    def test_when_surname_receive_Lucas_Carvalho_should_return_Carvalho(self):
        expect = 'Carvalho'

        employee_test = Funcionario(' Lucas Carvalho ', '13/03/2000', 1500)
        result = employee_test.surname()
        assert result == expect

    def test_decrease_salary_when_receive_100000_should_return_90000(self):
        initial_entry_salary = 100000
        initial_name = 'Paulo Bragança'
        expect = 90000

        employee_test = Funcionario(initial_name, '11/03/2000', initial_entry_salary)
        employee_test.decrease_salary()
        result = employee_test.salario

        assert result == expect

    @pytest.mark.calculate_bonuses
    def test_when_calculate_bonuses_receive_1000_should_return_100(self):
        salary = 1000  # given
        expect = 100

        employee_test = Funcionario('Jhon Doe', '11/03/2000', salary)
        result = employee_test.calcular_bonus()

        assert result == expect

    @pytest.mark.calculate_bonuses
    def test_when_calculate_bonuses_receive_150000_should_return_exception(self):
        with pytest.raises(Exception): # Take Exception
            salary = 150000  # given

            employee_test = Funcionario('Jhon Doe', '11/03/2000', salary)
            result = employee_test.calcular_bonus()

            assert result