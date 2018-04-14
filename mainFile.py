import tweepy,time

consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth , wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

keywords =['retweet to win', 'enter to win', 'Retweet for a chance to win', 'retweet for a chance', 'Retweet to win', 'Retweet To Win']
search_words = ['retweet to win', 'enter to win']
follow_keyword = ['FOLLOW', 'follow', '#follow', 'Follow', '#Folllow', 'following', '#following','Following', '#Following']
like_keyword = ['like', 'LIKE','Like','#Like','#like']

def follow_count():
    user = api.get_user('') # enter you userid
    while user.friends_count == 2000:
        friendship = api.friends_ids('avan472')[0:2000]
        for oldest_friend in range(len(friendship), 1500, -1):
            print(oldest_friend)
            api.destroy_friendship(id=friendship[oldest_friend - 1])

#retweet message, # like and # follow
def retweet_message(tweet):
    for words in keywords:
        if words in tweet.text:
            try:
                api.retweet(id = tweet.id_str)
                print('retweet')
                time.sleep(2) # pervent too many retweet
                likes(tweet)
                retweet_follow(tweet)
            except tweepy.TweepError as e:
                pass
        else:
            continue

#check if the word follow is in text
def retweet_follow(tweet):
    for follow in follow_keyword:
        if follow in tweet.text:
             try:
                #user_ids =tweet.retweeted_status.user.id
                user_ids = tweet.author._json['screen_name']
                print(user_ids)
                api.create_friendship(screen_name = user_ids)
                print("followed")
             except Exception as e:
                 print(e)
        else:
            continue

#check to see if the word like is in text
def likes(tweet):
    for like in like_keyword:
        if like in tweet.text:
            try:
                user_ids = tweet.id
                api.create_favorite(user_id = user_ids)
                print('like')
            except Exception as e:
                pass

def search_twitter():
    for phrase in search_words:
        tweet_cursor = tweepy.Cursor(api.search, phrase, result_type="recent", include_entities=True, lang="en").items()
        for tweet in tweet_cursor:
            if not tweet.retweeted:
                retweet_message(tweet)
            else:
                continue


follow_count() #make sure # of follow doesn't exceed 2000, if it does, unfollow to 1500 starting from oldest
search_twitter() #search, tweet, follow, and like




















