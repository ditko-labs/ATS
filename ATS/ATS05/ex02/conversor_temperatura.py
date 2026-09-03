def celsius_para_fahrenheit(temperatura_celsius):
    if isinstance(temperatura_celsius, (int, float)):
        temperatura_fahrenheit = temperatura_celsius * 9 / 5 + 32
        return round(temperatura_fahrenheit, 2)
    else:
        raise TypeError("Temperatura deve ser um valor numérico")


def fahrenheit_para_celsius(temperatura_fahrenheit):
    if isinstance(temperatura_fahrenheit, (int, float)):
        temperatura_celsius = (temperatura_fahrenheit - 32) * 5 / 9
        return round(temperatura_celsius, 2)
    else:
        raise TypeError("Temperatura deve ser um valor numérico")
