"program to display basic details"

def personal_details():
    name = "Anjali"
    email = "anjalinegi0602@gmail.com"
    slack = "@genesis"
    Biostack = "genomics"
    twitter_handle = "@genesisanjie
    
    def hammingDist(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
 
str1 = slack
str2 = twitter_handle


print("Name: {}email: {}\tSlack: {}\tBiostack: {}\t Twitter:".format(name, email, slack, Biostack, twitter_handle))

personal_details()
