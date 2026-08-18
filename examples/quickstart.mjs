// Trends API quickstart - TikTok. Get a free key at https://trendsapi.ai/#get-key
const res = await fetch("https://api.trendsapi.ai/api", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.TRENDSAPI_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    mode: "get_growth",
    source: "tiktok",
    keyword: "booktok",
    percent_growth: ["3M", "12M"],
  }),
});
if (!res.ok) throw new Error(`HTTP ${res.status}`);
const env = await res.json();
console.log(env.statusCode === 200 ? JSON.parse(env.body) : env);
