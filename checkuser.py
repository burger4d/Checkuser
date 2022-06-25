from urllib.request import urlopen

with open("data.txt", "r") as file:
    content = file.read()
    file.close()

data = {}
new_content = "'"+content.replace("\n", "','")+"'"
websites = eval("["+new_content+"]")
websites.sort()
#print(websites)
users = input("search user(s):").split()
for user in users:
    data[user] = []
    print()
    print("Note: V means 'found', and X means 'not found'")
    print()
    print(user+":")
    for website in websites:
        try:
            name = website[:website.find(".")]
            url = "https://"+website+"/"+user
            if name == "itch":
                url = "https://"+user+"."+website
                name = "itch.io"
            print("searching on "+name+"("+url+")", end=" ")
            #print("    "+url,end=" ")
            request = urlopen("https://"+website+"/"+user)
        except Exception as err:
            print("X")
        else:
            print("V")
            data[user].append(website)

record = input("record information?(y/n):")
if record == "y":
    for user in users:
        if data[user] == []:
            print("There is no information to record about "+user)
        else:
            with open(user+".txt", "w") as file:
                for website in data[user]:
                    file.write(website)
                file.close()
            print(user+".txt done")
