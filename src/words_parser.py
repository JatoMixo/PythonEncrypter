def parse_words(string):

  words = [""]

  for i in string:
    if i == " ":
      words.append("")
      continue

    words[len(words) - 1] += i
  
  return words