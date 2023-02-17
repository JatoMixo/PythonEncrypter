def parse_words(string):

  words = [""]

  for i in string:
    if i == " ":
      words.append("")
      continue

    words[len(words) - 1] += i
  
  return words

def parse_int(string):

  result = parse_words(string)

  for index, number in enumerate(result):

    if number == "":
      continue

    result[index] = int(number)
  
  return result