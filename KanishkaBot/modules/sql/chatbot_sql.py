import threading

from sqlalchemy import Column, String

from KanishkaBot.modules.sql import BASE, SESSION


class KanishkaChats(BASE):
    __tablename__ = "Kanishka_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


KanishkaChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_Kanishka(chat_id):
    try:
        chat = SESSION.query(KanishkaChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_Kanishka(chat_id):
    with INSERTION_LOCK:
        Kanishkachat = SESSION.query(KanishkaChats).get(str(chat_id))
        if not Kanishkachat:
            Kanishkachat = KanishkaChats(str(chat_id))
        SESSION.add(Kanishkachat)
        SESSION.commit()


def rem_Kanishka(chat_id):
    with INSERTION_LOCK:
        Kanishkachat = SESSION.query(KanishkaChats).get(str(chat_id))
        if Kanishkachat:
            SESSION.delete(Kanishkachat)
        SESSION.commit()
