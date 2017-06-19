import re
import logging
welcome_msg = '''Hi, My name is ZeroSurfer and I am a bot. Moksh Makhija is my father. I am in alpha phase right now. Can you suggest me something that I'm able to do in the near future? I'm looking for suggestions :) Suggest me with a message starting with @suggest.''';
suggests_pass = "oneplus5";
suggest_msg = "Thank you. I will discuss your idea with my father and will try to learn it";
ttoken = "323805326:AAHrtIVyVgaXogy-t6U528r3eCs_G5uZq1w";
#base_url = "https://api.telegram.org/bot";
#####code starts here#####
from telegram.ext import Updater, MessageHandler, Filters
upd = Updater(token=ttoken);

disp = upd.dispatcher;
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO);

def general(bot,update):
 arg = update.message.text.split(' ');
 #print(str(arg))
 if(arg[0] != '@suggest' and arg[0] != '@suggests'):
  bot.send_message(chat_id=update.message.chat_id,text=welcome_msg);
 elif(arg[0] == '@suggest'):
  tele_log = open('suggest_logs.txt','a');
  stext = update.message.text[9:];
  tele_log.write(stext);
  tele_log.write('\n')
  bot.send_message(chat_id=update.message.chat_id,text=suggest_msg);
  tele_log.close();
 else:
  if(len(arg) == 2 and arg[1] == suggests_pass):
   tele_log = open('suggest_logs.txt','r');
   for line in tele_log:
    bot.send_message(chat_id=update.message.chat_id,text=line);
   bot.send_message(chat_id=update.message.chat_id,text="That's it Father.");
   tele_log.close();
  else:
   bot.send_message(chat_id=update.message.chat_id,text=welcome_msg);


######general function ends######
general_handler = MessageHandler(Filters.text,general);
disp.add_handler(general_handler);
upd.start_polling();
