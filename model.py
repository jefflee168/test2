# coding: utf8

import web, datetime

db = web.database(dbn='mysql', db='blog', user='root', pw='redhat',host='10.0.0.20')

def get_posts():
    return db.select('entries', order='id DESC')

def get_post(id):
    try:
	return db.select('entries', where='id=$id', vars=locals())[0]
    except IndexError:
	return None

def new_post(title, text):
    db.insert('entries', title=tile, content=text, posted_on=datetime.datetime.utcnow())

def del_post(id):
    db.delete('entries', where='id=$id', vars=locals())

def update_post(id,title,text):
    db.update('entries', where='id=$id', vars=locals(),
        title=title, content=text)