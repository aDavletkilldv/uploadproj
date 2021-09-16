import logging
from django.shortcuts import render
from .forms import ImageForm
import PIL
import re

log = logging.getLogger(__name__)

def new_view(request):
    if request.method == 'POST':
        log.info('Method of sending the request POST')
        form = ImageForm(request.POST, request.FILES)

        newimg_open = PIL.Image.open(request.FILES['imgfile'])
        res_of_cb_counter = cb_counter(newimg_open)
        context = dict()
        context['count_white'] = res_of_cb_counter[0]
        context['count_black'] = res_of_cb_counter[1]
        context['res'] = res_of_cb_counter[2]

        hexcode = request.POST.get('hexcode')
        context['form'] = form
        context['message'] = hex_counter(newimg_open, hexcode)

        log.info('Returning a form with the received data')
        return render(request, 'index.html', context)

    else:
        log.info('Method of sending the request not POST')
        form = ImageForm()

    context = {'form': form}
    log.info('Returning a form')
    return render(request, 'index.html', context)


# Функция подсчета черных и белых пикселей
def cb_counter(img_open):
    log.info('Start of the function for counting black and white pixels')
    count_black = 0
    count_white = 0
    for i in img_open.getdata():
        if i[0:3] == (0, 0, 0):
            count_black += 1
        elif i[0:3] == (255, 255, 255):
            count_white += 1

    if count_black > count_white:
        res = 'Черных пикселей больше.'
    elif count_black < count_white:
        res = 'Белых пикселей больше.'
    else:
        res = 'Черных и белых пикселей одинаковое количество.'

    return (count_white, count_black, res)


# Функция для определения по HEX коду
def hex_counter(img_open, hex_code):
    log.info('Start of the function for counting pixels by HEX code')
    if hex_code == '':
        message = 'Вы не ввели HEX код.'
    elif re.fullmatch(r'^[A-Fa-f0-9]{6}', hex_code) is None:
        message = 'Вы ввели неверный HEX код.'
    else:
        int_code = tuple([int(hex_code[i:i+2], base=16) for i in (0, 2, 4)])
        counter = 0
        for i in img_open.getdata():
            if i[0:3] == int_code:
                counter += 1
        if counter:
            message = 'Пикселей с HEX кодом {0}: {1}.'.format(hex_code, counter)
        else:
            message = 'Пикселей с таким HEX кодом нет.'

    return message
