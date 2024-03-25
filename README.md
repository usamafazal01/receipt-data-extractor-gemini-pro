# Receipt Extractor with Gemini Pro API

## Overview

Welcome to the Receipt Extractor project powered by the Gemini Pro API. This solution allows for effortless extraction of data from receipts using Gemini Pro's robust service.

## Getting Started

### Prerequisites

Before diving into this project, ensure you have the following:

- Python 3.10
- Access to the Gemini Pro API Key ([Obtain it here](https://aistudio.google.com/app/apikey))

### Installation

Let's set up the project step by step:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/usamafazal01/receipt-data-extractor-gemini-pro.git
    cd receipt-data-extractor-gemini-pro
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the API key:**
    - Obtain your Gemini Pro API key from the [Gemini Pro Developer Portal](https://aistudio.google.com/app/apikey).
    - Store the API key securely, considering options like environment variables or a configuration file.

## Project Structure

The project follows a simple structure:

- **app.py**: This is the main application file where the receipt extraction functionality is implemented.
- **show_data.py**: This file converts the extracted JSON data into tabular form and displays it as clean data. Additionally, it provides the functionality to download this tabular data as an Excel file to your computer.
- **requirements.txt**: Contains a list of Python packages required for the project.

## Usage

To use the application, simply run the following command:

```bash
streamlit run app.py
