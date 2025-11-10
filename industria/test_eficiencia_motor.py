import pytest
from eficiencia_motor import calcular_eficiencia, classificar_eficiencia, analise_motor

def test_calculo_eficiencia():
    resultado = calcular_eficiencia(900, 1000)
    assert resultado == 90.0, f"Esperado 90.0, mas obteve {resultado}"

    resultado = calcular_eficiencia(855, 1000)
    assert resultado == 85.5, f"Esperado 85.5, mas obteve {resultado}"

    try:
        calcular_eficiencia(900, 0)
        assert False, "Esperado erro ValueError, mas não ocorreu"
    except ValueError:
        pass 


def test_classificacao_eficiencia():
    resultado = classificar_eficiencia(75.0)
    assert resultado == "IE1 - Baixa eficiência", f"Esperado 'IE1 - Baixa eficiência', mas obteve {resultado}"

    resultado = classificar_eficiencia(85.0)
    assert resultado == "IE2 - Eficiência média", f"Esperado 'IE2 - Eficiência média', mas obteve {resultado}"

    resultado = classificar_eficiencia(92.0)
    assert resultado == "IE3 - Alta eficiência", f"Esperado 'IE3 - Alta eficiência', mas obteve {resultado}"

def test_analise_motor_integracao():
    resultado = analise_motor(880, 1000)

    assert resultado["eficiencia"] == 88.0, f"Esperado eficiência 88.0, mas obteve {resultado['eficiencia']}"

    assert resultado["classificacao"] == "IE2 - Eficiência média", f"Esperado 'IE2 - Eficiência média', mas obteve {resultado['classificacao']}"