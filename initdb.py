#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Date:2017-02-07 15:10:14
# @Author:PieterTong
# @Link:https://zhaotongkp.cn
# @Version:0.0.1
from __future__ import unicode_literals
import random
from djangopython.wsgi import *
from front.models import Author, Article, Tag

authorNameList = [ 'pieter', 'twz915', 'dachui', 'hui' ]
articleTitleList = [ 'Django教程', 'Php基础', 'Html教程' ]


def createAuthors () :
    for authorName in authorNameList :
        author, created = Author.objects.get_or_create ( name = authorName )
        #this qq contains 0 begins;
        #so del
        author.qq =str( ''.join ( str ( random.choice ( range ( 10 ) ) ) for _ in range ( 9 ) ))
        # if(author.qq.startswith(0)):
        #     author.qq = str(random.randrange(1,10))+author.qq
        author.addr = '%s_addr_%s' % (authorName, (random.randrange ( 1, 3 )))
        author.email = '%s@zhaotongkp.cn' % (author.addr)
        author.save ( )


def createArticlesAndTags () :
    for articleTitle in articleTitleList :
        tagName = articleTitle.split ( ' ', 1 ) [ 0 ]
        tag, created = Tag.objects.get_or_create ( name = tagName )
        randomAuthor = random.choice ( Author.objects.all ( ) )
        for i in range ( 1, 21 ) :
            title = '%s_%s' % (articleTitle, i)
            article, created = Article.objects.get_or_create (
                    title = title,
                    defaults = {
                        'author' : randomAuthor,
                        'content' : '%s正文' % title,
                        'score' : random.randrange ( 70, 101 )
                    }
            )
            article.tags.add ( tag )


def main () :
    createAuthors ( )
    createArticlesAndTags ( )


if __name__ == '__main__' :
    main ( )
    print "Done!"
