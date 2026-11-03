import time
import yfinance as yf
from forex_python.converter import CurrencyRates

def monitorar_forex():
    c = CurrencyRates()
    while True:
        try:
            rate = c.get_rate('USD', 'BRL')
            print(f"Taxa USD/BRL: {rate}")
            
            if rate < 5.00:
                print("Alerta: Dólar abaixo de 5.00 - Considerar compra")
            
            time.sleep(1)
        except Exception as e:
            print(f"Erro: {e}")
            break

print(monitorar_forex)