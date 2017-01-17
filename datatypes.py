
def data_type(data):
  if data is None:
    return 'no value'
  t = type(data)
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