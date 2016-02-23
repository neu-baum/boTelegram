# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
import botelegram

class Test_Botelegram(unittest.TestCase):

	def test_assertTrue(self):
		bot = botelegram.TBot()
		bot.set_token("api_token")
		ret = bot.sendAudio(114093395,'/home/ray/Desktop/audio.mp3')
		self.assertTrue(ret.ok)

if __name__ == '__main__':
	unittest.main()
