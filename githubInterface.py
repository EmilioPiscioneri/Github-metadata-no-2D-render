import requests
from pathlib import Path
currentDirectory = Path("X:\python-programming\Github metadata no 2D render")
import json
configFilePath = currentDirectory / "config.json.gitignore" #config file path whicgh is ignore by github
configFileObject = open(Path(configFilePath),"r") # open the config file
rawConfigText = configFileObject.read()
configFileJSON = json.loads(rawConfigText) # get clonfig file as json
apikey = configFileJSON["api_key"]
configFileObject.close()

apiurl = "https://api.github.com"
def githubGetRequest(url):
     headers = {
            "accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Authorization": apikey
        }
     return  requests.get(url,headers)

class githubReceiver():
    # returns organisation photo if success as str else None Datatype
    def getOrganisationPhoto(self,organisationName):
       
        url = apiurl + "/orgs/"+organisationName
        
        response = githubGetRequest(url)
    
        if(not response.ok):
            return None # Error 
        
        responseJSON = response.json()
        # print(responseJSON) # Debugging
        return responseJSON["avatar_url"]

    # pass in name of author and repository as string and returns string withh data if success, if error returns None dataType
    def getAbout(self,author,repository):
        
        url = apiurl + "/repos/"+author+"/"+repository

        response = githubGetRequest(url)

        if(not response.ok):
            return None # Error 
        
        responseJSON = response.json()
        # print(responseJSON) # Debugging
        return responseJSON["description"]
    
    # Gets user input for repo details and calls the getAbout method
    def userInputGetAbout(self):
        print("Input github reposity details")
        author = input("Enter author:")
        repository = input("Enter repository:")
        response = self.getAbout(author,repository)
        print("---- DETAILS ----")
        if(response != None):
            print(response)
        else:
            print("There was an error requesting the github repo")


