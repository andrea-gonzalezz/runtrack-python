

def draw_rectangle(h, w):
    c = '|' + '-' * (h - 2) + '|\n';
    print(c + c.replace(*'- ') * (w - 2) + c)


draw_rectangle(50, 20)