import datetime

import action.lib.helpers as h

from pylons import config
from sqlalchemy import Column, MetaData, Table, types
from sqlalchemy.orm import mapper
from sqlalchemy.orm import scoped_session, sessionmaker

Session = scoped_session(sessionmaker(autoflush=False,
    autocommit=True, bind=config['pylons.g'].sa_engine))

metadata = MetaData()

#by default, everything should be done yesterday.
yesterday = datetime.date.today() + datetime.timedelta(-1)

tasks_table = Table('tasks', metadata,
        Column('id', types.Integer, primary_key=True, autoincrement=True),
        Column('task', types.Unicode(100)),
        Column('description', types.Unicode(), default=''),
        Column('deadline', types.DateTime(), default=yesterday),
        Column('done', types.Boolean(), default='False')
        )

class Task(object):
    def __init__(self, task, desc, dl, done):
        self.task = task
        self.description = desc
        self.deadline = dl
        self.done = done

    def __str__(self):
        return self.task

    def __cmp__(self, other):
        return cmp(self.task, other.task)

mapper(Task, tasks_table)
