# coding=utf-8

##################################
# Zappylib V0.3.0
# ZapiHelper
# (c) 2014 Pascal Nançoz
##################################
import json

class ZapiHelper:
	ZapiSession = None

	def __init__(self, zapiSession):
		self.ZapiSession = zapiSession

# -- Channels -- 
	def get_allChannels(self, flag_favorites=False):
		api = '/zapi/v2/cached/channels/' + self.ZapiSession.AccountData['account']['power_guide_hash'] + '?details=False'
		channelsData = self.ZapiSession.exec_zapiCall(api, None)
		if channelsData is None: 
			return None

		if flag_favorites:
			api = '/zapi/channels/favorites'
			favoritesData = self.ZapiSession.exec_zapiCall(api, None)
			if favoritesData is None:
				return None

		allChannels = []
		for group in channelsData['channel_groups']:
			for channel in group['channels']:
				allChannels.append({
					'id': channel['id'],
					'title': channel['title'],
					'image': channel['qualities'][0]['logo_black_42'],
					'recommend': 1 if channel['recommendations'] == True else 0,
					'favorite': 1 if flag_favorites and channel['id'] in favoritesData['favorites'] else 0})
		return allChannels

	def get_channels(self, category):
		allChannels = self.get_allChannels(True if category == 'favorites' else False)
		if allChannels is not None:
			if category == 'favorites':
				return [channel for channel in allChannels if channel['favorite'] == 1]
			elif category == 'recommended':
				return [channel for channel in allChannels if channel['recommend'] == 1]
			return allChannels
		return None

