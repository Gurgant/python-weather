# Python Weather

Python Weather is a web application that provides weather information using real-time data from the OpenWeatherMap API. The application features a Python backend and an HTML/CSS frontend.

## Features

- Real-time weather data
- User-friendly interface
- Support for multiple locations
- Responsive design

## Technologies Used

- **Python**: Backend logic
- **HTML**: Structure of the web pages
- **CSS**: Styling of the web pages

## Getting Started

### Prerequisites

- Python 3.x
- A free account on [OpenWeatherMap](https://openweathermap.org/) to get an API key

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Gurgant/python-weather.git
    cd python-weather
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your OpenWeatherMap API key:
    ```sh
    export OPENWEATHER_API_KEY=your_api_key_here  # On Windows, use `set OPENWEATHER_API_KEY=your_api_key_here`
    ```

### Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.
- All contributors who have helped with the project.
