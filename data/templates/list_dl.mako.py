from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1233985513.1468029
_template_filename='/home/sarah/Documents/action/action/templates/list_dl.mako'
_template_uri='/list_dl.mako'
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
        context.write(u'\n<h1>Todo, sorted by deadline</h1>\n<ul id="todo">\n')
        # SOURCE LINE 4
        for t in c.tasks:
            # SOURCE LINE 5
            context.write(u'    <li>\n        ')
            # SOURCE LINE 6
            context.write(unicode(t))
            context.write(u'\n    </li>\n')
        # SOURCE LINE 9
        context.write(u'</ul>\n\n<form method="post" action="/task/add_new">\n    <input type="text" name="new_task" />\n    <input type="submit" value="Add new task" />\n</form>\n\n    \n')
        return ''
    finally:
        context.caller_stack.pop_frame()


