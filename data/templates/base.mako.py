from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1234238713.006834
_template_filename=u'/home/sarah/Documents/action/action/templates/base.mako'
_template_uri=u'/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        next = context.get('next', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">\n<head>\n    <meta http-equiv="content-type" content="text/html; charset=utf-8" />\n    <meta name="author" content="Sarah G Barbour" />\n    \n    <title>Ferocious Kitten</title>\n\n    <!--stylesheets-->\n    <link rel="stylesheet" href="css/colors.css" type="text/css" />\n    <link rel="stylesheet" href="css/layout.css" type="text/css" />\n    <link rel="stylesheet" href="css/markup.css" type="text/css" />\n    <!--javascript-->\n    \n</head>\n<body>\n    <div class="navigation">\n        ')
        # SOURCE LINE 18
        context.write(unicode(h.link_to('home', h.url_for(action="index", title="home"))))
        context.write(u' \n    </div>\n    <div class="content">\n        ')
        # SOURCE LINE 21
        context.write(unicode(next.body()))
        context.write(u'\n    </div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


