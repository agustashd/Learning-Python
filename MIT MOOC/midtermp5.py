def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    new_dict = {}
    for keys in d:
      if d[keys] in new_dict:
        new_dict[d[keys]].append(keys)
      else:
        new_dict[d[keys]] = [keys]
      new_dict[d[keys]].sort()

    return new_dict



d = {8: 6, 2: 6, 4: 6, 6: 6}
print(dict_invert(d))