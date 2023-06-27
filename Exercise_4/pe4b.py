import wikipedia
import concurrent.futures
import time

def download_wiki_page(topic):
    # Step 1: Create a file with the title of the topic and a .txt extension 
    filename = f"{topic}.txt"

    # Step 2: Retrieve the Wikipedia page content
    page = wikipedia.page(topic, auto_suggest=False)
    content = page.content

    # Step 2a: write the contents of the wikipedia page to the file
    with open(filename, "w",encoding="utf-8") as file:
        file.write(content)


def concurrent_download_wiki_pages():
    search_query = "generative artificial intelligence"
    start_time = time.time()

    # Step 1: Search for topics related to search query
    search_results = wikipedia.search(search_query)

    # Step 2: Use ThreadPoolExecutor to concurrently execute code for each topic
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit download tasks for each topic
        futures = [executor.submit(download_wiki_page, topic) for topic in search_results]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

    # Calculate and print the execution time
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

# Call the main function
concurrent_download_wiki_pages()