from aqt.gui_hooks import deck_browser_will_render_content

from .utils import make_graph_js


def add_graphs_to_deckbrowser(self, content):
    graph_js = make_graph_js(["CalendarGraph", "CardCounts"])

    content.stats += '<div id="graphsSection"></div>' f"<script>{graph_js}</script>"


def init_deckbrowser():
    deck_browser_will_render_content.append(add_graphs_to_deckbrowser)