import json
from urllib.request import urlopen
#from pprint import pprint

class LoadJson(object):
    def __init__(self, path_url, bool_is_url):

        self.id = id
        self.path = path_url
        self.target = None

        if bool_is_url is True:
            # 'http://localhost:8080/config_server.json')
            with urlopen(self.path) as u:
                self.target = json.loads(u.read().decode('utf-8'), object_hook=self.JSONObject)
        else:
            with open(self.path, "r") as f:
                self.target = json.loads(f.read().encode('utf-8'), object_hook=self.JSONObject)


    def load_from_id(self, id):
        #pprint(resp.config_server)
        config = None
        count = 0
        for a in self.target.config_server:
            if a.ID == id:
                config = self.target.config_server[count]
            count += 1

        if config is not None:
            return config
        else:
            return 0

    # def load_from_id_dict(self, id):
    #     config = None
    #     count = 0
    #     for a in self.target["config_server"]:
    #         if a["ID"] == id:
    #             config = self.target["config_server"][count]
    #         count += 1
    #
    #     if config is not None:
    #         return config
    #     else:
    #         return 0

    class JSONObject:
        def __init__(self, d):
            self.__dict__ = d

load_json = LoadJson("http://localhost:8080/config_server.json", True)
this=load_json.load_from_id("xxxx1")
print(this.Video.framerate)

load_json = LoadJson("path_to/config_server.json", False)
this=load_json.load_from_id("xxxx1")
print(this.Video.framerate)
