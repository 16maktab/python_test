import telebot
bot = telebot.TeleBot('1428103015:AAESL5L9Ehsjn14VMfSq3jsPZjCd1VOwOF0')


@bot.message_handler(commands=['start'])
def start(message):
	name = str(message.from_user.first_name)
	bot.send_message(message.from_user.id ,'Assalomu alaykum ' + name)
	#bu yerda user /start bosganda Isminmi olib Salom qowb yuboradi
	#message bu json telegram server bizga xabarda json api yuboradi uni ichida userga tegishli #barcha narsa bor

@bot.message_handler(content_types=['text'])
def send(message):
	text = message.text
	if text == 'Salom':
		bot.send_message(message.from_user.id , 'Salom aka')
	elif text == 'Zo`rmisan':
		bot.send_message(message.from_user.id , 'Yaxshi, rahmat')
	elif text == 'Isming nima':
		bot.send_message(message.from_user.id , 'Men 16-maktab botiman')
	elif text == 'Xayr':
		bot.send_message(message.from_user.id , 'Sizga ham xayr')
	else:
		bot.send_message(message.from_user.id , 'Uzur men sizi tanimayaman 😑😂')

bot.polling(none_stop= True) # bu botimiz ochib qolmasligi uchun!