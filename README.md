# The latest Bitcoin network data in Python/Flask.

This is a minimal Flask application, that calculates Bitcoin transfer fees in Australian dollars. It uses [bitcoinlib](https://pypi.python.org/pypi/bitcoinlib) to retrieve the current miners' fees, and obtains Bitcoin exchange rates and average block completion time via the [Blockchain.info](https://blockchain.info/q) RESTful API.

See it working [here](https://btctx-rdm.herokuapp.com).

I've included the minimal files necessary to deploy a Flask HTTP server to Heroku.

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
