#info bot created by negative
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import telebot
from telebot import types
import json
import os
import config
import random
import requests as req

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def welcome(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("Taylor Team \xE2\x9C\x8C", url="https://telegram.me/taylor_team")
    c = types.InlineKeyboardButton("Add group \xE2\x9C\x8C", url="https://telegram.me/ID_bot_robot?startgroup=test")
    markup.add(a, c)
    b = types.InlineKeyboardButton("Developer ID bot \xE2\x9C\x8C", url="https://telegram.me/negative_officiall")
    markup.add(b)
    nn = types.InlineKeyboardButton("Inline Mode", switch_inline_query='')
    markup.add(nn)
    ret_msg = bot.send_message(cid, "Hello I'm ID bot \n\n Send : \n  /id or /me or /info   \n\n\n get your id : \n /idme (just pv) \nsend Your feedback : /feedback [msg]\n\n\n list inline mod : \ntype @ID_bot_robot\n\nBot version 3", disable_notification=True, reply_markup=markup)
    assert ret_msg.message_id

@bot.message_handler(commands=['id', 'ids', 'info', 'me'])
def id(m):      # info menu
    cid = m.chat.id
    title = m.chat.title
    usr = m.chat.username
    f = m.chat.first_name
    l = m.chat.last_name
    t = m.chat.type
    d = m.date
    text = m.text
    p = m.pinned_message
    fromm = m.forward_from
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("\xF0\x9F\x98\x8A Taylor Team \xF0\x9F\x98\x8A", url="https://telegram.me/taylor_team"))
#info text
    bot.send_chat_action(cid, "typing")
    bot.reply_to(m, "*ID from* : ```{}``` \n\n *Chat name* : ```{}``` \n\n\n *Your Username* : ```{}``` \n\n *Your First Name* : ```{}```\n\n *Your Last Name* : ```{}```\n\n *Type From* : ```{}``` \n\n *Msg data* : ```{}```\n\n *Your Msg* : ```{}```\n\n* pind msg * : ```{}```\n\n *from* : ```{}```".format(cid,title,usr,f,l,t,d,text,p,fromm), parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(commands=['contact'])
def c(m):
    uid = m.chat.id
    bot.send_chat_action(uid, 'typing')
    bot.send_contact(uid, phone_number="+98 937 909 7344", first_name="Negative")


@bot.message_handler(commands=['about']) # copy right Taylor Team
def p(m):
    uid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    v = types.InlineKeyboardButton('\xF0\x9F\x91\x87 \xF0\x9F\x91\xA5 Thanks to \xF0\x9F\x91\xA5 \xF0\x9F\x91\x87', callback_data='Team')
    a = types.InlineKeyboardButton('Negative', url='https://telegram.me/negative_officiall')
    b = types.InlineKeyboardButton('Parham', url='https://telegram.me/UnFriendlly')
    c = types.InlineKeyboardButton('Arsalan', url='https://telegram.me/mute_all')
    n = types.InlineKeyboardButton('Amircc_CreeD', url='https://telegram.me/Amircc_CreeD')
    m = types.InlineKeyboardButton('sorblack', url='https://telegram.me/sorblack')
    k = types.InlineKeyboardButton('MrJacki', url='https://telegram.me/MrJacki')
    j = types.InlineKeyboardButton('allwen', url='https://telegram.me/allwen')
    o = types.InlineKeyboardButton('Randall', url='https://telegram.me/Xx_Randall_Xx')
    p = types.InlineKeyboardButton('NeonGame', url='https://telegram.me/pokr_face')
    y = types.InlineKeyboardButton('\xF0\x9F\x92\x8E End \xF0\x9F\x92\x8E', callback_data='Team')
    ch = types.InlineKeyboardButton('Channel', url='https://telegram.me/idbot_channel')
    git = types.InlineKeyboardButton('Github', url='https://github.com/taylor-team')
    markup.add(v)
    markup.add(a, j)
    markup.add(b, c)
    markup.add(n, m)
    markup.add(k, o, p)
    markup.add(y)
    markup.add(ch, git)
    bot.send_chat_action(uid, 'typing')
    bot.send_message(uid, "Taylor Team development Telegram bot and web mastering \n\n developers : \n [negative](https://telegram.me/negative_officiall) \n [Parham](https://telegram.me/UnFriendlly)", parse_mode="Markdown")
    bot.send_photo(uid, open('taylor.jpg'), caption="@Taylor_Team", reply_markup=markup)

@bot.message_handler(commands=['idbot'])
def handler(m):
    cid = m.chat.id
    bot.send_message(cid, "My Name is ID bot \n creator and developer : [negative](https://telegram.me/negative_officiall) \n development channel : [Taylor Team](https://telegram.me/taylor_team)\n\n [github](https://github.com/taylor-team/id-bot)", parse_mode="Markdown")
    bot.send_chat_action(cid, "upload_photo")
    bot.send_photo(cid, open('slackbot-story1-582x436.jpg'), caption="@ID_bot_robot  \xF0\x9F\x98\x9C")

@bot.message_handler(commands=['idme'])
def test_handler(m):
    cid = m.from_user.id
    fl = m.from_user.first_name
    bot.send_message(cid, "*{}*  Your ID = ```{}```".format(fl,cid), parse_mode="Markdown")


@bot.message_handler(commands=['feedback'])
def feedback(m):
    senderid = m.chat.id
    first = m.from_user.first_name
    usr = m.from_user.username
    str = m.text
    txt = str.replace('/feedback', '')
    bot.send_message(senderid, "_Thank Your Msg Posted admin_", parse_mode="Markdown")
    bot.send_message(config.is_sudo, "msg : {}\nid : {}\nname : {}\nUsername : @{}".format(txt,senderid,first,usr))


@bot.message_handler(commands=['j'])
def j(m):
    sudo = config
    tmt = m.from_user.id
    idA, cid = m.chat.id, m.chat.id
    if str(tmt) not in config.is_sudo:
        bot.send_message(cid, "Just for admin", parse_mode="Markdown")
        return
    to_id = m.text.split()[1]
    txt = m.text.split()[2:]
    text = ' '.join(txt)
    bot.send_message(to_id, "<b>\xD8\xAF\xD8\xB1\x20\xD8\xAC\xD9\x88\xD8\xA7\xD8\xA8\x20\xD8\xB4\xD9\x85\xD8\xA7 :</b>\n <code>{}</code>".format(text), parse_mode="HTML")


@bot.inline_handler(lambda query: len(query.query) is 0)
def query_text(query):
    user = query.from_user.username
    name = query.from_user.first_name
    lname = query.from_user.last_name
    uid = query.from_user.id
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('\xE2\x9C\x85 {} \xE2\x9C\x85'.format(user), url="https://telegram.me/{}".format(user)))
    thumb_url = 'http://millingtonlibrary.info/wp-content/uploads/2015/02/Info-I-Logo.png'
    info = types.InlineQueryResultArticle('1',
                                          '\xF0\x9F\x8C\x8E Your Info \xF0\x9F\x8C\x8E',
                                          types.InputTextMessageContent('*Username : @{}\nYour First Name : {}\nYour Last Name : {}\nYour ID :  {}*'.format(user,name,lname,uid), parse_mode="Markdown"),
                                          reply_markup=markup,
                                          thumb_url=thumb_url)
    #pic = types.InlineQueryResultPhoto('2',
                                       #'http://vip.opload.ir/vipdl/95/3/negative23/photo-2016-06-09-01-09-41.jpg',
                                       #'http://vip.opload.ir/vipdl/95/3/negative23/photo-2016-06-09-01-09-41.jpg',
                                       #input_message_content=types.InputTextMessageContent('@Taylor_Team')
    #gif = types.InlineQueryResultGif('2',
                                    # 'http://andrewtrimmer.com/wp-content/uploads/2014/09/Coming-Soon_Light-Bulbs_Cropped-Animation-Set_03c.gif',
                                     #'http://andrewtrimmer.com/wp-content/uploads/2014/09/Coming-Soon_Light-Bulbs_Cropped-Animation-Set_03c.gif',
                                     #gif_width=70,
                                     #gif_height=40,
                                     #title="Soon Update",
                                    # input_message_content=types.InputTextMessageContent('New Update #Soon'))

    tumsss = 'http://images.clipartpanda.com/contact-clipart-contact-phone-md.png'
    random_text = random.randint(1, 100)
    tmpp = 'http://sugartin.info/wp-content/uploads/2013/11/logo.png'
    randowm = types.InlineQueryResultArticle('2', '\xD8\xB9\xD8\xAF\xD8\xAF\x20\xD8\xB4\xD8\xA7\xD9\x86\xD8\xB3\xDB\x8C\x20\xF0\x9F\x99\x88',
                                             types.InputTextMessageContent('\xD8\xB9\xD8\xAF\xD8\xAF\x20\xD8\xB4\xD8\xA7\xD9\x86\xD8\xB3\xDB\x8C : {}'.format(random_text)), thumb_url=tmpp)

    url = req.get('http://api.gpmod.ir/time/')
    data = url.json()
    EN = data['ENtime']
    time_tmp = 'http://prek-8.com//images/time21.jpg'
    timesend = types.InlineQueryResultArticle('3', 'Time / \xD8\xB3\xD8\xA7\xD8\xB9\xD8\xAA', types.InputTextMessageContent('`Tehran` : *{}*'.format(EN), parse_mode='Markdown'), thumb_url=time_tmp)
    bot.answer_inline_query(query.id, [info, randowm, timesend], cache_time=5, switch_pm_text='Start bot')

@bot.message_handler(commands=['uptime'])
def ss(m):
    cc = os.popen("uptime").read()
    bot.send_message(m.chat.id, '{}'.format(cc))

@bot.message_handler(commands=['leave'])
def leavehandler(m):
    if m.from_user.id == config.is_sudo:
        bot.leave_chat(m.chat.id)

@bot.message_handler(commands=['whois'])
def whois(m):
    text = m.text
    repll = text.replace('/whois', '')
    whois = os.popen('whois {}'.format(repll)).read()
    bot.send_message(m.chat.id, '{}'.format(whois))

bot.polling(True)
#end
# _____           _              _____
#|_   _|_ _ _   _| | ___  _ __  |_   _|__  __ _ _ __ ___
#  | |/ _` | | | | |/ _ \| '__|   | |/ _ \/ _` | '_ ` _ \
#  | | (_| | |_| | | (_) | |      | |  __/ (_| | | | | | |
#  |_|\__,_|\__, |_|\___/|_|      |_|\___|\__,_|_| |_| |_|
#           |___/
#Copy right  2016 Negative - Taylor Team
#MIT license
