import requests


def get_exchange_rates(base_currency):
  # Using a free, reliable open API for live currency exchange rates
  url = f"https://open.er-api.com/v6/latest/{base_currency.upper()}"
  try:
    response = requests.get(url)
    data = response.json()
    if data["result"] == "success":
      return data["rates"]
    else:
      return None
  except Exception as e:
    print(f"\033[91m[-] Network Error: {e}\033[0m")
    return None


def currency_converter():
  print("\n" + "=" * 50)
  print("        PYTHON LIVE CURRENCY CONVERTER & TRACKER")
  print("=" * 50)

  base = input("Enter base currency (e.g., USD, EUR, GBP,): ").strip()
  rates = get_exchange_rates(base)

  if not rates:
    print("\033[91m[-] Failed to fetch rates. Please check your currency code or internet connection.\033[0m")
    return

  print(f"\n\033[92m[+] Successfully fetched live rates for {base.upper()}!\033[0m")
  
  target = input("Enter target currency to convert to (e.g., EUR, INR, CAD): ").strip().upper()

  if target not in rates:
    print(f"\033[91m[-] Currency '{target}' not found in live data.\033[0m")
    return

  try:
    amount = float(input(f"Enter amount in {base.upper()}: "))
  except ValueError:
    print("\033[91m[-] Invalid amount entered. Please enter a number.\033[0m")
    return

  converted_amount = amount * rates[target]

  print("\n" + "=" * 50)
  print("                   CONVERSION RESULT")
  print("=" * 50)
  print(f"💱 Live Rate : 1 {base.upper()} = {rates[target]:.4f} {target}")
  print(f"💰 Converted : {amount:,.2f} {base.upper()} = \033[92m{converted_amount:,.2f} {target}\033[0m")
  print("=" * 50 + "\n")


if __name__ == "__main__":
  currency_converter()