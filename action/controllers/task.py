import logging
import datetime

from action.lib.base import *
from action.model import Task

log = logging.getLogger(__name__)

#used in add_new
yesterday = datetime.date.today() + datetime.timedelta(-1)

class TaskController(BaseController):

    def index(self):
        sorter = lambda tsks: tsks 
        return self.view_page(sorter)

    def view_page(self, sorter):
        c.tasks = sorter(Session.query(Task).filter(Task.done==False).all())
        c.done_tasks = sorter(Session.query(Task).filter(Task.done==True).all())
        return render('/list.mako')

    def sort_by_deadline(self):
        def sorter(tsks):
            tsks.sort(lambda x, y: (x.deadline - y.deadline).days)
        return self.view_page(sorter)

    def sort_by_alpha(self):
        sorter = lambda tsks: tsks.sort()
        return self.view_page(sorter)
    
    def complete_task(self):
        to_complete = map(int, request.params.keys())
        for task_id in to_complete:
            task = Session.query(Task).filter(Task.id==task_id).first()
            task.done = True
        Session.flush()
        redirect_to(action='index')

    def add_new(self):
        Session.begin()
        t = Task(request.params['new_task'], u'', yesterday, False)
        Session.add(t)
        Session.commit()
        #TODO: ajaxify this
        redirect_to(action='index')
