# ScriptScraperAI

## 🎬 Overview
ScriptScraperAI is a Python application I developed to practice web scraping and OpenAI API integration. The tool scrapes movie scripts from subslikescript.com and allows users to search, view, save transcripts, and ask AI-powered questions about the movies based on their actual content.

This project helped me strengthen my skills in:
- Web scraping with BeautifulSoup
- API integration (OpenAI)
- Command-line interface development
- Handling pagination in web scraping
- Text processing and analysis

## 🚀 Features
- Search through a database of movie scripts
- View movie details including title, plot, and transcript
- Save full movie transcripts locally
- Ask questions about movies and get AI-powered analysis based on the actual script content
- User-friendly command-line interface

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- OpenAI API key (for AI analysis functionality)

### Steps to Install
1. **Clone the repository:**
   ```
       git clone https://github.com/YOUR_USERNAME/ScriptScraperAI.git
       cd ScriptScraperAI
   ```

2. **Set up a virtual environment (recommended):**
   ```
       python -m venv venv
       source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```
       pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key:**
   - Create a `.env` file in the project root directory
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## 🔍 Usage

Run the script using Python:
```
    python ScriptScraperAI.py
```

### Basic Flow:
1. The program will initialize and fetch movie listings (limited to 10 pages for performance)
2. Enter a movie title to search
3. Select from search results to view details
4. Option to save the transcript locally
5. Ask questions about the movie to get AI analysis

## 📝 Important Notes

- **Pagination Limit:** I've limited the pagination to only fetch the first 10 pages of movies to make the program run faster during testing. If you want to scrape all available movies, you can modify the `pages_to_fetch` variable in the `fetch_all_movies()` function.

- **Responsible Scraping:** The code includes a small delay between requests to be respectful to the server. Please maintain this practice if you modify the code.

- **API Key Security:** Never commit your `.env` file with your API key to version control. It's included in `.gitignore` for a reason!

## 📋 Requirements

The following packages are required:
```
requests
beautifulsoup4
python-dotenv
openai
lxml
```

These are listed in the `requirements.txt` file for easy installation.

## 🧠 Learning Reflection

This project was a great opportunity for me to practice web scraping techniques while integrating with one of the most powerful AI APIs available. I learned a lot about handling pagination properly, managing API rate limits, and creating a user-friendly command-line experience.

The most challenging part was properly truncating the movie transcripts to fit within OpenAI's token limits while still preserving enough information for meaningful analysis.

## ⚠️ Disclaimer

This tool is created for educational purposes only.

## 🙏 Acknowledgments

- subslikescript.com for providing publicly accessible movie scripts
- OpenAI for their powerful API

