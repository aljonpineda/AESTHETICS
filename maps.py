class MapLocation:
    def __init__(self, title, info, content):
        self.title = title
        self.info = info
        self.content = content

    def listString(self, page_id):
        return "<a href='map?page_id=" + str(page_id) + "'>" + self.title + "</a>"

map_list = [
    
]
