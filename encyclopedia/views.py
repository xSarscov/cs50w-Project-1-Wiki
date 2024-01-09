from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
from .forms import CreateEntryForm, EditEntryForm
import random

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
                "title": TITLE,
                "content": content
            })

        return render(request, "encyclopedia/entry.html", {
            "error": "The requested page was not found."
        })

def search(request):

    if request.method == 'GET':
        query = request.GET['q']
        entries = [entry.upper() for entry in util.list_entries()]

        if not entries:
            return render(request, "encyclopedia/search.html", {
                    "query": query,
                    "error": "No entries found. Please check back later or add new entries."
                })

        if query.upper() in entries:
            return redirect('entries', TITLE=query)
        else:
            matches = find_matches(util.list_entries(), query)

            if matches:   
                return render(request, "encyclopedia/search.html", {
                    "query": query,
                    "matches": matches,
                })
            else:
                return render(request, "encyclopedia/search.html", {
                    "query": query,
                    "error": "Sorry, no entries were found matching the search."
                })

def new_page(request):
    if request.method == 'POST':
        form = CreateEntryForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            util.save_entry(title, content)
            
            return redirect('entries', TITLE=title)
        else:
            print(form.errors)
            return render(request, "encyclopedia/new_page.html", {
                "form": form
            })
        
    return render(request, "encyclopedia/new_page.html", {
        "form": CreateEntryForm
    })

def edit_page(request, TITLE):


    if request.method == 'POST':
        form = EditEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']

            util.save_entry(TITLE, content)

            return redirect('entries', TITLE=TITLE)
        else:
            return render(request, 'encyclopedia/edit_page.html', {
                "title": TITLE,
                "form": form,
            })

    entry = util.get_entry(TITLE)

    if entry:
        entry_data = {
            'content': entry
        }

        form = EditEntryForm(initial=entry_data)

        return render(request, 'encyclopedia/edit_page.html', {
            "title": TITLE,
            "form": form
        })
    else: 
        return render(request, 'encyclopedia/edit_page.html', {
            "title": TITLE,
        })


        
def random_page(request):

    if request.method == 'GET':

        entries = util.list_entries()

        if entries:
            entry = random.choice(entries)
            return redirect('entries', TITLE=entry)
        else:
            return redirect("index")




# Markdown to HTML conversion method
def markdown_to_html(content):
    markdowner = Markdown()
    html_content = markdowner.convert(content)
    return html_content

# Entries search method
def find_matches(list_entries, query):

    matches = []
    query = query.upper()

    if not query:
        return matches    

    matches = [entry for entry in list_entries if entry.upper() in query or query in entry.upper()]

    return matches
