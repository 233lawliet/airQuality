class City:
    def __init__(self, id, name, longitude, latitude, url=""):
        self.id = int(id)
        self.name = name
        self.longitude = float(longitude)
        self.latitude = float(latitude)
        self.url = url

    def addUrl(self, targetUrl, token):
        self.url = targetUrl + "geo:" + self.latitude + ";" + self.longitude + "/?token=" + token

