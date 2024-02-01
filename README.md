
# Truecaller_lite

Truecaller_lite is a Python web application project hosted on GitHub. It is a simplified version of the Truecaller application, allowing users to search for phone numbers and view details associated with those numbers.

## Repository Structure

- **templates/**: Directory containing HTML templates for the web pages.
- **static/**: Directory containing static files such as CSS stylesheets and JavaScript files.
- **app.py**: Python script containing the main application logic and Flask routes.
- **requirements.txt**: File listing all Python dependencies required to run the application.
- **Procfile**: File specifying the command to run the application on a Heroku server.
- **runtime.txt**: File specifying the Python version required to run the application.

## Dependencies

The project relies on the following Python libraries, listed in the `requirements.txt` file:

- Flask
- gunicorn
- requests

## Main Components

- **app.py**: Contains Flask application logic and routes for:
  - `/`: Home page where users can enter a phone number to search.
  - `/search`: Handling phone number search requests.
  - `/details/<phone_number>`: Displaying details associated with a phone number.

- **templates/**: Contains HTML templates for the web pages rendered by the Flask application:
  - `index.html`: Template for the home page.
  - `search.html`: Template for displaying search results.
  - `details.html`: Template for displaying details of a phone number.

- **static/**: Contains static files such as CSS stylesheets (`style.css`) and JavaScript files (`script.js`) used for styling and client-side interactions on the website.

## Deployment

The project is designed to be deployed on a web server. It includes a `Procfile` for specifying the command to run the application on a Heroku server and a `runtime.txt` file specifying the Python version required to run the application.

## Usage

To run the project locally:
1. Clone the repository: `git clone https://github.com/suhassk-hash/Truecaller_lite.git`
2. Navigate to the project directory: `cd Truecaller_lite`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the Flask application: `python app.py`
5. Open a web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Contributors

The project is maintained by [suhassk-hash](https://github.com/suhassk-hash). Contributions from other developers are welcome through pull requests.
```
