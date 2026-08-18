import { TrendsAPI } from "trendsapi-tiktok";

const client = new TrendsAPI({ apiKey: process.env.TRENDSAPI_KEY });
const series = await client.getTimeSeries("matcha");
console.log(series.at(-1));
