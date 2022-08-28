def telegrambot():
    import telebot 
    from telebot import types
    TOKEN="5428904552:AAGZhvIbk0c3Bjnbke7Rmi7o-DEBDefk_9g"

    bot=telebot.TeleBot(TOKEN)

    #create keyboards
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1=types.KeyboardButton('Да')
    button2=types.KeyboardButton('Нет')
    #add buttons and keyboards
    keyboard.add(button1,button2)

    @bot.message_handler(commands=['hello','hi','привет','Hi','салам','start'])

    def start(message):  
      user=message.chat.first_name
      message2=bot.send_message(message.chat.id, f'Привет, {user} хотите посмотреть про машины или узнать другие новости?', reply_markup=keyboard)
    
      bot.register_next_step_handler(message2,check_answer)

    def check_answer(message):
      markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
      if message.text=='Да':
        item1 = types.KeyboardButton("🚘 Котегрии машин")   
        item2 = types.KeyboardButton("💰 Курсы валют")
        item3 = types.KeyboardButton("📲 Новости про игры")
        item4 = types.KeyboardButton("💻 Обучение")

        markup.add(item1,item2,item3,item4)
        bot.send_message(message.chat.id, f'Вы находитесть в главном меню',   reply_markup=markup)


      else:
        #if push button NotADirectoryError
        bot.send_message(message.chat.id, "Окей, до  встречи, заходите еще! ")

    @bot.message_handler(content_types=["text"])
    def bot_message(message):
      if message.text=='🚘 Котегрии машин':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton('🛻 Купе')
        item2=types.KeyboardButton('🚗 Седан')
        item3=types.KeyboardButton('🚙 Джип')
        item4=types.KeyboardButton('🚐 Минивэн')
        back=types.KeyboardButton('⬅️ Назад')
        markup.add(item1,item2,item3,item4,back)

        bot.send_message(message.chat.id, '🚘 Котегрии машин', reply_markup=markup)

      elif message.text=='💰 Курсы валют':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton('💵 Обменка')
        back=types.KeyboardButton('⬅️ Назад')
        markup.add(item1,back)

        bot.send_message(message.chat.id, '💰 Курсы валют', reply_markup=markup)

      elif message.text=='💵 Обменка':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, '[ВАлюта.кг](https://valuta.kg//)', parse_mode='Markdown')    
        back=types.KeyboardButton('⬅️ Назад')
        markup.add(back)

        bot.send_message(message.chat.id, '💵 Обменка', reply_markup=markup)

      elif message.text=='⬅️ Назад':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton('💵 Обменка')
        item1 = types.KeyboardButton("🚘 Котегрии машин")   
        item2 = types.KeyboardButton("💰 Курсы валют")
        item3 = types.KeyboardButton("📲 Новости про игры")
        item4 = types.KeyboardButton("💻 Обучение")

        markup.add(item1,item2,item3,item4)
        bot.send_message(message.chat.id, f'Вы находитесть в главном меню',   reply_markup=markup)

      elif message.text=='🛻 Купе':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, '[cars.kg](https://cars.kg//)', parse_mode='Markdown')    
        back=types.KeyboardButton('⬅️ Назад')
        markup.add(back)

        bot.send_message(message.chat.id, '🛻 Купе', reply_markup=markup)  

      elif message.text=='🚗 Седан':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, '[cars.kg](https://cars.kg//)', parse_mode='Markdown')    
        back=types.KeyboardButton('⬅️ Назад')
        markup.add(back)

        bot.send_message(message.chat.id, '🚗 Седан', reply_markup=markup)  
      elif message.text=='🚙 Джип':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, '[cars.kg](https://cars.kg//)', parse_mode='Markdown')    
        back=types.KeyboardButton('⬅️ Назад')
        markup.add(back)

        bot.send_message(message.chat.id, '🚙 Джип', reply_markup=markup)  

      elif message.text=='🚐 Минивэн':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, '[cars.kg](https://cars.kg//)', parse_mode='Markdown')    
        back=types.KeyboardButton('⬅️ Назад')
        markup.add(back)
        bot.send_message(message.chat.id, '🚐 Минивэн', reply_markup=markup) 
      elif message.text=='📲 Новости про игры':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, '[stopgame.ru](https://stopgame.ru/review//)', parse_mode='Markdown')    
        back=types.KeyboardButton('⬅️ Назад')
        markup.add(back)

        bot.send_message(message.chat.id, '📲 Новости про игры', reply_markup=markup)  
    
      elif message.text=='💻 Обучение':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, '[makers.kg](https://makers.kg//)', parse_mode='Markdown')    
        back=types.KeyboardButton('⬅️ Назад')
        markup.add(back)

        bot.send_message(message.chat.id, '💻 Обучение', reply_markup=markup)  

    bot.polling(none_stop=True)
