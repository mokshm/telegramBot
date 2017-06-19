import re
import logging
welcome_msg = '''Hi, My name is ZeroSurfer and I am a bot. Moksh Makhija is my father. I am in alpha phase right now. Can you suggest me something that I'm able to do in the near future? I'm looking for suggestions :) Suggest me with a message starting with @suggest.''';
suggests_pass = "oneplus5";
welcome_msg = "Thank you. I will discuss this your idea with my father and will try to learn to learn it";
ttoken = "323805326:AAHrtIVyVgaXogy-t6U528r3eCs_G5uZq1w";
#base_url = "https://api.telegram.org/bot";
#####code starts here#####
from telegram.ext import Updater, MessageHandler, Filters
upd = Updater(token=ttoken);

disp = upd.dispatcher;
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO);

def general(bot,update,arg):
 if(arg[0] != '@suggest' or arg[0] != '@suggests'):
  bot.send_message(chat_id=upd.message.chat_id,text=welcome_msg);
 elif(arg[0] == '@suggest'):
  tele_log = open('suggest_logs.txt','a');
  stext = upd.message.text[9:];
  stext .= '\n';
  tele_log.write(stext);
  bot.send_message(chat_id=upd.message.chat_id,text=welcome_msg);
  tele_log.close();
 else:
  if(arg[1] == suggests_pass):
   tele_log = open('suggest_logs.txt','r');
   for line in tele_log:
    bot.send_message(chat_id=upd.message.chat_id,text=line);
   bot.send_message(chat_id=upd.message.chat_id,text="That's it Father.");
   tele_log.close();

######general function ends######
general_handler = MessageHandler(Filters.text,general);
disp.add_handler(general_handler);
upd.start_polling();
