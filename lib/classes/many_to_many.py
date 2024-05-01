class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not hasattr(self, '_title'):
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = value

    def _validate_title(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters long")


class Author:

    all_authors = []

    def __init__(self, name):
        self.name = name
        self._articles = []
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self ]

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):  
        if len(self.articles()) == 0:
            return None

        magazine_categories = set()
        for article in self.articles():
            magazine_categories.add(article.magazine.category)
        unique_categories = list(magazine_categories)
        return unique_categories


class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self ]

    def contributors(self):
        return list(set(article.author for article in Article.all if article.magazine == self))
    
    def article_titles(self):
        get_title = [article.title for article in Article.all if article.magazine == self]
        return None if get_title == [] else get_title

        

    def contributing_authors(self):
        contributing_authors = []

        for article in self.articles():
            author = article.author
        if sum(1 for a in author.articles() if a.magazine == self) > 2:
            contributing_authors.append(author)

        if len(contributing_authors) > 0:
            return contributing_authors
        else:
            return None

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article
