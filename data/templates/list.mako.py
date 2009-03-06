from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1235498278.1602621
_template_filename='/home/sarah/Documents/action/action/templates/list.mako'
_template_uri='/list.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'\n<h1>Todo</h1>    \n<span id="arrange">Arrange \n<a href="/task/sort_by_alpha">alphabetically</a>,\n<a href="/task/sort_by_deadline">by deadline</a>\n</span>\n\n<form method="post" action="/task/complete_task">\n    <ul id="todo">\n')
        # SOURCE LINE 10
        for t in c.tasks:
            # SOURCE LINE 11
            context.write(u'        <li>\n            <input type="checkbox" onchange="complete()" name="')
            # SOURCE LINE 12
            context.write(unicode(t.id))
            context.write(u'" />')
            context.write(unicode(t))
            context.write(u'\n        </li>\n')
        # SOURCE LINE 15
        context.write(u'    </ul>\n    <input type="submit" value="update tasks" />\n</form>\n\n\n<form method="post" action="/task/add_new">\n    <input type="text" name="new_task" />\n    <input type="submit" value="Add new task" />\n</form>\n\n<a href="#">see completed tasks</a>\n\n<ul id="done">\n')
        # SOURCE LINE 28
        for d in c.done_tasks:
            # SOURCE LINE 29
            context.write(u'    <li>')
            context.write(unicode(d))
            context.write(u'</li>\n')
        # SOURCE LINE 31
        context.write(u'</ul>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


