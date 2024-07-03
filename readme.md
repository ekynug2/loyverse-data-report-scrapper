```markdown
# Loyverse Data Reports Scraper

This project is a web scraper for extracting report sales by item data from the Loyverse dashboard using Selenium and saving the data to an Excel file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/loyverse-data-scraper.git
   cd loyverse-data-scraper
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Install Chromedriver via Homebrew:**

   ```sh
   brew install chromedriver
   ```

5. **Create a `.env` file in the root directory and add your login credentials:**

   ```plaintext
   EMAIL=your_email@example.com
   PASSWORD=your_password
   ```

## Usage

1. **Run the scraper script:**

   ```sh
   python scraper.py
   ```

   This will open a Chrome browser, log into Loyverse, navigate to the sales report page, and save the data to `loyverse_data.xlsx`.

## Environment Variables

The following environment variables are used in the project:

- `EMAIL`: Your Loyverse account email.
- `PASSWORD`: Your Loyverse account password.

## Project Structure

```plaintext
loyverse-data-scraper/
├── .env                # Environment variables
├── .gitignore          # Git ignore file
├── README.md           # Project readme file
├── requirements.txt    # Python dependencies
├── scraper.py          # Main scraper script
├── venv/               # Virtual environment directory
```

## Dependencies

- `selenium`: A browser automation tool.
- `pandas`: A data manipulation and analysis library.
- `python-dotenv`: A tool to read environment variables from a `.env` file.
- `openpyxl`: A library to read/write Excel files.

Install all dependencies using:

```sh
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.
```

### Save the README file

Save the content above to a file named `README.md` in the root directory of your project. This provides essential information about your project, making it easier for others (and yourself) to understand and use the project.