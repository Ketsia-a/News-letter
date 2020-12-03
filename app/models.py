class News:
    def __init__(self,id,name,url,category):
        self.id = id
        self.name = name
        self.url = url
        self.category = category

class Article:
    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

# class Category:

#     def __init__(self, id,title,text):
#         self.id = id
#         self.title = title
#         self.text = text