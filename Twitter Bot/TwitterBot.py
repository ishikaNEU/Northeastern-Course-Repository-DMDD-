import tweepy  # Library required for Twitter API
import pandas as pd
import pip

package = 'tweepy'  # Just replace the package name with any package to install it.
pip.main(['install', package])

#Twitter keys details

consumer_key = "eYR5Ni67Nd12rgEb9H8LIapD8"
consumer_secret = "CPeb11EARYCvVW6AyidiX3WvxGRxa8Aq7bi4ihYdJs3Fv2DfBn"
Bearer_Token = "AAAAAAAAAAAAAAAAAAAAAL6XiQEAAAAACK8IPhfixHObQ4cTIXWHy0RuYHU%3DlFlmefdzhrX3wwnc63PcdZpmVoUNV2S6h7fg5vKrGhdWFwVPag"

access_key = "1583205059231240192-Vtu4zLpMvO8CJZhyB7aZ4VVYJvEn3d"
access_secret = "VRgRTWjPcGuvt7o9p5rCVR9EOM4ZPKu9Fj4g1OMpzE44z"


auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
outtweets = []  # initialize master list to hold our ready tweets

for tweet in tweepy.Cursor(api.search_tweets, q="#neucourserepo", count=100,  # The q variable holds the hashtag
                           lang="en").items():
    outtweets.append([tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.user.location])


tweetdf = pd.DataFrame(outtweets, columns=["ID", "Created_at", "Text", "Location"])
df = tweetdf.to_csv("tweet_csv.csv", sep='\t', encoding='utf-8')

#Setting up the MySql connection

import mysql.connector

neucourse = mysql.connector.connect(host='localhost', user='root', passwd='password', database='neu_course_repository')
mycursor = neucourse.cursor()

#test table (used for testing only, not a part of UML)

mycursor.execute("Truncate neu_course_repository.test_table1")
neucourse.commit()

for i,row in tweetdf.iterrows():
    sql = "INSERT INTO neu_course_repository.test_table1 values(%s,%s,%s,%s)"
    mycursor.execute(sql,tuple(row))
    neucourse.commit()

print("Record inserted in test table")


for tweet in tweepy.Cursor(api.search_tweets, q="#neucourserepo", count=100,  # The q variable holds the hashtag
                           lang="en").items():
    outtweets.append([tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.user.location])

#users_table: Has details about the followers of NEU Course Repo page

user = api.get_user(screen_name="NEU_CourseRepo")
users =[]
for follower in user.followers():
    users.append([follower.screen_name, follower.name, follower.profile_image_url, follower.description,
                  follower.followers_count, follower.following])

#storing results in dataframe

userdf = pd.DataFrame(users, columns=["Twitter_handle", "name", "profile_image", "description", "followers_count", "following_count"])
userdf

#Exporting the dataframe to MySql database using the connection established above

mycursor.execute("Truncate neu_course_repository.User")
neucourse.commit()

for i,row in userdf.iterrows():
    sql = "INSERT INTO neu_course_repository.User values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,tuple(row))
    neucourse.commit()

print("Record inserted in User Values table")

# Tweet Details Table

outweets_user = []
for tweet in tweepy.Cursor(api.search_tweets, q="#neucourserepo", count=100,  # The q variable holds the hashtag
                           lang="en").items():
    outweets_user.append(
        [tweet.id_str, tweet.author.screen_name, tweet.source_url, tweet.author.name, tweet.created_at, tweet.text])

#storing results in dataframe
tweet_user = pd.DataFrame(outweets_user,columns = ["tweet_id","twitter_handle","tweet_source_url","name","created_at","tweet"])


#Exporting the dataframe to MySql database using the connection established above

mycursor.execute("Truncate neu_course_repository.Tweet_Details")
neucourse.commit()

for i,row in tweet_user.iterrows():
    sql = "INSERT INTO neu_course_repository.Tweet_Details values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,tuple(row))
    neucourse.commit()

print("Record inserted in Tweet Details Table")

# tags table: Gets the relevant tags from user tweets

tags = []
tweet_tags = []
for tweet in tweepy.Cursor(api.search_tweets,
                           q="#neucourserepo",
                           lang="en").items():
    s = ""

    for i in (tweet.entities.get("hashtags")):
        s = s + " #" + i["text"]
    # print("xxxxxxx")
    if (len(s) == 0):
        tags.append([tweet.id_str])
    else:
        tags.append([tweet.id_str, s])

#storing results in dataframe
tweet_tags = pd.DataFrame(tags,columns = ["ID","Tags"])

#Exporting the dataframe to MySql database using the connection established above

mycursor.execute("Truncate neu_course_repository.Tweet_Tag")
neucourse.commit()

for i,row in tweet_tags.iterrows():
    sql = "INSERT INTO neu_course_repository.Tweet_Tag values(%s,%s)"
    mycursor.execute(sql,tuple(row))
    neucourse.commit()

print("Record inserted in tweet tag table")

# tweet mentions: stores tweet details in database

outweets_mentions = []
for tweet in tweepy.Cursor(api.search_tweets, q="#neucourserepo", count=100,  # The q variable holds the hashtag
                           lang="en").items():
    outweets_mentions.append([tweet.id_str, tweet.author.screen_name, tweet.author.name, tweet.in_reply_to_screen_name])

#storing results in dataframe
mentiondf = pd.DataFrame(outweets_mentions,columns = ["tweet_id","twitter_handler", "source_user", "target_user"])

#Exporting the dataframe to MySql database using the connection established above

mycursor.execute("Truncate neu_course_repository.Tweet_Mention")
neucourse.commit()

for i,row in mentiondf.iterrows():
    sql = "INSERT INTO neu_course_repository.Tweet_Mention values(%s,%s,%s,%s)"
    mycursor.execute(sql,tuple(row))
    neucourse.commit()

print("Record inserted in tweet mentions")