def print_book_info(title, author=None, year=None):
    information = f'"{title}"'

    if author or year:
        information += ' was written'
        if author:
            information += f' by {author}'
        if year:
            information += f' in {year}'
    print(information)