# -*- coding: utf-8 -*-

import ConfigParser

config = ConfigParser.ConfigParser();
config.read('environment.cfg');

def getNoxPath():
	return config.get('nox','path');

def getControllerPortByName(name):
	fullname = name + '_port';
	return config.get('nox', fullname);

def getRouteflowPath():
	return config.get('routeflow','path');
