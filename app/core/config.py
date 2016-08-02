# -*- coding: utf-8 -*-
import json
from core.util import Util

class Config(object):
	_config = None

	@staticmethod
	def get(name):
		if Config._config is None:
			try:
				with open(Util.basedir() + '/config.json', 'r') as fp:
					Config._config = json.load(fp)
			except:
				Util.log('json error on config.json')
				return None

		if name in Config._config:
			return Config._config[name]
		else:
			return None
