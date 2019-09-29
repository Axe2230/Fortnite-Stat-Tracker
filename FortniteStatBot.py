import requests
from flask import Flask, render_template
app = Flask(__name__)#, static_folder= '/static'
#app._static_folder = '/static'

API_KEY = "92f0223c-52ac-4d22-8ee4-402cf490d368"

@app.route("/")
def get_user_stats():
    playerName = input("Enter username: ")
    platform = input("Enter platform: ").lower()
    #get_user_stats(platform, username)
    url = "https://api.fortnitetracker.com/v1/profile/" + platform + "/" + playerName
    headers = {
        'TRN-Api-Key': API_KEY,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
        # DON'T NEED THIS#
    }
    response = requests.get(url, headers=headers).json()
    #print(response.text)
    accountInfo = []
    accountInfo.append("Account ID: " + response["recentMatches"][0]["accountId"])
    accountInfo.append("Wins: " + response["lifeTimeStats"][8]["value"])
    accountInfo.append("Win percentage: " + response["lifeTimeStats"][9]["value"])
    accountInfo.append("Kills: " + response["lifeTimeStats"][10]["value"])
    accountInfo.append("K/D: " + response["lifeTimeStats"][11]["value"])
    accountInfo.append("Matches Played: " + response["lifeTimeStats"][7]["value"])
    #strcat = ""
    #strcat+="Account ID: " + response["recentMatches"][0]["accountId"] + "\n"
    #strcat+="\nWins: " + response["lifeTimeStats"][8]["value"]  + "\n"
    #strcat+="\nWin %: " + response["lifeTimeStats"][9]["value"] + "\n"
    #strcat+="\nKills: " + response["lifeTimeStats"][10]["value"] + "\n"
    #strcat+="\nK/D: " + response["lifeTimeStats"][11]["value"] + "\n"
    #strcat+="\nMatches Played: " + response["lifeTimeStats"][7]["value"] + "\n"
    return render_template('index.html', stats = accountInfo, accountName = playerName) #statString is the string containing all the data
    #print()
    #print("Account ID: " + response["recentMatches"][0]["accountId"])
    #print("Wins: " + response["lifeTimeStats"][8]["value"])
    #print("Win %: " + response["lifeTimeStats"][9]["value"])
    #print("Kills: " + response["lifeTimeStats"][10]["value"])
    #print("K/D: " + response["lifeTimeStats"][11]["value"])
    #print("Matches Played: " + response["lifeTimeStats"][7]["value"])

if __name__ == '__main__':
    app.run(debug=True)

