# Image Captioning App

This is an Image Captioning application built using FastAPI. Users can upload images, and the app will generate detailed captions using a pre-trained transformer model. The app is containerized using Docker and can be easily run using Docker Compose.

## Features

- Upload an image and generate a detailed caption using a transformer-based model.
- Option to append a concept sentence to the caption.
- Built with FastAPI, Uvicorn, and Docker for easy deployment.
- Lightweight frontend using Jinja2 templates and basic HTML/CSS.

### Run the app with Docker Compose

Build and start the app using Docker Compose:

```bash
docker-compose up --build
```

The app will be available at [http://localhost:8000](http://localhost:8000).

### Access the Application

- Open a browser and go to `http://localhost:8000`.
- You can upload an image to generate a caption.
- Optionally, check the checkbox to append a concept sentence to the caption.

## Endpoints

### `GET /`

- Renders the index page where users can upload an image.

### `POST /upload`

- Accepts an image file and generates a caption using the pre-trained transformer model.



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This `README.md` gives an overview of the project, steps for setup and running the app, and information about the project structure. Feel free to update it with specific instructions as needed, especially if your repository has additional requirements or custom features.
