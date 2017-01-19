
def data_type(data):
  print "If no data provided:"
  print " no value"
  if data is None:
    return 'no value'
  print "Retrieve data type using inbuilt type function"
  t = type(data)
  print "If data type is integer:"
  print " If data is less than 100:"
  print "   less than 100"
  print " else If data greater than 100:"
  print "   more than 100:"
  print " else (equal to 100):"
  print "   equal to 100"
  print "else If data type is list:"
  print " If data length is greater than 2:"
  print "   value at index 2"
  print " else:"
  print "   None"
  print "else If data type is string:"
  print " number of characters in data"
  print "else If data type is boolean:"
  print " True/False"
  print "else:"
  print " Value Error"
  if t is int:
    if data < 100:
      return 'less than 100'
    elif data > 100:
      return 'more than 100'
    else:
      return 'equal to 100'
  elif t is list:
    if len(data) > 2:
      return data[2]
    else:
      return None
  elif t is str:
    return len(data)
  elif t is bool:
    return data
  else:
    raise ValueError("This function does not support the provided data type")