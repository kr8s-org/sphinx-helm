import os

from docutils import nodes
from docutils.parsers import rst
from docutils.parsers.rst.directives import unchanged
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles

from .gen import gen


class HelmDirective(rst.Directive):
    has_content = True
    required_arguments = 1
    option_spec = {
        'output_format': unchanged,
    }

    def run(self):
        chart_path = os.path.join(
            self.state.document.settings.env.srcdir,
            self.arguments[0],
        )
        if self.options.get('output_format') is None:
            # if page is being built with myst use markdown
            if self.state.document.current_source.endswith('.md'):
                self.options.update({'output_format': 'markdown'})
            else:
                self.options.update({'output_format': 'rst'})
        output = ViewList(gen(chart_path, output_format=self.options.get('output_format')).split("\n"))

        node = nodes.section()
        node.document = self.state.document
        nested_parse_with_titles(self.state, output, node)

        return node.children


def setup(app):
    app.add_directive("helm", HelmDirective)
