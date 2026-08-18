# TikTok hashtag volume API

TikTok hashtag and search interest trends via the Trends API. History, growth, and live trending hashtags.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) [![PyPI](https://img.shields.io/pypi/v/trendsapi-tiktok.svg)](https://pypi.org/project/trendsapi-tiktok/) [![npm](https://img.shields.io/npm/v/trendsapi-tiktok.svg)](https://www.npmjs.com/package/trendsapi-tiktok)

Key: [trendsapi.ai/#get-key](https://trendsapi.ai/#get-key). Full contract: [trendsapi-ai/trendsapi](https://github.com/trendsapi-ai/trendsapi).

## Install

### Python

```bash
pip install trendsapi-tiktok
```

```python
from trendsapi_tiktok import TrendsAPI

client = TrendsAPI()  # TRENDSAPI_KEY
series = client.get_time_series("matcha")
growth = client.get_growth("matcha", percent_growth=["12M"])
hot = client.get_live(limit=10)
```

### JavaScript

```bash
npm install trendsapi-tiktok
```

```ts
import { TrendsAPI } from "trendsapi-tiktok";

const client = new TrendsAPI({ apiKey: process.env.TRENDSAPI_KEY });
const series = await client.getTimeSeries("matcha");
const growth = await client.getGrowth("matcha", { percent_growth: ["12M"] });
const live = await client.getLive({ limit: 10 });
```


## Call

| Field | Value |
|---|---|
| Endpoint | `POST https://api.trendsapi.ai/api` |
| Auth | `Authorization: Bearer $TRENDSAPI_KEY` |
| History | `source: tiktok` with `get_time_series` or `get_growth` |
| Keyword | Hashtag or topic, e.g. matcha (`#` optional) |
| Live `type` | TikTok Trending Hashtags, TikTok Trending Searches, TikTok Shop Hot Products |

```bash
curl -sS -X POST https://api.trendsapi.ai/api \
  -H "Authorization: Bearer $TRENDSAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mode":"get_time_series","source":"tiktok","keyword":"matcha"}'
```

`value` is 0-100 for this hashtag, not view count.

`tiktok trending hashtags` (wrong case) is 400.

Publishing videos still requires TikTok's own APIs. This endpoint is demand only.

Site: [https://trendsapi.ai/trends/tiktok-trends](https://trendsapi.ai/trends/tiktok-trends).

## License

MIT. See [LICENSE](LICENSE).
