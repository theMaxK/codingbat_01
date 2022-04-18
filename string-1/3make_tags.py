from distutils.archive_util import make_archive


def make_tags(tag, word): 
    open_tag = '<' + tag + '>'
    close_tag = '</'+tag+'>'
    return open_tag+word+close_tag

print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))

