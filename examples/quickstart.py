"""Trends API quickstart - TikTok. Get a free key at https://trendsapi.ai/#get-key"""
import json, os

import requests

res = requests.post(
    "https://api.trendsapi.ai/api",
    headers={"Authorization": f"Bearer {os.environ['TRENDSAPI_KEY']}"},
    json={
        "mode": "get_growth",
        "source": "tiktok",
        "keyword": "booktok",
        "percent_growth": ["3M", "12M"],
    },
    timeout=60,
)
res.raise_for_status()
env = res.json()
print(json.loads(env["body"]) if env.get("statusCode") == 200 else env)
