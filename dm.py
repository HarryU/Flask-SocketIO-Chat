#!/bin/env python
from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app, certfile="/etc/letsencrypt/live/153.duckdns.org/fullchain.pem", keyfile="/etc/letsencrypt/live/153.duckdns.org/privkey.pem")
