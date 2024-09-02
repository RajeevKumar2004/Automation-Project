from speed_bot import InternetSpeedTwitterBot

call = InternetSpeedTwitterBot()
speed = call.get_internet_speed()
tweet = call.tweet_at_provider(speed)
