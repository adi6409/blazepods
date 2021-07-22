import chardet
the_encoding = chardet.detect(b'P\xfb0\x050\n\x14\x00')['encoding']
print(the_encoding)