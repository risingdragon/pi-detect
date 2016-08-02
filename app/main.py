#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import time
import shutil
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from core.util import Util
from core.config import Config

now = datetime.now().strftime('%s')
pictureDir = Util.basedir() + '/' + Config.get('picture-dir')

detectedPicrure = pictureDir + '/lastsnap.jpg'

lastmodified = 0
for i in range(0, 15):
	if os.path.exists(detectedPicrure):
		stat = os.stat(detectedPicrure)
		if int(stat.st_mtime) >= int(now):
			lastmodified = stat.st_mtime
			break
	time.sleep(1)

if lastmodified == 0:
	Util.log('file not found')
	sys.exit()

savedPicture = pictureDir + '/' + now + '.jpg'
shutil.copy(detectedPicrure, savedPicture)

if Config.get('mail-to') == None or Config.get('mail-to') == '':
	Util.log('no email')
	sys.exit()

message = MIMEMultipart()
message['Subject'] = 'motion detected!'
message['From'] = Config.get('mail-from')
message['To'] = Config.get('mail-to')
message.attach(MIMEText('motion detected!'))

file = open(savedPicture, 'rb')
attachment = MIMEImage(file.read(), 'jpeg', filename=os.path.basename(savedPicture))
attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(savedPicture))
message.attach(attachment)

smtp = smtplib.SMTP(Config.get('smtp-host'), Config.get('smtp-port'))
smtp.sendmail(Config.get('mail-from'), Config.get('mail-to'), message.as_string())
smtp.quit()
