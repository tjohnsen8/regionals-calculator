import requests
import json

# build maps


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

def get_rank_for_score(region_num, wod_num, target_score, overall_score):
	page = 1
	score_search = target_score.split(' ')[0]
	while True:
		url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2018/leaderboards?division=1&region={}&scaled=0&sort={}&occupation=0&page={}' \
			.format(region_num, wod_num, page)
		page = requests.get(url)
		try:
			scores = page.json()
		except:
			print('decode error')
			exit()
		# loop through all the scores for that wod and to find
		num_rows = len(scores['leaderboardRows'])
		for i in range (0, num_rows):
			score = scores['leaderboardRows'][i][wod_num]['scoreDisplay']
			score = score.split(' ')[0]
			if score <= score_search:
				return i
		#check the rank vs the overall_score
		if page*50 > overall_score:
			return -1; # error
		page = page + 1

# get the region first page data
url = 'https://games.crossfit.com/competitions/api/v1/competitions/open/2018/leaderboards?division=1&region=15&scaled=0&sort=0&occupation=0&page=1'
page = requests.get(url)
try:
    region = page.json()
except:
    print('json decode error')
    exit()

# what are the dynamic inputs
# division
# region - if division = men/women

# dependent properties
# needed_rank - dependent on division and region
# region_score
# number_workouts
# average_points_needed

needed_rank = 19
region_score = region['leaderboardRows'][needed_rank]['overallScore']
num_workouts = len(region['leaderboardRows'][0]['scores'])
print('score needed {} across {} workouts'.format(region_score, num_workouts))
average_ponts = int(int(region_score) / num_workouts)
print(average_ponts)

scores = []
# range 1 - 5
for i in range(1,6):
	scores.append(get_score_for_workout(15, i, average_ponts))
print(scores)

# now test getting a rank for a specific time
desired_1_score = '400 reps'
