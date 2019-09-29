import requests

API_KEY = "92f0223c-52ac-4d22-8ee4-402cf490d368"


def get_user_stats(platform, playerName):
    url = "https://api.fortnitetracker.com/v1/profile/" + platform + "/" + playerName
    headers = {
        'TRN-Api-Key': API_KEY,
        'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2'
    }
    response = requests.get(url, headers=headers).json()
    print("Wins: " + response["lifeTimeStats"][8]["value"])
    print("Win %: " + response["lifeTimeStats"][9]["value"])
    print("Kills: " + response["lifeTimeStats"][10]["value"])
    print("K/D: " + response["lifeTimeStats"][11]["value"])
    print("Matches Played: " + response["lifeTimeStats"][7]["value"])


get_user_stats("psn", "E11 Matrix")