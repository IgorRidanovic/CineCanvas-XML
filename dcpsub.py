#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Generate CineCanvas compliant DCP subtitle XML file elements.
# genuuid() returns UUID
# Instantiate with a minimum of UUID and title string
# genheader() returns header portion
# gensubtitle(tc, text) takes 2-item timecode list and n-item subtitle card text
# genendtags() returns closing tags
# CineCanvas spec:
# http://www.deluxecdn.com/dcinema/support/ti_subtitle_spec_v1_1.pdf
# Igor Ridanovic, www.hdhead.com

import uuid

class XMLsubgen(object):
	'''DCP XML subtitle generator'''

	def __init__(self, uuid, title, reel=1, lang='en', fn='Arial.ttf', fc='ffffffff', fs='42'):
		self.uuid   = uuid
		self.title  = title
		self.reel   = reel
		self.lang   = lang
		self.fname  = fn
		self.fcolor = fc
		self.fsize  = fs
		self.snumb  = 1
		self.eol    = '\n'
		self.vstep  = 8

	def genheader(self):
		'''Generate subtitle header'''
		head = ['<?xml version="1.0" encoding="UTF-8"?>',
				'<DCSubtitle Version="1.0">',
				'<SubtitleID>%s</SubtitleID>'%self.uuid,
				'<MovieTitle>%s</MovieTitle>'%self.title,
				'<ReelNumber>%s</ReelNumber>'%str(self.reel),
				'<Language>%s</Language>'%self.lang,
				'<LoadFont Id="Font1" URI="%s"/>'%self.fname,
				'<Font Id="Font1" Color="%s" Effect="shadow" '%self.fcolor+
				'EffectColor="ff000000" Italic="no" ' +
				'Script="normal" Size="%s" Underlined="no" '%self.fsize +
				'Weight="normal" AspectAdjust="1" Spacing="0em">' + self.eol
				]
		return self.eol.join(head)

	def gensubtitle(self, tc, text):
		'''Generate subtitle event. Timecode is a 2-item list. Text items are not limited'''
		# Insert SpotNumber and timecode values
		l1 = '<Subtitle SpotNumber="%s"'%str(self.snumb) + \
				' TimeIn="%s" TimeOut="%s"'%(tc[0],tc[1]) +\
				' FadeUpTime="000" FadeDownTime="000">' + self.eol
		self.snumb += 1

		# Closing tags
		l3 = '</Subtitle>' + self.eol

		# One subtitle row
		lt = len(text)
		if lt == 1:
			l2 = '<Text HPosition="0" VAlign="bottom" VPosition="6">%s</Text>%s'\
					%(text[0], self.eol)
		
		else:
			# Multiple subtitle rows
			mrow = []
			vpos = lt * self.vstep - 2

			# Insert Vposition, text, and eol for each row in a subtitle
			for t in text:
				mrow.append(
					'<Text HPosition="0" VAlign="bottom" VPosition="%s">%s</Text>%s'\
					%(str(vpos), t, self.eol)
					)
				# Decrease VPosition by preset amount for subsequent rows
				vpos -= self.vstep
			
			# Join multiple row list into a string
			l2 = ''.join(mrow)


		return l1 + l2 + l3


	def genendtags(self):
		return '</Font>' + self.eol + '</DCSubtitle>'

	@staticmethod
	def genuuid():
		return str(uuid.uuid4())
