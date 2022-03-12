import os
import nicehash
from flask import Flask, jsonify

NICEHASH_URL = "https://api2.nicehash.com"
key = os.environ.get("KEY")
secret = os.environ.get("SECRET")
organisation_id = os.environ.get("ORG_ID")
PORT = int(os.environ.get("PORT", 80))

private_api = nicehash.private_api(NICEHASH_URL, organisation_id, key, secret)

app = Flask(__name__)

@app.route('/<name>', methods=["POST"])
def get_status(name):
  rigs = private_api.get_rigs()
  rigs = rigs["miningRigs"]
  rigs = {r["name"]: r for r in rigs} #map to name:rig

  response = None

  if name in rigs:
    response = rigs[name]["minerStatus"]

  return jsonify(response)

app.run(host="0.0.0.0", port=PORT)
