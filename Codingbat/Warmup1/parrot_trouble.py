def parrot_trouble(talking, hour):
  if talking:
    if 7<=hour<=20:
      return not talking
    else:
      return talking
  else:
    return talking
