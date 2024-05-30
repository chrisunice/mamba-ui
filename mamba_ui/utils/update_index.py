def update_index(obj, new_index):

    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'id' and 'index' in v:
                v['index'] = new_index  # update index
            elif isinstance(v, (dict, list)):
                update_index(v, new_index)
    elif isinstance(obj, list):
        for item in obj:
            update_index(item, new_index)
