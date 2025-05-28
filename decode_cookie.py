#!/usr/bin/python3
import zlib
import sys
import json
from itsdangerous import base64_decode


def decode(cookie):
    """
    Decode a Flask cookie

    https://www.kirsle.net/wizards/flask-session.cgi
    """
    try:
        compressed = False
        payload = cookie

        if payload.startswith('.'):
            compressed = True
            payload = payload[1:]

        data = payload.split(".")[0]

        data = base64_decode(data)
