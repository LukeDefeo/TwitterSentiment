__author__ = 'Luke'

"Code for this function " \
" from http://stackoverflow.com/questions/323750/how-to-access-previous-next-element-while-for-looping"
def neighborhood(iterable):
    iterator = iter(iterable)
    prev = None
    item = iterator.next()
    for next in iterator:
        yield (prev, item, next)
        prev = item
        item = next
    yield (prev, item, None)

