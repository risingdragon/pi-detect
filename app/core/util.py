# -*- coding: utf-8 -*-
import os
import fcntl
import re
from datetime import datetime

class Util(object):
	@staticmethod
	def basedir():
		match = re.search('^(.+)/app/core', os.path.dirname(__file__))
		return match.group(1)

	@staticmethod
	def log(msg, logname = 'debug'):
		logdir = Util.basedir() + '/log'

		with open(logdir + '/' + logname + '.txt', 'a') as fp:
			fcntl.flock(fp.fileno(), fcntl.LOCK_EX)
			fp.write('[%s]%s\n' % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), msg))
			fcntl.flock(fp.fileno(), fcntl.LOCK_UN)
