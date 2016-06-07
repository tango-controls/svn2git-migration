import pycurl
import urllib
import json

GITHUB_API_URL = "https://api.github.com"

class pyGitHub(object):
    """
    """

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.data = None    

    def setUsername(self, user):
        self.username = username

    def setPassword(self, pwd):
        self.password = password

    def curl(self, url, args={}, custom=None):
        conn = pycurl.Curl()

        self.data = ""
        conn.setopt(pycurl.URL, url)
        conn.setopt(pycurl.WRITEFUNCTION, self.callback)

        if self.username is not None:
             conn.setopt(pycurl.USERNAME, self.username)

        if self.password is not None:
             conn.setopt(pycurl.PASSWORD, self.password)

        if len(args) != 0:
            data = json.dumps(args)
            conn.setopt(pycurl.POSTFIELDS, data)

        if custom is not None:
            conn.setopt(pycurl.CUSTOMREQUEST, custom)

        conn.perform()
        conn.close()

    def ls(self):
        url = GITHUB_API_URL + "/user/repos"
        self.curl(url)
        
        list = json.loads(self.data)
        for i in range(len(list)):
            print list[i]['name']
            print "    " + list[i]['description']
            print "    " + list[i]['clone_url']


    def mk(self, name, org=None, homepage=None, description=None, 
           team_id=None, private=False):
        url = GITHUB_API_URL + "/user/repos"
        if org is not None:
            url = GITHUB_API_URL + "/orgs/" + org + "/repos"
        args = {
            "name": name,
            "has_issues": True,
            "has_wiki": True,
            "has_downloads": True
            }

        if homepage is not None:
            args["homepage"] = homepage
        
        if description is not None:
            args["description"] = description

        if team_id is not None:
            args["team_id"] = team_id
        if private is not None:
            args["private"] = private

        self.curl(url, args=args)

        msg = json.loads(self.data)
        print msg['name'], "Created"
        print "    " + msg['description']
        print "    " + msg['clone_url']


    def rm(self, owner, repo):
        url = GITHUB_API_URL + "/repos/" + owner + "/" + repo
        print "rm %s" % url
        self.curl(url, custom="DELETE")
        if self.data != "":
            msg = json.loads(self.data)
            print msg["message"]
        else:
            print "Done"

    def callback(self, data):
        self.data = self.data + data


if __name__ == "__main__":

    GH = pyGitHub(username="gjover", password="")

    # List repositories
    GH.ls()

    # Create Repository
    # GH.mk("Test_usr", description="personal test")
    GH.mk("Test_org", org="tango-controls", 
          homepage="http://www.tango-controls.org/",
          description="Test project. " +
          "All the information will be used in searches. " +
          "Tags: " + "/Instrumentation/Tektronix".replace("/"," "),
          )

    # Delete Repo
    GH.rm("tango-controls","Test_org")

