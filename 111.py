import requests
import datetime


class BotHandler:

    def __init__(self, token):
        self.token = token
        # self.token = '1362363600:AAEDBSXn2o83y2gMaVQgatUArL_M5bIp-TI'
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': timeout}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        # print("{}!{}!".format(timeout,offset))
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        # print("Get result{}".format(get_result))
        # print(len(get_result))

        if len(get_result) > 0:
            # print("Get result{}".format(get_result))
            last_update = get_result[-1]
            # print("Get result -1 {}".format(last_update))
        else:
            last_update = get_result[len(get_result)]

        return last_update


token = '1362363600:AAEDBSXn2o83y2gMaVQgatUArL_M5bIp-TI'
greet_bot = BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)
        # print(new_offset)
        # print(greet_bot.get_updates(new_offset))
        last_update = greet_bot.get_last_update()
        # print(last_update)
        last_update_id = last_update['update_id']
        # print(last_update_id)
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1
        # print(new_offset)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()