from alpaca.data.live import StockDataStream, CryptoDataStream
ALPACA_API_KEY = "PKHSTPPHMOTOWZYHN5QWDXVIFL"
ALPACA_SECRET_KEY = "8VUBoZFfA9jKGCUmib3auRYKh7ZRebuxwcVJGQN1M83C"

wss_client = StockDataStream(ALPACA_API_KEY, ALPACA_SECRET_KEY, raw_data=True)

# async handler


async def quote_data_handler(data):
    # quote data will arrive here
    print(data)

wss_client.subscribe_quotes(quote_data_handler, "NBIS", "OKLO", "HOOD")

wss_client.run()
