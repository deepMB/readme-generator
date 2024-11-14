# Readme Generator using Streamlit and Google Gemini

This Streamlit application uses Google Gemini's large language model to generate a README.md file for your code.  Simply upload your code file, and the app will generate a README based on its content.

## Features

* **Easy Code Upload:** Upload your code file directly through the Streamlit interface.
* **Automated README Generation:**  Leverages the power of Google Gemini to create a well-formatted README.
* **Clean Interface:** Simple and intuitive user experience.

## Requirements

* **Python:**  Ensure you have Python 3.8 or higher installed.
* **Libraries:** You'll need to install the following libraries:
    ```bash
    pip install streamlit langchain_google_genai langchain-core dotenv
    ```
* **Google Generative AI API Key:** You need a Google Cloud project with the Generative AI API enabled and an API key.  This key should be stored in a `.env` file in the same directory as the script, with the key named `GOOGLE_APPLICATION_CREDENTIALS`.  See the [Google Cloud documentation](https://cloud.google.com/generative-ai/docs) for details on setting this up.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   (A `requirements.txt` file should be created containing the necessary libraries listed above)
3. **Create a `.env` file:** Create a file named `.env` in the same directory as the script and add your Google Cloud API key:
   ```
   GOOGLE_APPLICATION_CREDENTIALS="<your_api_key>"
   ```
4. **Run the app:**
   ```bash
   streamlit run app.py 
   ```

## Usage

1. Run the application.
2. Upload your code file (.py, .js, .java, etc.).
3. The application will generate a README.md file based on your code and display it.


## Disclaimer

The quality of the generated README depends on the quality and clarity of your code.  The model may not always perfectly capture the intent of your code, and manual review and editing of the generated README is recommended.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
