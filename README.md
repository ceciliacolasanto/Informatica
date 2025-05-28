## 🎵 Project Summary: Ruta del Vinilo – Vinyl Store Management System

**Ruta del Vinilo** is a vinyl record store based in Buenos Aires, Argentina. This project addresses the need for a centralized, efficient system to manage records and their associated song details. Our solution includes backend development, API integration, and data analysis components.

### 🧩 Problem

- Lack of a unified system to consult, add, modify, or delete records.
- No structured access to song-level information for each vinyl.

### 💡 Solution

- Implementation of a **Python-based backend** to manage CRUD operations on a SQLite database.
- Integration of the **Spotify API** to fetch detailed track information for each album.
- Use of **Flask** to create RESTful API endpoints for external access.
- Testing endpoints via **Postman**.
- Conversion of database to CSV for further data analysis in Python.

### ⚙️ Technical Overview

- **class_disco.py**: Defines the `Disco` class with attributes and methods.
- **db_discos.py**: Handles database creation and SQL logic.
- **disco_controller_poo.py**: Contains functions for CRUD operations.
- **api_terceros.py**: Connects to the Spotify API for album data.
- **server_discos_poo.py**: Flask server that exposes the API endpoints (`GET`, `POST`, `PUT`, `DELETE`).
- **Postman**: Used to test all API functionalities.
- **album_datos.csv**: Structured database exported for data analysis.
- **Data Analysis**: Various Python scripts applied for insights on prices, artists, genres, and more.

### 📊 Outcome

The system allows fast and reliable interaction with a vinyl record catalog and enables a full inventory and information management process:

- Add new records when they come into **stock**.
- Check **current stock** of vinyls.
- **Update prices** of individual albums.
- **Delete records** when no longer available.
- Query detailed **song lists** within each album.
- Perform **exploratory data analysis (EDA)** for business insights.
- Quickly answer customer questions about album content and availability.
