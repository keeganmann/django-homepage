 #!python
"""
This file defines a command for importing data from a wordpress xml file.
All files will be created in the database as drafts and with the author
specified by --author.
"""
import xml.parsers.expat
import datetime
from django.utils.timezone import make_aware, get_current_timezone

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

class Command(BaseCommand):
    args = '--author rootauthor filename.xml'
    help = 'Imports articles from the specified wordpress xml file'
    option_list = BaseCommand.option_list + (
        make_option("-a", "--author",
            action="store", 
            type="string", 
            dest="author",
            help='Author for all imported articles'),
        )

    def handle(self, *args, **options):
        from django.contrib.auth.models import User
        string = open(args[0]).read()
        wpp = WordpressParser()
        p = xml.parsers.expat.ParserCreate()
        p.StartElementHandler = wpp.start_element
        p.EndElementHandler = wpp.end_element
        p.CharacterDataHandler = wpp.char_data
        p.Parse(string)
        print 'author for all articles will be ' + options['author']
        author = User.objects.get(username=options['author'])
        wpp.write_to_database(author)
        self.stdout.write('Migration Successful')

class WordpressParser:
    recordable_tags = {
        'title':'title',
        'wp:post_type':'type',
        'wp:attachment_url':'attachment url',
        'content:encoded':'content',
        'wp:post_date': 'date',
        #'pubDate': 'pubdate',
        'wp:post_name' : 'slug',
    }
    def __init__(self):
        self.items = []
        self.item_current = None
        self.current_tag = None

    # 3 handler functions
    def start_element(self, name, attrs):
        self.current_tag = name
        if name == 'item':
            self.item_current = {}
    def end_element(self, name):
        self.current_tag = None
        if name == 'item':
            self.items.append(self.item_current)
            self.item_current = None
    def char_data(self, data):
        if self.item_current == None:
            return 
        if self.current_tag in self.recordable_tags.keys():
            cleaned_key = self.recordable_tags[self.current_tag]
            if not cleaned_key in self.item_current.keys():
                self.item_current[cleaned_key] = ""
            self.item_current[cleaned_key] += unicode(data)

    def write_to_database(self, author):
        print "Writing to Database..."
        self.migrate_posts(author)

    def migrate_posts(self, author):
        from articles.models import Article
        timezone = get_current_timezone()
        for item in self.items:
            if item['type'] in ('page','post'):
                print '  migrating page : ' + item['title']
                a = Article(
                    title=item['title'] + "(PAGE)",
                    content=item['content'],
                    author=author,
                    publish_date=make_aware(datetime.datetime.strptime(item['date'], "%Y-%m-%d %H:%M:%S"), timezone),
                    )
                a.save()
                print '         ...done'

    def get_first_caption_start(self, string):
        """
        >>> wpp = WordpressParser()
        >>> wpp.get_first_caption_start("Hello [caption annoying] World!")
        WORK IN PROGRESS
        """
        start_index = string.find('[caption') + len('[caption')
        end_index = string.find(']', start_index)
        string = string[start_index:end_index]
        result = {'start':start_index, 'end':end_index}

        quoted = False
        after_equal = False
        key = ""
        value = ""
        for char in string:
            if not after_equal:
                if char == ' ':
                    pass #wait for key
                elif char == '=':
                    after_equal = True #key finished
                else:
                    key += char #building key
            else:
                if char == '"':
                    quoted = True

    def get_first_caption_end(self, string):
        """WORK IN PROGRESS"""
        i1 = string.find('[caption')
        i2 = string.find(']')

import optparse

def main():
    o_parse = optparse.OptionParser()
    o_parse.add_option('--file', '-f', default="wordpress.xml")
    o_parse.add_option('--printout', '-p', default='false')
    o_parse.add_option('--migrate', '-m', default='false')
    options, arguments = o_parse.parse_args()
    print 'Loading file %s' % options.file
    string = open(options.file).read()

    wpp = WordpressParser()
    p = xml.parsers.expat.ParserCreate()
    p.StartElementHandler = wpp.start_element
    p.EndElementHandler = wpp.end_element
    p.CharacterDataHandler = wpp.char_data
    p.Parse(string)
    if options.printout != 'false':
        for item in wpp.items:
            print "===== ITEM ====="
            for key, value in item.items():
                print "  " + key + " : " + value
    if options.migrate != 'false':
        wpp.write_to_database()
    print "Finished"

if __name__ == '__main__':
    main()
