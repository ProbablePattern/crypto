# First time install
#pip3 install ccxt

import ccxt
kraken = ccxt.kraken()
for trade in kraken.fetch_trades('BTC/USD'):
    print(
        f"date: {trade['datetime']} | " +
        f"symbol: {trade['symbol']} | " +
        f"price: {trade['price']} | " +
        f"amount: {trade['amount']} | " +
        f"cost: {trade['cost']} | " +
        f"side: {trade['side']} | " +
        f"type: {trade['type']}"
    )

# Try cryptofeed as well