# -*- coding: utf-8 -*-
"""
:mirrors:`<path>[,<scheme>][,literal]`

path should start with '/'

if literal:
    create a literal block
elif scheme
    create a html link, with text 'scheme://domain/path'
else:
    create a text block
"""

from docutils import nodes, utils

import sphinx


def make_mirrors_role(base_domain):
    def role(typ, rawtext, text, lineno, inliner, options={}, content=[]):
        text = utils.unescape(text).split(',')
        length = len(text)
        if length <= 3:
            text.extend(['']*(3-length))
        else:
            inliner.reporter.warning('wrong mirrors sytax')

        path, scheme, literal = text
        if scheme:
            scheme = text[1] + '://'

        full_url = ''.join([scheme, base_domain, path])

        if literal:
            pnode = nodes.literal(full_url, full_url)
        elif scheme:
            pnode = nodes.reference(full_url, full_url, internal=False, refuri=full_url)
        else:
            pnode = nodes.inline(full_url, full_url)

        return [pnode], []
    return role


def setup_mirrors_role(app):
    app.add_role('mirrors', make_mirrors_role(app.config.mirrors_domain))


def setup(app):
    app.add_config_value('mirrors_domain', '', 'env')
    app.connect('builder-inited', setup_mirrors_role)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
