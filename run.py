from waybackpy import WaybackMachineSaveAPI
main = "https://fullpwn.net"
imgarchive = "https://fullpwn.net/imgarchive"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"

save_api = WaybackMachineSaveAPI(main, user_agent)
print(save_api.save())
print("Saved Main Page")
save_api = WaybackMachineSaveAPI(imgarchive, user_agent)
print(save_api.save())
print("imgarchive")

