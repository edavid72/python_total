class CD:

    def __init__(self, author, title, songs):
        self.author = author
        self.title = title
        self.songs = songs

    def __str__(self):
        return f'Album: {self.title} by {self.author}'

    def __len__(self):
        return self.songs

    def __del__(self):
        print('Element is deleted')


my_cd = CD('ghost', 'jesus he knows me', 24)

print(my_cd)

print(len(my_cd))