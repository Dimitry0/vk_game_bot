# -*- coding: utf-8 -*-
# https://severecloud.github.io/vk-keyboard/
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from random import randint, choice
from db import UsersInfo as user
import time

casino_items = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

def main():
    global mes_text
    vk_session = vk_api.VkApi(token='fc0a207dd2667e41f3c88d0b966b85a9333646496022e058166227eaf2c0d27f626a63b4250d42c86a823')

    longpoll = VkBotLongPoll(vk_session, '212404498')

    vk = vk_session.get_api()

    try:
        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                text = event.message.text
                user_id = event.message.from_id
                if event.message.peer_id < 2000000000:
                    if not user.is_reg(user_id):
                        if text.lower() == "начать":
                            user.insert(user_id)
                            vk.messages.send(user_id=user_id,
                                             random_id=get_random_id(),
                                             keyboard=open('keyboard_main1.json', 'r', encoding='UTF-8').read(),
                                             message="Вы зарегистирировались в чат-игре Кликер 👍🏻\nКликайте на кнопку 'Клик' и зарабатывайте деньги 💥\n\nДля просмотра топа игроков по кликам нажмите кнопку 'Топ игроков' 👥\n\nЕсли нужна помощь используйте команду 'помощь' 📣\n\nПриятной игры 😘")

                    else:
                        if text.lower() == "помощь" or text == "Помощь 📚":
                            vk.messages.send(user_id=user_id,
                                             random_id=get_random_id(),
                                             message="Чат-игра кликер - игра, суть которой заключается в наборе денег топа благодаря кликам на главную кнопку 💥\n\nЕсли у вас пропала клавиатура напишите любое сообщение, которое не похоже на команды 💡")

                        elif text.lower() == "заработать" or text == "Заработать":
                            vk.messages.send(user_id=user_id,
                                             random_id=get_random_id(),
                                             keyboard=open('keyboard_main.json', 'r', encoding='UTF-8').read(),
                                             message="Вы перешли на клаву для заработка")

        # клавиатура 1

                        elif text.lower() == "клик" or text == "Клик 💥":
                            point = randint(1, 3)
                            vk.messages.send(user_id=user_id,
                                            random_id=get_random_id(),
                                            message=f"Вы кликнули и получили +{point} {'копейка' if point == 1 else 'копейки'} топа 💥")
                            user.update_clicks(user_id, user.get_clicks(user_id) + point)

            # клавиатура 1_1

                        elif text.lower() == "азино 3 топора" or text == "Азино 3 топора":
                            vk.messages.send(user_id=user_id,
                                             random_id=get_random_id(),
                                             keyboard=open('casino_key.json', 'r', encoding='UTF-8').read(),
                                             message="казино клава отправлена "
                                                     "СТАВКА 10 копеек")

                        elif text.lower() == "2x--черное" or text == "2X--черное":
                            cas = choice(casino_items)
                            if cas == 0:
                                mes_text =f"Вы выиграли +20 копеек!✅\n"
                                mes_text += f"На вашем счету {user.get_clicks(user_id) + 20} копеек. 👍🏻\n"
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message=mes_text)
                                user.update_clicks(user_id, user.get_clicks(user_id) + 20)
                            else:
                                mes_text = f"Вы просрали -10 копеек!❌\n"
                                mes_text += f"На вашем счету {user.get_clicks(user_id) - 10} копеек. 👍🏻\n"
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message=mes_text)
                                user.update_clicks(user_id, user.get_clicks(user_id) - 10)

                        elif text.lower() == "2x--красное" or text == "2X--красное":
                            cas = choice(casino_items)
                            if cas == 1:
                                mes_text = f"Вы выиграли +20 копеек!✅\n"
                                mes_text += f"На вашем счету {user.get_clicks(user_id) + 20} копеек. 👍🏻\n"
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message=mes_text)
                                user.update_clicks(user_id, user.get_clicks(user_id) + 20)
                            else:
                                mes_text = f"Вы просрали -10 копеек!❌\n"
                                mes_text += f"На вашем счету {user.get_clicks(user_id) - 10} копеек. 👍🏻\n"
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message=mes_text)
                                user.update_clicks(user_id, user.get_clicks(user_id) - 10)

                        elif text.lower() == "10x--зеленое" or text == "10X--зеленое":
                            cas = choice(casino_items)
                            if cas == 2:
                                mes_text = f"Вы выиграли +100 копеек!✅\n"
                                mes_text += f"На вашем счету {user.get_clicks(user_id) + 100} копеек. 👍🏻\n"
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message=mes_text)
                                user.update_clicks(user_id, user.get_clicks(user_id) + 100)
                            else:
                                mes_text = f"Вы просрали -10 копеек!❌\n"
                                mes_text += f"На вашем счету {user.get_clicks(user_id) - 10} копеек. 👍🏻\n"
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message=mes_text)
                                user.update_clicks(user_id, user.get_clicks(user_id) - 10)

                        elif text.lower() == "baby back, hey!)" or text == "Baby back, hey!)":
                            vk.messages.send(user_id=user_id,
                                             random_id=get_random_id(),
                                             keyboard=open('keyboard_main.json', 'r', encoding='UTF-8').read(),
                                             message="Вы перешли на клаву для заработка")

                        elif text.lower() == "назад" or text == "Назад":
                            vk.messages.send(user_id=user_id,
                                             random_id=get_random_id(),
                                             keyboard=open('keyboard_main1.json', 'r', encoding='UTF-8').read(),
                                             message="Вы перешли на главную клаву")

                        elif text.lower() == "топ игроков" or text == "Топ игроков 👥":
                            if user.rows() <= 15:
                                mes_text = "Топ игроков по состоятельности 👥\n\n"
                                top = user.get_top(user.rows())

                                for i, value in enumerate(top):
                                    data = (vk.users.get(user_ids=(value[0])))[0]
                                    name = data["first_name"]
                                    family = data["last_name"]

                                    mes_text += f"- {name} {family} [{value[1]} копеек.] 👍🏻\n"

                                mes_text += "\nКликайте больше и возвышайтесь в топы 📣"
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message=mes_text)
                            else:
                                mes_text = "Топ-15 игроков по состоятельности 👥\n\n"
                                top = user.get_top(15)
                                for i, value in enumerate(top):
                                    data = (vk.users.get(user_ids=(value[0])))[0]
                                    name = data["first_name"]
                                    family = data["last_name"]
                                    mes_text += f"- {name} {family} [{value[1]} копеек.] 👍🏻\n"

                                mes_text += "\nКликайте больше и возвышайтесь в топы 📣"
                                vk.messages.send(user_id=user_id,
                                                 random_id=get_random_id(),
                                                 message=mes_text)
                        elif text.lower() == "профиль" or text == "Профиль":
                            data = (vk.users.get(user_ids=user_id))[0]
                            name = data["first_name"]
                            family = data["last_name"]
                            mes_text = f"Да ты бомба)\n"
                            mes_text += f" {name} {family}, на твоем счету {user.get_clicks(user_id)} копеек\n"
                            mes_text += '\nКстати пошел нахуй👍'
                            vk.messages.send(user_id=user_id,
                                             random_id=get_random_id(),
                                             message=mes_text)



                        else:
                            vk.messages.send(user_id=user_id,
                                             random_id=get_random_id(),
                                             keyboard=open('keyboard_main1.json', 'r', encoding='UTF-8').read(),

                                             message="Ты помоему перепутал@_@\n\n\nКлавиатура отправлена ✅")

    except TimeoutError:
        print("--------------- [ СЕТЕВАЯ ОШИБКА ] ---------------")
        print("Переподключение к серверам...")
        time.sleep(3)


if __name__ == '__main__':
    main()