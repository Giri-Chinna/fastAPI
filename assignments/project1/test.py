BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science', 'tag' : None},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science', 'tag' : None},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history', 'tag' : None},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math', 'tag' : None},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math', 'tag' : 'favorite'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math', 'tag' : 'favorite'}
]

print([book for book in BOOKS if book['tag'] == 'favorite'])