from waybackpy import WaybackMachineSaveAPI
url = "https://fullpwn.is-a.dev"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"

save_api = WaybackMachineSaveAPI(url, user_agent)
print save_api.save()
