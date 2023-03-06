info = dict(first_name = 'John', last_name = 'Doe', age = '35')
def info_kwargs(info):
    sorted_info = sorted(info.items())
    for i in sorted_info:
        print(i[0], i[1], sep = '-')
info_kwargs(info)
