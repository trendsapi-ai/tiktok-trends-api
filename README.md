# TikTok hashtag volume API

JSON hashtag-volume history and live TikTok boards via [Trends API](https://trendsapi.ai). No TikTok app, no Research API waitlist.

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). Contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Source](https://img.shields.io/badge/source-tiktok-black.svg)](https://trendsapi.ai/trends/tiktok-trends)
[![npm](https://img.shields.io/npm/v/trendsapi-tiktok.svg)](https://www.npmjs.com/package/trendsapi-tiktok)

```bash
npm install trendsapi-tiktok
```

## Call

| Field | Value |
|---|---|
| Endpoint | `POST https://api.trendsapi.ai/api` |
| Auth | `Authorization: Bearer $TRENDSAPI_KEY` |
| History | `source: tiktok` with `get_time_series` or `get_growth` |
| Keyword | Hashtag or topic, e.g. `matcha` (`#` optional) |
| Live `type` | `TikTok Trending Hashtags`, `TikTok Trending Searches`, `TikTok Shop Hot Products` |

```bash
curl -sS -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer $TRENDSAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode":"get_time_series","source":"tiktok","keyword":"matcha"}'
```

```python
from trendsapi import TrendsAPI
client = TrendsAPI()
series = client.get_time_series(source="tiktok", keyword="matcha")
hashtags = client.get_top_trends(type="TikTok Trending Hashtags", limit=10)
```

`value` is 0-100 for this hashtag, not view count. `tiktok trending hashtags` (wrong case) is 400.

Publishing videos still requires TikTok's own APIs. This endpoint is demand only.

Site: [trendsapi.ai/trends/tiktok-trends](https://trendsapi.ai/trends/tiktok-trends).

## License

MIT. See [LICENSE](LICENSE).
