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

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

    def __repr__(self):
        return f"<{type(self).__name__} " \
               f"title=\"{self.title}\" " \
               f"author='{self.author}' " \
               f"publication_date='{self.publication_date.isoformat()}'>"

    def __len__(self):
        return len(self.content)

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
