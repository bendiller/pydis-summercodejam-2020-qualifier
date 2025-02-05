"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import re
import typing


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""
    # I've never used a descriptor before, this was useful to learn!
    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.field_type):
            raise TypeError(
                f"Expected {self.field_type.__name__} for attribute {self.name}, got {type(value).__name__} instead"
            )
        else:
            obj.__dict__[self.name] = value


class Article:
    """The `Article` class you need to write for the qualifier."""
    next_id = 0
    title = ArticleField(str)
    author = ArticleField(str)
    publication_date = ArticleField(datetime.datetime)
    _content = ArticleField(str)

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self._content = content
        self.id = Article.next_id
        Article.next_id += 1
        self.last_edited = None

    def __repr__(self):
        return f"<{type(self).__name__} " \
               f"title=\"{self.title}\" " \
               f"author='{self.author}' " \
               f"publication_date='{self.publication_date.isoformat()}'>"

    def __len__(self):
        return len(self.content)

    def __lt__(self, other):
        return self.publication_date < other.publication_date

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content
        self.last_edited = datetime.datetime.now()

    def short_introduction(self, n_characters):
        if len(self.content) <= n_characters:
            return self.content

        # Can probably clean this up some
        last_space = self.content[:n_characters+1].rfind(' ')
        last_newline = self.content[:n_characters+1].rfind('\n')
        last_idx = last_space if last_space > last_newline else last_newline

        return self.content[:last_idx]

    def most_common_words(self, n_words):
        # Break into alphabetic words only (i.e. "It's" -> "It" and "s")
        p = re.compile('\w+')
        word_list = p.findall(self.content.lower())

        counts = {k: word_list.count(k) for k in dict.fromkeys(word_list)}

        # Sort and limit to only n_words
        return {k: v for k, v in sorted(counts.items(), key=lambda item: -item[1])[:n_words]}
