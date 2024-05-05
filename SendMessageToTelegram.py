import requests
import json


def loadConfigFile(filename='config.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    return (data['apiToken'], data['chatID'])

def sendToTelegram(message):
    apiToken, chatID = loadConfigFile()
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    sendToTelegram("Hello from Python!")