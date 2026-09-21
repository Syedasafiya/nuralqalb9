# -*- coding: utf-8 -*-
"""
Asma ul Husna — Flask backend.

Run:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000
"""

import random
from flask import Flask, jsonify, render_template, request

from data.names import NAMES, get_all, get_one, search

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # keep Arabic readable in responses


# ----------------------------- pages -----------------------------

@app.route("/")
def index():
    return render_template("index.html")


# ------------------------------ api ------------------------------

@app.route("/api/names")
def api_names():
    """List all names. Optional ?q=search-term"""
    q = request.args.get("q", "")
    data = search(q) if q else get_all()
    return jsonify({"count": len(data), "names": data})


@app.route("/api/names/<int:name_id>")
def api_name(name_id):
    """Full detail for one name — this is what a card click calls."""
    name = get_one(name_id)
    if name is None:
        return jsonify({"error": "Name not found", "id": name_id}), 404

    prev_id = name_id - 1 if name_id > 1 else len(NAMES)
    next_id = name_id + 1 if name_id < len(NAMES) else 1

    payload = dict(name)
    payload["prev_id"] = prev_id
    payload["next_id"] = next_id
    return jsonify(payload)


@app.route("/api/random")
def api_random():
    """A random name — used for 'Name of the moment'."""
    return jsonify(random.choice(NAMES))


@app.errorhandler(404)
def not_found(_e):
    if request.path.startswith("/api/"):
        return jsonify({"error": "Not found"}), 404
    return render_template("index.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
