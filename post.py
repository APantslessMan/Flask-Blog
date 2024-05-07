class Post:
    def __init__(self, title, subtitle, id, body, image_url, author):
        self.title = title
        self.subtitle = subtitle
        self.id = int(id)
        self.body = body
        self.author = author
        self.image_url = image_url