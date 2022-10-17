# REFERENCES: https://www.jcchouinard.com/twitter-api/

import tweepy

def show_followers(username):

    # api_key = input("ENTER API KEY: ")
    api_key = 'DCJffcKxsoeuaLwulTaqG3EK2'

    # api_secrets = input("ENTER API SECRETS KEY: ")
    api_secrets = '7hzEtMYxloxQaLP7bs4vi0JvSBgxLFOr7e3ykzVVvCSUCMQg4G'

    # access_token = input("ENTER ACCESS TOKEN: ")
    access_token = '1519865372945571841-h6htwtFx2fgRIrsczdQH2qVMmLlDCd'

    # access_secret = input("ENTER ACCESS SECRET: ")
    access_secret = 'QaBYl0CNz2IipkFkfatybYd37DC1YpevQrEomvM0hMjI0'

    # Provide authentication to twitter
    auth = tweepy.OAuthHandler(api_key, api_secrets)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print('AUTHENTICATION WAS SUCCESSFUL')
    except:
        print('AUTHENTICATION FAILED')

    user = api.get_user(screen_name = username)

    # Print user statistics
    print(f"Number of Followers: {user.followers_count}")
    print(f"Number of Statuses: {user.statuses_count}")

    # Show all followers
    print("FOLLOWERS INFORMATION: ")
    for follower in user.followers():
        print('Name: ' + str(follower.name))
        print('Username: ' + str(follower.screen_name))

if __name__ == '__main__':
    print("ENTER USERNAME OF TWITTER USER TO SEARCH: ")
    twitterUser = input()
    show_followers(twitterUser)
