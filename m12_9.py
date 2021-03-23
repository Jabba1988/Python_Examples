# Программа подготовлена И.В. Библовым
# Выводит случайные страницы с сайта vk.com


from webbrowser import open_new
f = open('sites.txt')
for s in f:
    open_new(s)
    
