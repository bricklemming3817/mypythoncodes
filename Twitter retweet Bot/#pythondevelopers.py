import tweepy
import time


auth = tweepy.OAuthHandler('Y3vlxDYkrJSReOa8Ym5Kld5Ua',
                           'ppzc0tae08hF0l3hFAwimy7ck9Kbcmh07nlMDxV8uVY4Exz7ik')
auth.set_access_token('1287969426541645825-rsy8aEJ1ajACC66pMcnMBGgHPFnfYH',
                      '5s5QFiYQydSnMnYLIhbzP2NcLkEBR1DqZWDmo4vwnwmYz')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

search2 = '#pythondevelopers'
n_tweets = 500

while(True):
    for tweet in tweepy.Cursor(api.search, search2).items(n_tweets):
        try:
            tweet.retweet()
            print('#pythondeveloper Retweeted!')
            time.sleep(60)

        except tweepy.TweepError as e:
            print('reason =', e.reason)
            time.sleep(120)
        except StopIteration:
            break

