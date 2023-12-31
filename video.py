class Video:
    def __init__(self, obj):
        self.id = obj.get('id', None)
        self.type = obj.get('type', None)
        self.title = obj.get('title', None)
        self.publishedTime = obj.get('publishedTime', None)
        self.duration = obj.get('duration', None)
        self.viewCount = obj.get('viewCount', None)
        self.thumbnails = obj.get('thumbnails', None)
        self.richThumbnail = obj.get('richThumbnail', None)
        self.descriptionSnippet = str(obj.get('descriptionSnippet', None))
        self.channel = obj.get('channel', None)
        self.accessibility = obj.get('accessibility', None)
        self.link = obj.get('link', None)
        self.shelfTitle = obj.get('shelfTitle', None)

    def validate(self):
        if self.descriptionSnippet.lower().find("karaoke")!=-1:
            return False
        if self.descriptionSnippet.lower().find("instrumental")!=-1:
            return False
        if self.title.lower().find("karaoke")!=-1:
            return False
        if self.title.lower().find("instrumental")!=-1:
            return False
        return True
