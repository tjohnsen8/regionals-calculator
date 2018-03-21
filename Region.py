import requests
import json

# what are the dynamic inputs
# division
# region - if division = men/women

# dependent properties
# needed_rank - dependent on division and region
# region_score
# number_workouts
# average_points_needed

class Region:
	def __init__(self, division):
		self.division = division
		self.region = 0
		self.needed_rank = 0
		self.total_score = 0
		self.number_workouts = 0
		self.average_points_needed = 0
		self.url =''

	def get_needed_rank(self):
		# depends on division first, if anything other than 1 or 2, its 200
		if self.division > 2:
			self.needed_rank = 200
			self.region = 0
		else:
			ranks = {
				25: 20,
				20: 10,
				21: 30,
				18: 15,
				5: 5,
				26: 15,
				6: 20,
				23: 20,
				22: 20,
				24: 20,
				9: 20,
				10: 20,
				11: 25,
				27: 25,
				14: 20,
				15: 20,
				17: 20,
				19: 35
			}
			self.needed_rank = ranks.get(self.region, 20)

	def build_url(self, wod_num):
		self.url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2018/leaderboards?division={}&region={}&scaled=0&sort={}&occupation=0&page=' \
			.format(self.division, self.region, wod_num)

	def get_total_score_needed(self):
		self.build_url(0)
		self.get_needed_rank()
		page = requests.get(self.url)
		try:
		    self.json_data = page.json()
		except:
		    print('json decode error')
		    return
		self.number_workouts = len(self.json_data['leaderboardRows'][0]['scores'])
		self.total_score = self.json_data['leaderboardRows'][self.needed_rank]['overallScore']

	def get_average_points_needed(self):
		self.average_points_needed = self.total_score / self.number_workouts

