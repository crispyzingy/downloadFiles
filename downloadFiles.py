import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(res.status_code)  # 200 means fine
print(len(res.text))
print(res.text[:500])

res.raise_for_status()  # simple check for success, raises exception if download fails

playFile = open("RomeoAndJuliet.txt", "wb")  # wb: to maintain unicode

# For converting website to file
# for chunk in res.iter_content(100000):
#     playFile.write(chunk)
# playFile.close()
