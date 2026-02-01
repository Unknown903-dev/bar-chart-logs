import re
from collections import Counter
from urllib.parse import urlparse

import requests
from flask import Flask, jsonify, Response

app = Flask(__name__)


##############################################
# insert the URL here
LOG_URL = "https://example.com/logs"
#############################################


#filter the endpoint 
ENDPOINT_RE = re.compile(r"Endpoint\s+(\S+)")

ALLOWED_HOSTS = {urlparse(LOG_URL).hostname}


def compute_top_endpoints(top_n: int = 10) -> dict:
    r = requests.get(LOG_URL, timeout=3)
    r.raise_for_status()

    lines = r.text.splitlines()

    counts = Counter()

    # skip first line; parse rest
    for line in lines[1:]:
        m = ENDPOINT_RE.search(line)
        if not m:
            continue
        endpoint = m.group(1)
        
        #skip these endpoints
        if endpoint == "/":
            continue
        if endpoint == "/favicon.ico":
            continue
        if endpoint == "/memes":
            continue
        if endpoint == "/logs":
            continue
        
        counts[endpoint] += 1

    # return top N as ordered dict like mapping
    return dict(counts.most_common(top_n))


@app.get("/api/top-endpoints")
def top_endpoints():
    data = compute_top_endpoints(20)

    # Convert mapping -> list of {endpoint,count} for frontend
    payload = [{"endpoint": k, "count": v} for k, v in data.items()]
    return jsonify(payload)


@app.get("/")
def dashboard():
    # render the chart 
    html = """<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Top Endpoints</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
  <h2>Top 20 Endpoints</h2>
  <canvas id="chart" width="900" height="350"></canvas>

  <script>
    async function load() {
      const res = await fetch("/api/top-endpoints");
      const data = await res.json();

      const labels = data.map(x => x.endpoint);
      const values = data.map(x => x.count);

      const ctx = document.getElementById("chart").getContext("2d");
      new Chart(ctx, {
        type: "bar",
        data: { labels, datasets: [{ label: "Requests", data: values }] },
        options: { responsive: true }
      });
    }
    load();
  </script>
</body>
</html>"""
    return Response(html, mimetype="text/html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

