def find_by_second_element(dictionary, element):

  for i in dictionary:
    if dictionary[i] == element:
      return i
  
  raise Exception(f"Exception: Didn't find element in {dictionary}: {element}")