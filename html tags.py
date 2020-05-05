def make_tags(tag, word):
      return "<%s>%s</%s>" % (tag, word, tag)
print(make_tags('html', 'tags'))

def make_out_word(out, word):
      return out[:2] + word + out[2:]
print(make_out_word("<<>>", "worked"))



