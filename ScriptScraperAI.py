import time

import requests
from bs4 import BeautifulSoup


# NOTE: Pagination
def pagination():
    try:
        website = "https://subslikescript.com/movies"
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, "lxml")
        pagination = soup.find("ul", class_="pagination")
        pages = pagination.find_all("li", class_="page-item")
        last_page = pages[-2].text
        return int(last_page)
    except:
        return 1


# NOTE: Movie list 
def movie_list(page_number):
    try:
        root = "https://subslikescript.com"
        website = f"{root}/movies?page={page_number}"
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, "lxml")
        main_list = soup.find("article", class_="main-article")

        page_links = []
        page_titles = []

        # Get name and website of the movie for this specific page only
        for link in main_list.find_all("a", href=True):
            page_links.append(link.get("href"))
            page_titles.append(link.get_text().strip())

        return page_titles, page_links
    except Exception as e:
        print(f"Error fetching page {page_number}: {e}")
        return [], []


# NOTE: Fetch all movies
# Practiced fetching titles with pagination
def fetch_all_movies(last_page):
    all_titles = []
    all_links = []

    print(f"Fetching movies from {last_page} pages...")

    # Only fetch first 3 pages for testing to be faster
    pages_to_fetch = min(last_page, 3)

    for i in range(1, pages_to_fetch + 1):
        print(f"Fetching page {i}/{pages_to_fetch}...")
        page_titles, page_links = movie_list(i)
        all_titles.extend(page_titles)
        all_links.extend(page_links)
        # Add a small delay to be respectful to the server
        time.sleep(0.5)

    print(f"Total movies fetched: {len(all_titles)}")
    return all_titles, all_links


# NOTE: Detailed movie information
# Scraped the actual movie data
def movie_info(movie):
    root = "https://subslikescript.com"
    website = f"{root}{movie}"
    try:
        result = requests.get(website)
        soup = BeautifulSoup(result.text, "lxml")
        main_data = soup.find("article", class_="main-article")
        title = (
            main_data.find("h1").get_text()
            if main_data.find("h1")
            else "No title available"
        )
        plot = (
            main_data.find("p", class_="plot").get_text()
            if main_data.find("p", class_="plot")
            else "No plot available"
        )
        transcript = (
            main_data.find("div", class_="full-script").get_text(
                strip=True, separator="\n"
            )
            if main_data.find("div", class_="full-script")
            else "No transcript available"
        )
        return title, plot, transcript
    except Exception as e:
        print(f"Error fetching movie info: {e}")
        return (
            "Error loading movie",
            "Could not retrieve plot",
            "Could not retrieve transcript",
        )


def search_movies(titles, links, query):
    # returns sequential search result numbers
    results = []
    for idx, (title, link) in enumerate(zip(titles, links)):
        if query.lower() in title.lower():
            results.append((title, link))
    return [(i + 1, title, link) for i, (title, link) in enumerate(results)]


def main():
    print("Welcome to Movie Script Finder")
    print("Initializing...")

    last_page = pagination()
    titles, links = fetch_all_movies(last_page)

    while True:
        query = input("\nEnter a movie title to search (or 'exit' to quit): ").strip()
        if query.lower() == "exit":
            break

        search_results = search_movies(titles, links, query)

        if not search_results:
            print("No movies found matching your query.")
            continue

        print(f"\nFound {len(search_results)} results:")
        for idx, title, _ in search_results:
            print(f"{idx}. {title}")

        try:
            selection = int(
                input("\nEnter the number of the movie for details (0 to cancel): ")
            )
            if selection == 0:
                continue

            if selection < 1 or selection > len(search_results):
                print(f"Please enter a number between 1 and {len(search_results)}")
                continue

            selected_movie = search_results[selection - 1][2]
            print("\nFetching movie details...")
            title, plot, transcript = movie_info(selected_movie)

            print(f"\n{'=' * 50}")
            print(f"Title: {title}")
            print(f"{'=' * 50}")
            print(f"Plot: {plot}")
            print(f"{'=' * 50}")
            print(f"Transcript Preview (first 500 chars):")
            print(f"{transcript[:500]}...\n")

            save_option = input(
                "Would you like to save the full transcript? (y/n): "
            ).lower()
            if save_option == "y":
                filename = (
                    title.replace(" ", "_").replace(":", "").replace("/", "_") + ".txt"
                )
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(
                        f"Title: {title}\n\nPlot: {plot}\n\nTranscript:\n{transcript}"
                    )
                print(f"Transcript saved to {filename}")

        except (ValueError, IndexError) as e:
            print(f"Invalid selection: {e}. Please try again.")
            continue


if __name__ == "__main__":
    main()
