#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bottle import route, run, get, post, run, request, template, response

@route('/hello/world')
def hello():
    return template('Hello {{string}}', string = 'World')

@route('/greeting/<name>')
def greeting(name):
    return template('Hello {{name}}.', name = name)


@route('/')
def main_page():
    return template('Hello {{string}}.', string = "main")

@route('/show_header')
def show_header():
    headers_list = ["<p> %s = %s <p>" % (k,v) for k, v in request.headers.items()]
    # headers_list = ["aabb", "cc"]
    return "".join(headers_list)

@route('/show_cookie')
def show_header():
    count = request.cookies.get('count')
    return template('count={{count}}', count = count)

@get('/show_query')
def show_query():
    keyword = request.query.keyword
    return template(
    'keyword={{keyword}}.',
    keyword=keyword)

@get('/show_form')
def show_form():
    name = request.forms.get('name')
    return template('name={{name}}.',name=name)

@post('/show_file')
def show_file():
    upload_file = request.files.get('name')
    return template(
        'file_name={{file_name}}.',
        file_name=upload_file.file_name)

@get('/set_response')
def set_response():
    response.status = 200
    response.set_header("Cache-Control", "max-age=0")
    response.set_cookie("spam", "egg")

@route('/show/<id>')
def show(id):
    return template('show', id=id)

# @get('/itmes')
# def lists():
#     pass
#
# @post('/itmes')
# def add():
#     pass

if __name__ == '__main__':
    run(host='localhost',
        port=1112,
        debug=True,
        reloader=True)
