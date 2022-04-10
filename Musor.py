try:
    import telebot, time, threading, requests, os, psycopg2
    from telebot import types

    bot = telebot.TeleBot('5003628344:AAFfNzenU2CLVPOC_cNDIOKo9PoCCdafvwo')
    print('Работает!')

    con = psycopg2.connect(
      database="d6fntqlv4rnp6m", 
      user="rdlugbeaoencha", 
      password="fda1af30b1db2eebc984fd28518ad895843859137098117edd785fcef287494e", 
      host="ec2-52-30-67-143.eu-west-1.compute.amazonaws.com", 
      port="5432"
    )
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tab(
        id BIGINT,
        bal BIGINT,
        clava INT,
        naz TEXT,
        ban INT);''')
    con.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS qiwi(
        popo BIGINT);''')
    # INSERT INTO qiwi (popo) VALUES (0);''')
    con.commit() 


    c1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    c1_1 = types.KeyboardButton('VK 💙')
    c1_2 = types.KeyboardButton('Telegtam 💜')
    c1_3 = types.KeyboardButton('Instagram ❤')
    c1_4 = types.KeyboardButton('Баланс 💰')
    c1_5 = types.KeyboardButton('Пополнить 💳')
    c1_6 = types.KeyboardButton('Правила 📋')
    c1.add(c1_1, c1_2)
    c1.add(c1_3)
    c1.add(c1_4, c1_5)
    c1.add(c1_6)

    c2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    c2_1 = types.KeyboardButton('QIWI ИЛИ КАРТА')
    c2_2 = types.KeyboardButton('Оплата картой 💳')
    c2_3 = types.KeyboardButton('Назад ↩')
    c2.add(c2_1)
    # c2.add(c2_2)
    c2.add(c2_3)

    c3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    c3_1 = types.KeyboardButton('Назад ↩')
    c3.add(c3_1)

    c4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    c4_1 = types.KeyboardButton('Подписчики 👤')
    c4_2 = types.KeyboardButton('Лайки ❤')
    c4_3 = types.KeyboardButton('Репосты 💬')
    c4_4 = types.KeyboardButton('Просмотры 👀')
    c4_5 = types.KeyboardButton('Назад ↩')
    c4.add(c4_1, c4_2)
    c4.add(c4_3, c4_4)
    c4.add(c4_5)

    c5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    c5_1 = types.KeyboardButton('Подписчики 👤')
    c5_2 = types.KeyboardButton('Просмотры 👀')
    c5_3 = types.KeyboardButton('Назад ↩')
    c5.add(c5_1, c5_2)
    c5.add(c5_3)

    c6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    c6_1 = types.KeyboardButton('Подписчики 👤')
    c6_2 = types.KeyboardButton('Лайки ❤')
    c6_3 = types.KeyboardButton('Назад ↩')
    c6.add(c6_1)
    c6.add(c6_2)
    c6.add(c6_3)

    def extract_arg(arg):
        return aarg.split()[0]

    def extract_arg1(arg):
        return arg.split()[1]

    def extract_arg2(arg):
        return arg2.split()[2]


    def clava(send, zn):
        cur.execute(f"""UPDATE tab SET clava = {zn} WHERE id = {send}""")
        con.commit()

    def sms1(messs, smm, clava):
        bot.send_message(messs, smm, reply_markup=clava)
    def sms(messs, smm):
        bot.send_message(messs, smm)

    def obnova(send, cym, zn):
        cur.execute(f"SELECT bal FROM tab WHERE id = '{send}'")
        if zn == 1:
            opop = int(cur.fetchall()[0][0]) + int(cym)
        else:
            opop = int(cur.fetchall()[0][0]) - int(cym)
        # Обнова
        cur.execute(f"""UPDATE tab SET bal = {opop} WHERE id = {send}""")
        con.commit() 

    def nazvanie(send):
        cur.execute(f"SELECT naz FROM tab WHERE id = '{send}'")
        return str(cur.fetchall()[0][0])

    def nazvanie_obnova(send, zn):
        cur.execute(f"""UPDATE tab SET naz = '{zn}' WHERE id = {send}""")
        con.commit()

    def balance(send):
        cur.execute(f"SELECT bal FROM tab WHERE id = '{send}'")
        return cur.fetchall()[0][0]

    def payment_history_last(my_login, api_access_token, rows_num, next_TxnId, next_TxnDate):
        # сессия для рекуест
        s = requests.Session()
        # добавляем рекуесту headers
        s.headers['authorization'] = 'Bearer ' + api_access_token
        # параметры
        parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate}
        # через рекуест получаем платежы с параметрами - parameters
        h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params=parameters)
        # обязательно json все объекты в киви апи json
        return h.json()


    mylogin = '79283692011'
    api_access_token = '5fec7a63ea890c52a6124fcad3d5636d'


    def QiwiCheck(number, api):
        while True:
            time.sleep(20)
            try:
                lastPayments = payment_history_last(number, api, '1', '', '')
                num = lastPayments['data'][0]['account']
                sum = lastPayments['data'][0]['sum']['amount']
                comm = lastPayments['data'][0]['comment']
                type = lastPayments['data'][0]['type']
                txnId = lastPayments['data'][0]['txnId']
                txnId = str(txnId)

                cur.execute("SELECT * FROM qiwi")
                lastpay = cur.fetchall()[0][0]
                lastpay = str(lastpay)

                if lastpay == txnId:
                    pass
                else:
                    try:
                        cur.execute(f"SELECT bal FROM tab WHERE id = {int(comm[1:])}")
                        we = cur.fetchall()[0][0]
                        we = int(we)
                        sum = int(sum)
                        opop = we + sum
                        cur.execute(f"""UPDATE tab SET bal = {opop} WHERE id = {int(comm[1:])}""")
                        con.commit()
                        cur.execute(f"""UPDATE qiwi SET popo = {txnId} WHERE popo = {lastpay}""")
                        con.commit()
                        sms(int(comm[1:]), "На ваш баланс зачисленно " + str(sum) + " руб.\n\nУдачных игр!")
                    except:
                        pass
            except:
                pass

    Tqiwi = threading.Thread(target=QiwiCheck, args=(mylogin, api_access_token))
    Tqiwi.start()

    def ras(text, admin):
        # Рaссылка
        cur.execute("SELECT * FROM tab")
        succes = 0
        fail = 0
        for it in cur.fetchall():
            try:
                sms(str(it[0]), str(text))
                succes +=1
            except:
                fail +=1
        sms(admin, "Рассылку получило - " + str(succes) + " пользователей\nЗаблокировали бота - " + str(fail) + " пользователей")

    @bot.message_handler()
    def get_text_messages(message):
        admin = 5073415776
        messages = message.from_user.id
        mess = message.text.lower()
        try:
            cur.execute(f"SELECT * FROM tab WHERE id = '{messages}'")
            infa = cur.fetchall()[0]
            ban = infa[4]
            i = infa[2]
            n = 1
        except:
            lolo = cur.fetchall()
            if str(lolo) == '[]':
                cur.execute(f"""INSERT INTO tab (id, bal, clava, naz, ban) VALUES ({messages}, 0, 1, 'text', 1);""")
                con.commit()
                ban = 1
                i = 1
                n = 0
                sms1(messages, f'Привет, {message.from_user.first_name}! \nРады видеть тебя в нашей группе 😊', c1)
            else:
                pass
        if ban == 0:
            sms(sender, 'Ваш аккаунт заблокирован. ⛔')

        elif n == 0:
            pass

        elif mess[0:5] == 'назад' and i == 5 or mess[0:5] == 'назад' and i == 6 or mess[0:5] == 'назад' and i == 7 or mess[0:5] == 'назад' and i == 20:
            clava(messages, 3)
            bot.send_message(messages, "Выберите:", reply_markup=c4)

        elif mess[0:5] == 'назад' and i == 23 or mess[0:5] == 'назад' and i == 25:
            clava(messages, 22)
            bot.send_message(messages, 'Выберите:', reply_markup=c6)

        elif mess[0:9] == "instagram" or mess == 'инстаграм':
            clava(messages, 22)
            bot.send_message(messages, 'Выберите:', reply_markup=c6)

        elif mess[0:5] == 'назад' and i == 8:
            clava(messages, 5)
            bot.send_message(messages, 'Введите ссылку на группу или профиль: \nВ формате: https://vk.com/', reply_markup=c3)

        elif mess[0:10] == 'подписчики' and i == 22:
            clava(messages, 23)
            bot.send_message(messages, 'Введите ссылку: \nВ формате: https://instagram.com/', reply_markup=c3)
       
        elif mess[0:5] == 'лайки' and i == 22:
            clava(messages, 25)
            bot.send_message(messages, 'Введите ссылку: \nВ формате: https://instagram.com/p/', reply_markup=c3)

        elif mess[0:5] == 'назад' and i == 24:
            clava(messages, 23)
            bot.send_message(messages, 'Введите ссылку: \nВ формате: https://instagram.com/', reply_markup=c3)
        
        elif mess[0:5] == 'назад' and i == 26:
            clava(messages, 25)
            bot.send_message(messages, 'Введите ссылку: \nВ формате: https://instagram.com/p/', reply_markup=c3)

        elif mess[0:22] == 'https://instagram.com/' and i == 23 and len(mess) > 25 and mess[0:24] != 'https://instagram.com/p/' or mess[0:24] == 'https://instagram.com/p/' and len(mess) > 29 and i == 25:
            nazvanie_obnova(messages, str(mess))
            if i == 23:
                clava(messages, 24)
                bot.send_message(messages, 'Сколько подписчиков нужно? \n\n50 подписчиков = 5₽ \nМинимум 50 подписчиков')
            elif i == 25:
                clava(messages, 26)
                bot.send_message(messages, 'Сколько лайков нужно? \n\n100 лайков = 5₽ \nМинимум 20 лайков')


        elif i == 24:
            naz = nazvanie(messages)
            try:
                bal2 = balance(messages)
                bal2 = int(bal2)
                if int(mess) > 49:
                    df = int(float(mess) * float(0.1))
                    if bal2 >= int(df):
                        obnova(messages, int(df), 2)
                        a = requests.get('https://wiq.ru/api/', 
                            params={'key': '1356536ce1fe797f8e1ff1b092ef60fe', 'action': 'create', 'service': '177', 'quantity': int(mess), 'link': str(naz)})
                        a = str(a.json()['order'])
                        clava(messages, 1)
                        bot.send_message(messages, f"ID: {a} \nСтоимость заказа: {df}₽ \nНакрутка запущена ✅", reply_markup=c1)
                    else:
                        clava(messages, 2)
                        bot.send_message(messages, f'Стоимость заказа: {df}₽ \nУ вас недостаточно средств ⛔', reply_markup=c2)
                else:
                    bot.send_message(messages, 'Укажите число больше: 49 ⛔')
            except:
                bot.send_message(messages, 'Укажите число ⛔')

        elif i == 26:
            naz = nazvanie()
            try:
                bal2 = balance(messages)
                bal2 = int(bal2)
                if int(mess) > 19:
                    df = int(float(mess) * float(0.05))
                    if bal2 >= int(df):
                        obnova(messages, int(df), 2)
                        a = requests.get('https://wiq.ru/api/', 
                            params={'key': '1356536ce1fe797f8e1ff1b092ef60fe', 'action': 'create', 'service': '131', 'quantity': int(mess), 'link': str(naz)})
                        a = str(a.json()['order'])
                        clava(messages, 1)
                        bot.send_message(messages, f"ID: {a} \nСтоимость заказа: {df}₽ \nНакрутка запущена ✅", reply_markup=c1)
                    else:
                        clava(messages, 2)
                        bot.send_message(messages, f'Стоимость заказа: {df}₽ \nУ вас недостаточно средств ⛔', reply_markup=c2)
                else:
                    bot.send_message(messages, 'Укажите число больше: 19 ⛔')
            except:
                bot.send_message(messages, 'Укажите число ⛔')

        elif mess[0:5] == 'назад' and i == 9:
            clava(messages, 6)
            bot.send_message(messages, 'Введите ссылку на пост: \nВ формате: https://vk.com/', reply_markup=c3)
        
        elif mess[0:5] == 'назад' and i == 21:
            clava(messages, 20)
            bot.send_message(messages, 'Введите ссылку на пост: \nВ формате: https://vk.com/', reply_markup=c3)
        
        elif mess[0:5] == 'назад' and i == 10:
            clava(messages, 7)
            bot.send_message(messages, 'Введите ссылку на пост: \nВ формате: https://vk.com/', reply_markup=c3)
        
        elif mess[0:5] == 'назад' and i == 12 or  mess[0:5] == 'назад' and i == 15:
            clava(messages, 11)
            bot.send_message(messages, 'Выберите:', reply_markup=c5)
        
        elif mess[0:5] == 'назад' and i == 13:
            clava(messages, 12)
            bot.send_message(messages, 'Введите ссылку: \nВ формате: https://t.me/', reply_markup=c3)
        
        elif mess[0:5] == 'назад' and i == 16:
            clava(messages, 15)
            bot.send_message(messages, 'Введите ссылку: \nВ формате: https://t.me/', reply_markup=c3)

        elif mess[0:7] == 'правила':
            bot.send_message(messages, 'Используя наш сервис вы соглашаетесь со всеми перечисленными пунктами: \n\n1 - Пополнение. \n1.1 При пополнении деньги не подлежат возврату! Их можно потратить только на накрутку в нашем сервисе. '+
                '\n1.2 Если после оплаты деньги не пришли в течении 1 - минуты обратитесь в поддержку.\n1.3 Чтобы пополнить баланс через карту обратитесь в поддержку.'+
                ' \n\n2 - Выполнение заказа. \n2.1 В редких случаях ваш заказ может обрабатываться до 12-ти часов, обычно это происходит сразу после создания заказа. \nПравила могут измениться в любой момент! \n\nПоддержка: \n@nakrut_ca')

        elif mess[0:9] == 'просмотры' and i == 11:
            clava(messages, 15)
            bot.send_message(messages, 'Введите ссылку: \nВ формате: https://t.me/', reply_markup=c3)
        
        elif mess[0:10] == 'подписчики' and i == 11:
            clava(messages, 12)
            bot.send_message(messages, 'Введите ссылку: \nВ формате: https://t.me/', reply_markup=c3)
       
        elif mess[0:13] == 'https://t.me/' and len(mess) > 15 and i == 12 or mess[0:13] == 'https://t.me/' and len(mess) > 15 and i == 15:
            a = open(str(messages) + "naz.txt", "w")
            a.write(str(mess))
            a.close()
            if i == 12:
                clava(messages, 13)
                bot.send_message(messages, 'Сколько подписчиков нужно? \n\n50 подписчиков = 10₽ \nМинимум 50 подписчиков.')
            elif i == 15:
                clava(messages, 16)
                bot.send_message(messages, 'Сколько просмотров нужно? \n\n1000 просмотров = 10₽ \nМинимум 500 просмотров.')

        elif mess[0:9] == 'просмотры' and i == 3:
            clava(messages, 20)
            bot.send_message(messages, 'Введите ссылку: \nВ формате: https://vk.com/', reply_markup=c3)

        elif mess[0:10] == 'подписчики' and i == 3:
            clava(messages, 5)
            bot.send_message(messages, 'Введите ссылку на группу или профиль: \nВ формате: https://vk.com/', reply_markup=c3)
        
        elif mess[0:5] == 'лайки' and i == 3:
            clava(messages, 6)
            bot.send_message(messages, 'Введите ссылку на пост: \nВ формате: https://vk.com/', reply_markup=c3)
        
        elif mess[0:7] == 'репосты' and i == 3:
            clava(messages, 7)
            bot.send_message(messages, "Введите ссылку на пост: \nВ формате: https://vk.com/", reply_markup=c3)
        
        elif mess[0:8] == 'telegtam':
            clava(messages, 11)
            bot.send_message(messages, 'Выберите:', reply_markup=c5)
        elif mess[0:15] == 'https://vk.com/' and len(mess) > 19 and i == 5 and mess[0:19] != 'https://vk.com/wall' and mess[0:20] != 'https://vk.com/photo' or \
            mess[0:19] == 'https://vk.com/wall' and len(mess) > 19 and i == 6 or \
            mess[0:19] == 'https://vk.com/wall' and len(mess) > 19 and i == 7 or \
            mess[0:20] == 'https://vk.com/photo' and len(mess) > 19 and i == 6 or \
            mess[0:20] == 'https://vk.com/photo' and len(mess) > 19 and i == 7 or \
            mess[0:19] == 'https://vk.com/wall' and len(mess) > 19 and i == 20 or  \
            mess[0:20] == 'https://vk.com/photo' and len(mess) > 19 and i == 20:
            nazvanie_obnova(messages, str(mess))
            if i == 5:
                clava(messages, 8)
                bot.send_message(messages, 'Сколько подписчиков нужно? \n\n100 подписчиков = 25₽ \nМинимум 50 подписчиков')
            elif i == 6:
                clava(messages, 9)
                bot.send_message(messages, 'Сколько лайков нужно? \n\n100 лайков = 15₽ \nМинимум 20 лайков')
            elif i == 7:
                clava(messages, 10)
                bot.send_message(messages, 'Сколько репостов нужно? \n\n100 репостов = 25₽ \nМинимум 50 репостов')
            elif i == 20:
                clava(messages, 21)
                bot.send_message(messages, 'Сколько просмотров нужно? \n\n100 просмотров = 10₽ \nМинимум 50 просмотров')
       
        elif i == 21:
            naz = nazvanie(messages)
            try:
                bal2 = balance(messages)
                bal2 = int(bal2)
                if int(mess) > 49:
                    df = int(float(mess) * float(0.10))
                    if bal2 >= int(df):
                        obnova(messages, int(df), 2)
                        a = requests.get('https://wiq.ru/api/', 
                            params={'key': '1356536ce1fe797f8e1ff1b092ef60fe', 'action': 'create', 'service': '154', 'quantity': int(mess), 'link': str(naz)})
                        a = str(a.json()['order'])
                        
                        clava(messages, 1)
                        bot.send_message(messages, f"ID: {a}\nСтоимость заказа: {df}₽ \nНакрутка запущена ✅", reply_markup=c1)
                    else:
                        clava(messages, 2)
                        bot.send_message(messages, f'Стоимость заказа: {df}₽ \nУ вас недостаточно средств ⛔', reply_markup=c2)
                else:
                    bot.send_message(messages, 'Укажите число больше: 49 ⛔')
            except:
                bot.send_message(messages, 'Укажите число ⛔')
        
        elif i == 8:
            naz = nazvanie(messages)
            try:
                bal2 = balance(messages)
                bal2 = int(bal2)
                if int(mess) > 49:
                    df = int(float(mess) * float(0.25))
                    if bal2 >= int(df):
                        obnova(messages, int(df), 2)
                        a = requests.get('https://wiq.ru/api/', 
                            params={'key': '1356536ce1fe797f8e1ff1b092ef60fe', 'action': 'create', 'service': '350', 'quantity': int(mess), 'link': str(naz)})
                        a = str(a.json()['order'])
                    
                        clava(messages, 1)
                        bot.send_message(messages, f"ID: {a} \nСтоимость заказа: {df}₽ \nНакрутка запущена ✅", reply_markup=c1)
                    else:
                        clava(messages, 2)
                        bot.send_message(messages, f'Стоимость заказа: {df}₽ \nУ вас недостаточно средств ⛔', reply_markup=c2)
                else:
                    bot.send_message(messages, 'Укажите число больше: 49 ⛔')
            except:
                bot.send_message(messages, 'Укажите число ⛔')

        elif i == 16:
            naz = nazvanie(messages)
            try:
                bal2 = balance(messages)
                bal2 = int(bal2)
                if int(mess) > 499:
                    df = int(float(mess) * float(0.01))
                    if bal2 >= int(df):
                        obnova(messages, int(df), 2)
                        a = requests.get('https://wiq.ru/api/', 
                            params={'key': '1356536ce1fe797f8e1ff1b092ef60fe', 'action': 'create', 'service': '2191', 'quantity': int(mess), 'link': str(naz)})
                        a = str(a.json()['order'])
                        
                        clava(messages, 1)
                        bot.send_message(messages, f"ID: {a} \nСтоимость заказа: {df}₽ \nНакрутка запущена ✅", reply_markup=c1)
                    else:
                        clava(messages, 2)
                        bot.send_message(messages, f'Стоимость заказа: {df}₽ \nУ вас недостаточно средств ⛔', reply_markup=c2)
                else:
                    bot.send_message(messages, 'Укажите число больше: 499 ⛔')
            except:
                bot.send_message(messages, 'Укажите число ⛔')

        elif i == 13:
            naz = nazvanie(messages)
            try:
                bal2 = balance(messages)
                bal2 = int(bal2)
                if int(mess) > 49:
                    df = int(float(mess) * float(0.2))
                    if bal2 >= int(df):
                        obnova(messages, int(df), 2)
                        a = requests.get('https://wiq.ru/api/', 
                            params={'key': '1356536ce1fe797f8e1ff1b092ef60fe', 'action': 'create', 'service': '400', 'quantity': int(mess), 'link': str(naz)})
                        a = str(a.json()['order'])

                        
                        clava(messages, 1)
                        bot.send_message(messages, f"ID: {a} \nСтоимость заказа: {df}₽ \nНакрутка запущена ✅", reply_markup=c1)
                    else:
                        clava(messages, 2)
                        bot.send_message(messages, f'Стоимость заказа: {df}₽ \nУ вас недостаточно средств ⛔', reply_markup=c2)
                else:
                    bot.send_message(messages, 'Укажите число больше: 49 ⛔')
            except:
                bot.send_message(messages, 'Укажите число ⛔')


        elif i == 9:
            naz = nazvanie(messages)
            bal2 = balance(messages)
            bal2 = int(bal2)
            try:
                if int(mess) > 19:
                    df = int(float(mess) * float(0.15))
                    if bal2 >= int(df):
                        obnova(messages, int(df), 2)
                        a = requests.get('https://wiq.ru/api/', 
                            params={'key': '1356536ce1fe797f8e1ff1b092ef60fe', 'action': 'create', 'service': '351', 'quantity': int(mess), 'link': str(naz)})
                        a = str(a.json()['order'])
                        clava(messages, 1)
                        bot.send_message(messages, f"ID: {a} \nСтоимость заказа: {df}₽ \nНакрутка запущена ✅", reply_markup=c1)
                    else:
                        clava(messages, 2)
                        bot.send_message(messages, f'Стоимость заказа: {df}₽ \nУ вас недостаточно средств ⛔', reply_markup=c2)
                else:
                    bot.send_message(messages, 'Укажите число больше: 19 ⛔')

            except:
                bot.send_message(messages, 'Укажите число ⛔')

        elif i == 10:
            naz = nazvanie(messages)
            try:
                bal2 = balance(messages)
                bal2 = int(bal2)
                if int(mess) > 49:
                    df = int(float(mess) * float(0.25))
                    if bal2 >= int(df):
                        obnova(messages, int(df), 2)
                        a = requests.get('https://wiq.ru/api/', 
                            params={'key': '1356536ce1fe797f8e1ff1b092ef60fe', 'action': 'create', 'service': '352', 'quantity': int(mess), 'link': str(naz)})
                        a = str(a.json()['order'])

                        clava(messages, 1)
                        bot.send_message(messages, f"ID: {a} \nСтоимость заказа: {df}₽ \nНакрутка запущена ✅", reply_markup=c1)
                    else:
                        clava(messages, 2)
                        bot.send_message(messages, f'Стоимость заказа: {df}₽ \nУ вас недостаточно средств ⛔', reply_markup=c2)
                else:
                    bot.send_message(messages, 'Укажите число больше: 49 ⛔')
            except:
                bot.send_message(messages, 'Укажите число ⛔')
        
        elif mess[0:2] == 'id' or mess[0:4] == 'айди':
            bot.send_message(messages, f'Ваш ID: {messages}')
        
        elif mess[0:2] == "фф":
            if messages == admin:
                try:
                    id = extract_arg(mess)
                    bal = extract_arg2(mess)
                    obnova(id, int(bal), 1)
                    bot.send_message(messages, "Готово")
                    bot.send_message(str(id), "На ваш баланс зачислено " + str(bal) + " руб.")
                except:
                    bot.send_message(messages, "Вы не указали айди или сумму")

        elif mess[0:2] == 'vk':
            clava(messages, 3)
            bot.send_message(messages, 'Выбери:', reply_markup=c4)

        elif mess[0:6] == 'баланс':
            bal2 = balance(messages)
            bal2 = int(bal2)
            bot.send_message(messages, f'Твой баланс: {bal2} руб. 💰')

        elif mess[0:5] == 'назад' and i == 3 or mess[0:5] == 'назад' and i == 2 or mess[0:5] == 'назад' and i == 11 or mess[0:5] == 'назад' and i == 22:
            clava(messages, 1)
            bot.send_message(messages, 'Выберите:', reply_markup=c1)
        
        elif mess[0:9] == 'пополнить':
            clava(messages, 2)
            bot.send_message(messages, "Выберите способ оплаты:", reply_markup=c2)
        
        # elif mess[0:13] == 'оплата картой' and i == 2:
        #     bot.send_message(messages, 'Для оплаты картой обратитесь в поддержку: \n@nakrut_ca')
        
        elif mess[0:9] == 'поддержка' or mess == 'помощь':
            bot.send_message(messages, 'Поддержка: \n@nakrut_ca')
        
        elif mess[0:14] == "qiwi или карта" and i == 2:
            clava(messages, 2)
            bot.send_message(messages, 'Кошелек для платежа: +79283692011 \n Примечание к платежу: ' + "1" + str(
                messages) + f' ❗ \n\nТак же оплатить можно с помощью карты (выбирается на сайте). \n\nПосле оплаты на Ваш баланс будет зачислена сумма перевода. Об этом вас уведомят.\n\nhttps://qiwi.com/payment/form/99?&extra%5B%27comment%27%5D=1{messages}&extra%5B%27account%27%5D=79283692011&blocked%5B0%5D=comment&blocked%5B1%5D=account&blocked%5B2%5D=sum')
            
        elif mess[0:3] == 'бан':
            try:
                helovek = extract_arg(mess)
                cur.execute(f"""UPDATE tab SET ban = 0 WHERE id = {helovek}""")
                con.commit() 
                sms(helovek, 'Ваш аккаунт заблокирован. ⛔')
                sms(messages, 'Аккаунт заблокирован. 😇')
            except:
                sms(sender, 'Неверный ID. ⛔')

        elif mess[0:6] == 'разбан':
            try:
                helovek = extract_arg(mess)
                cur.execute(f"""UPDATE tab SET ban = 1 WHERE id = {helovek}""")
                con.commit() 
                sms(helovek, 'Ваш аккаунт разблокирован. 😇')
                sms(messages, 'Аккаунт разблокирован. 😇')
            except:
                sms(sender, 'Неверный ID. ⛔')

        elif mess[0:8] == "рассылка":
                if messages == admin:
                    m = message.text[9:]
                    t = threading.Thread(target=ras, args=(m, admin))
                    t.start()
                    sms(messages, 'Рассылка запущена.')
                else:
                    sms(messages, 'Вы не являетесь администратором 👤')

        elif mess[0:5] == '/menu':
            clava(messages, 1)
            bot.send_message(messages, 'Вы в главном меню', reply_markup=c1)

        else:
            if i == 5:
                bot.send_message(messages, 'Введите ссылку \nВ формате: https://vk.com/')
            elif i == 6 or i == 7 or i == 20:
                bot.send_message(messages, 'Введите ссылку \nВ формате: https://vk.com/wall \nИли: https://vk.com/photo')
            elif i == 12 or i == 15:
                bot.send_message(messages, 'Введите ссылку: \nВ формате: https://t.me/')
            elif i == 2:
                bot.send_message(messages, 'Выбери cпособ пополнения 💳')
            else:
                bot.send_message(messages, "Я тебя не понимаю. Напиши /menu.")

    bot.polling(none_stop=True, interval=0)
except:
    os.system('python Musor.py')
