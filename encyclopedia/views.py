from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, TITLE):

    if request.method == 'GET':
        entry = util.get_entry(TITLE)

        if entry is not None:

            # Markdown to HTML Conversion
            content = markdown_to_html(entry)

            return render(request, "encyclopedia/entry.html", {
                "entry": content
            })

        return render(request, "encyclopedia/entry.html", {
            "error": "The requested page was not found."
        })

def search(request):
    if request.method == 'GET':
        query = request.GET['q']

        if any(query in entries for entries in util.list_entries()):   
            return render(request, "encyclopedia/search.html", {
                "si": "si"
            })
        else:
            return render(request, "encyclopedia/search.html", {
                "si": "casi"
            })
    return render(request, "encyclopedia/search.html", {
                "si": "no"
            })

# Markdown to HTML conversion method
def markdown_to_html(content):
    markdowner = Markdown()
    html_content = markdowner.convert(content)
    return html_content