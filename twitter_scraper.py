import csv
import tweepy
import ssl
import json
import re
import colorama
import datetime

#Colorama Windows
colorama.init(strip=False)

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Date - Year/Mon/Day
startDate = datetime.datetime(2022, 4, 1, 0, 0, 0)
endDate =   datetime.datetime(2023, 12, 1, 0, 0, 0)


#Call of Duty
def CODMW():
    search = api.user_timeline(screen_name = 'infinityward', count = 60, include_rts = True,) 

    status=search[0]

    F_NAME = 'CODMW_status.json'
    with open(F_NAME,'w') as f_out:
        for status in search:
            if status.created_at < endDate and status.created_at > startDate:
                json.dump(status._json, f_out)
                f_out.write('\n')




#Keyword - Season
    with open('CODMW_status.json','r') as f:
        for line in f:
            for word in line.split():
                if "Season" in line.split():

                    regex_resources = re.compile(r'\d{19}')
                    resources = regex_resources.findall(line)
                    listToStr = ' '.join(map(str, resources))
                    tweetidnum = (listToStr[0:19])
                    tweet = api.get_status(tweetidnum)



                    #Account Name
                    tweetaccname = (tweet.user.screen_name)
                    print(("\n") , (colorama.Fore.YELLOW + tweetaccname + colorama.Fore.RESET),("\n"))

                    #Tweet Creation Date
                    tweetcreated = (tweet.created_at)
                    print((colorama.Fore.YELLOW + "Tweet Created: " + colorama.Fore.RESET),(colorama.Fore.YELLOW + str(tweetcreated) + colorama.Fore.RESET))

                    #Tweet ID
                    tweet = api.get_status(tweetidnum)
                    print((colorama.Fore.YELLOW + "Twitter ID: " + colorama.Fore.RESET),(colorama.Fore.YELLOW + str(tweetidnum) + colorama.Fore.RESET), "\n")



                    #Tweet Text
                    tweetcont = (tweet.text)
                    print(colorama.Fore.GREEN + tweetcont + colorama.Fore.RESET)

                    print()
                    linebrk = ("_________________________________________________________________________________________________")
                    print(colorama.Fore.YELLOW + linebrk + colorama.Fore.RESET)


                    break
                
                else:
                    None

#Keyword - update
    with open('CODMW_status.json','r') as f:
        for line in f:
            for word in line.split():
                if "update" in line.split():

                    regex_resources = re.compile(r'\d{19}')
                    resources = regex_resources.findall(line)
                    listToStr = ' '.join(map(str, resources))
                    tweetidnum = (listToStr[0:19])
                    tweet = api.get_status(tweetidnum)



                    #Account Name
                    tweetaccname = (tweet.user.screen_name)
                    print(("\n") , (colorama.Fore.YELLOW + tweetaccname + colorama.Fore.RESET),("\n"))

                    #Tweet Creation Date
                    tweetcreated = (tweet.created_at)
                    print((colorama.Fore.YELLOW + "Tweet Created: " + colorama.Fore.RESET),(colorama.Fore.YELLOW + str(tweetcreated) + colorama.Fore.RESET))

                    #Tweet ID
                    tweet = api.get_status(tweetidnum)
                    print((colorama.Fore.YELLOW + "Twitter ID: " + colorama.Fore.RESET),(colorama.Fore.YELLOW + str(tweetidnum) + colorama.Fore.RESET), "\n")



                    #Tweet Text
                    tweetcont = (tweet.text)
                    print(colorama.Fore.GREEN + tweetcont + colorama.Fore.RESET)

                    print()
                    linebrk = ("_________________________________________________________________________________________________")
                    print(colorama.Fore.YELLOW + linebrk + colorama.Fore.RESET)


                    break
                
                else:
                    None





def FORTNITE():
    search = api.user_timeline(screen_name = 'FortniteStatus', count = 60, include_rts = True,) 

    status=search[0]

    F_NAME = 'Fortnite_status.json'
    with open(F_NAME,'w') as f_out:
        for status in search:
            if status.created_at < endDate and status.created_at > startDate:
                json.dump(status._json, f_out)
                f_out.write('\n')





#Keyword - issue
    with open('Fortnite_status.json','r') as f:
        for line in f:
            for word in line.split():
                if "issue" in line.split():

                    regex_resources = re.compile(r'\d{19}')
                    resources = regex_resources.findall(line)
                    listToStr = ' '.join(map(str, resources))
                    tweetidnum = (listToStr[0:19])
                    tweet = api.get_status(tweetidnum)



                    #Account Name
                    tweetaccname = (tweet.user.screen_name)
                    print(("\n") , (colorama.Fore.YELLOW + tweetaccname + colorama.Fore.RESET),("\n"))

                    #Tweet Creation Date
                    tweetcreated = (tweet.created_at)
                    print((colorama.Fore.YELLOW + "Tweet Created: " + colorama.Fore.RESET),(colorama.Fore.YELLOW + str(tweetcreated) + colorama.Fore.RESET))

                    #Tweet ID
                    tweet = api.get_status(tweetidnum)
                    print((colorama.Fore.YELLOW + "Twitter ID: " + colorama.Fore.RESET),(colorama.Fore.YELLOW + str(tweetidnum) + colorama.Fore.RESET), "\n")



                    #Tweet Text
                    tweetcont = (tweet.text)
                    print(colorama.Fore.GREEN + tweetcont + colorama.Fore.RESET)

                    print()
                    linebrk = ("_________________________________________________________________________________________________")
                    print(colorama.Fore.YELLOW + linebrk + colorama.Fore.RESET)


                    break
                
                else:
                    None





CODMW()
FORTNITE()
