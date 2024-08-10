import requests

site1 = requests.get("https://developers.institute/").elapsed.total_seconds()
site2 = requests.get("https://www.google.com/").elapsed.total_seconds()
site3 = requests.get("https://www.timesofisrael.com/").elapsed.total_seconds()
site4 = requests.get("https://www.skysports.com/").elapsed.total_seconds()


def time_to_load():
    print(f"It took {site1} seconds to load Developers Institute")
    print(f"It took {site2} seconds to load Google")
    print(f"It took {site3} seconds to load Times of Israel")
    print(f"It took {site4} seconds to load Skysports")


def fastest_site():
    all_sites = (site1, site2, site3, site4)
    min_index = all_sites.index(min(all_sites))
    get_min = min(all_sites)
    site_name = ""
    if min_index == 0:
        site_name = "Developers Institute"
    elif min_index == 1:
        site_name = "Google"
    elif min_index == 2:
        site_name = "Times of Israel"
    elif min_index == 3:
        site_name = "Skysports"
    print(f"\nThe fastest site was {site_name} at {get_min} seconds")


time_to_load()
fastest_site()
