import wikipedia
import time

def download_wikipedia_pages():
    # Set Search Querry
    search_query = "generative artificial intelligence"
    # Set start time
    start_time = time.time()

    # Getting the search results from wikipedia using the search querry
    search_results = wikipedia.search(search_query)

    # iterate over all the search results
    for topic in search_results:
        # Create a txt File
        filename = f"{topic}.txt"

        # setting the page to the wikipedia page of the topic
        page = wikipedia.page(topic, auto_suggest=False)
        # Setting the content to the content
        content = page.content

        # Opening the file and writing the file as a utf-8 file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    
    # Getting End time
    end_time = time.time()
    # Calculating the execution time
    execution_time = end_time - start_time
    # Printing the execution time
    print(f"Execution Time: {execution_time} seconds")

# Call the function
download_wikipedia_pages()