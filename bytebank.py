from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        date_nasc_breaked = self._data_nascimento.split('/')
        year_nasc = date_nasc_breaked[-1]
        ano_atual = date.today().year
        return ano_atual - int(year_nasc)

    def surname(self):
        complete_name = self.nome.strip()
        name_breaked = complete_name.split(' ')

        return name_breaked[-1]

    def _is_partner(self):
        surnames = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tour', 'Ptolomeu']
        return self._salario >= 100000 and (self.surname() in surnames)

    def decrease_salary(self):
        if self._is_partner():
            salary_decrease_ten_percent = self._salario * 0.1
            self._salario = self._salario - salary_decrease_ten_percent

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus.')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
