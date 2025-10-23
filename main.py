from alpaca.data.live import StockDataStream, CryptoDataStream
import os
from dotenv import load_dotenv

load_dotenv()
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
print(ALPACA_API_KEY, ALPACA_SECRET_KEY)
wss_client = StockDataStream(ALPACA_API_KEY, ALPACA_SECRET_KEY, raw_data=True)

# async handler


async def quote_data_handler(data):
    # quote data will arrive here
    print(data)

wss_client.subscribe_quotes(quote_data_handler, "NBIS", "OKLO", "HOOD")

if __name__ == "__main__":
    # wss_client.run()
    print("Testing boot trader...")
