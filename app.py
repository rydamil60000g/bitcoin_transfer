import os
import requests
from flask import Flask
from bitcoinlib.services.services import Service

app = Flask(__name__)

@app.route("/")
def hello():
    max_blocks = 50
    byte_per_tx = 250
    aud_per_btc = 1 / float(requests.get('https://blockchain.info/tobtc?currency=AUD&value=1').text)
    sec_per_block = float(requests.get('https://blockchain.info/q/interval').text)
    btc_per_byte = Service().estimatefee(max_blocks)/10**8
    bitcoin_quote = """
        {0!s} BTC / kb
        {0!s} BTC for 1 input and 2 outputs
        {0!s} $AUD
        {0!s} minutes
    """.format(
        btc_per_byte,
        btc_per_byte * byte_per_tx / 1000,
        aud_per_btc * btc_per_byte * byte_per_tx / 1000,
        max_blocks * sec_per_block / 60
    )[1:].replace('\n', '<br>')
    return bitcoin_quote

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)