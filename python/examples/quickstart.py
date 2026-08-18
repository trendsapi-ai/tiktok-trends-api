from trendsapi_tiktok import TrendsAPI

client = TrendsAPI()  # TRENDSAPI_KEY
series = client.get_time_series('matcha')
print(series[-1])
growth = client.get_growth('matcha', percent_growth=["12M"])
print(growth["results"][0]["growth"], growth["results"][0]["direction"])
hot = client.get_live(limit=5)
print(hot["data"])
