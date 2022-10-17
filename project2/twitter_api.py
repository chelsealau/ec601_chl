# REFERENCES: https://www.jcchouinard.com/twitter-api/

import tweepy

# Provide authentication credentials to Twitter and initialize tweepy
def authenticate():
    api_key = input("ENTER API KEY: ")
    api_secrets = input("ENTER API SECRETS KEY: ")
    access_token = input("ENTER ACCESS TOKEN: ")
    access_secret = input("ENTER ACCESS SECRET: ")

    # Provide authentication to twitter
    auth = tweepy.OAuthHandler(api_key, api_secrets)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print('AUTHENTICATION WAS SUCCESSFUL')
        return api
    except:
        print('AUTHENTICATION FAILED')

# Retrieve and print information about the followers of the specified user
def show_followers(username):
    api = authenticate()
    user = api.get_user(screen_name = username)

    # Print user statistics
    print(f"Number of Followers: {user.followers_count}")
    print(f"Number of Statuses: {user.statuses_count}")

    # Show all followers
    print("FOLLOWERS INFORMATION: ")
    for follower in user.followers():
        print('Name: ' + str(follower.name))
        print('Username: ' + str(follower.screen_name))

# Retrieve and show tweets from specified user
def get_tweets(username):
    api = authenticate()
    tweets = api.user_timeline(screen_name=username, count=200)
    tweets_extended = api.user_timeline(screen_name=username, tweet_mode='extended', count=200)
    print(tweets_extended)


if __name__ == '__main__':
    print("ENTER USERNAME OF TWITTER USER TO SEARCH: ")
    twitterUser = input()
    show_followers(twitterUser)
    get_tweets(twitterUser)


