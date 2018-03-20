import requests
import json


def get_score_for_workout(region_num, wod_num, place):
	if place > 50:
		page = 2
		place = place - 50
	else: 
		page = 1
	url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2018/leaderboards?division=1&region={}&scaled=0&sort={}&occupation=0&page={}' \
		.format(region_num, wod_num, page)
	page = requests.get(url)
	try:
		scores = page.json()
	except:
		print('decode error')
		exit()
	score = scores['leaderboardRows'][place]['scores'][wod_num -1]['scoreDisplay']
	return score


# get the region first page data
url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2018/leaderboards?division=1&region=15&scaled=0&sort=0&occupation=0&page=1'
page = requests.get(url)
try:
    region = page.json()
except:
    print('json decode error')
    exit()
region_score = region['leaderboardRows'][19]['overallScore']
print(region_score)
average_ponts = int(int(region_score) / 6)
print(average_ponts)

score = get_score_for_workout(15, 5, average_ponts)
print(score)
'''
# now go find the 51st place finisher in each
url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2018/leaderboards?division=1&region=15&scaled=0&sort=1&occupation=0&page=2'
page = requests.get(url)
try:
	point1 = page.json()
except:
	print('decode error')
	exit()
point1_score = point1['leaderboardRows'][average_ponts - 50]['scores'][0]['scoreDisplay']
print(point1_score)
'''