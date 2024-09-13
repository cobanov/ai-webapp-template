# Image Captioning App

> **_Template for any AI web application_**

This project provides a FastAPI-based web application for generating captions for images using a pre-trained transformer model. It also includes command-line utilities for image captioning with both single-threaded and parallel processing options.

## Features

- **FastAPI Web Interface**: Upload images and get captions via a user-friendly web interface.
- **Parallel Processing**: Speed up caption generation by using multiple threads.
- **Model**: Utilizes a pre-trained model from Hugging Face to generate detailed image captions.
- **Docker Support**: Containerize the application using Docker for easy deployment.

## Installation

### Prerequisites

- Python 3.8 or higher
- CUDA for GPU acceleration (optional)
- Docker (optional for containerized deployment)
- Windows, Linux, or MacOS for script execution

#### Linux/MacOS

You can use the `run_webapp.sh` script to set up and run the environment:

First, ensure the script has executable permissions:

```bash
chmod +x start_server.sh
```

Then run it:

```bash
./run_webapp.sh
```

This script will create a virtual environment, install the required dependencies from `requirements.txt`, and start the FastAPI server.

#### Windows

Use the `run_webapp.bat` script to set up and run the environment:

```bash
.\run_webapp.bat
```

This will check if a virtual environment exists, create one if needed, install dependencies, and run the FastAPI server.

3. The server will start at `http://localhost:8000`.

### Running with Docker

You can also use Docker to run the application:

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Start the application:

   ```bash
   docker-compose up
   ```

## Usage

### Web Application

Once the server is running, visit `http://localhost:8000` to access the web interface. You can upload images and receive captions based on the selected model.

### Command-Line Interface (CLI)

#### Single-Threaded Mode

Run the caption generator in single-threaded mode using:

```bash
python app.py /path/to/image1.jpg /path/to/image2.jpg
```

#### Parallel Mode

For faster caption generation, use the parallel version:

```bash
python app_parallel.py --workers 4 /path/to/image1.jpg /path/to/image2.jpg
```

The `--workers` flag allows you to specify the number of threads.

## Model Details

The application uses the `multimodalart/Florence-2-large-no-flash-attn` model from Hugging Face, which is loaded using the `transformers` library. It supports both CPU and GPU (CUDA) acceleration.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
