from waybackpy import WaybackMachineSaveAPI
main = "https://fullpwn.is-a.dev"
whatsnew = "https://fullpwn.is-a.dev/whats-new/"
new = "https://fullpwn.is-a.dev/new"
preview = "https://fullpwn.is-a.dev/preview/"
archive = "https://fullpwn.is-a.dev/archive/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"

save_api = WaybackMachineSaveAPI(main, user_agent)
print(save_api.save())
print("Saved Main Page")
save_api = WaybackMachineSaveAPI(whatsnew, user_agent)
print(save_api.save())
print("Saved What's New")
save_api = WaybackMachineSaveAPI(new, user_agent)
print(save_api.save())
print("Saved new")
save_api = WaybackMachineSaveAPI(preview, user_agent)
print(save_api.save())
print("Saved Preview")
save_api = WaybackMachineSaveAPI(archive, user_agent)
print(save_api.save())
print("Saved Archive")
