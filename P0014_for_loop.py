#!/usr/bin/env python3

writers = []
books = []

writer = None

while writer != '':
    writer = input('Kérlek, add meg az író nevét! ')
    if writer:
        writers.append(writer)
for writer in writers:
    book = input('Add meg ' + writer + ' egy művét!')
    books.append(book)

for i in range(0, len(writers)):
    print(writers[i], '-', books[i])
