import wikipedia

no_page_complete = True
while no_page_complete:
    search_phrase = input("Enter a page title: ")
    try:
        page = wikipedia.page(search_phrase)
        print("About {}".format(page.title))
        print(page.summary)
        print("Info from: {}".format(page.url))
        no_page_complete = False
    except wikipedia.exceptions.DisambiguationError as search_phrase:
        print(search_phrase.options)
    except wikipedia.exceptions.PageError:
        print("No page with that title")