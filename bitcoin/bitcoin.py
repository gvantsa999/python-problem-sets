import sys
import requests

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

   
    api_key = "464e863273d6ac402041a507ac17d369025be2207951faa4dcbd196528f07979"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        price = float(data["data"]["priceUsd"])
        total_cost = n * price
        
        print(f"${total_cost:,.4f}")

    except (requests.RequestException, KeyError, ValueError, TypeError):
        sys.exit("Error fetching or parsing data")

if __name__ == "__main__":
    main()