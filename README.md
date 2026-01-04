# Hotel Management System (Tkinter + SQLite)

This repository contains a lightweight desktop application for managing a hotel. It is built with **Tkinter** and stores data in an **SQLite** database. The codebase is organized into layered modules (Entity, Repository, Controller, and View) for managing rooms, guests, and reservations.

## Prerequisites
- Python 3.10 or newer
- Python packages: `Pillow` (for loading images in Tkinter)
- SQLite (ships with Python)
- Tkinter (installed by default on most Python distributions)

## Quick start
1. Create and activate a virtual environment (optional):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install Pillow
   ```
3. Create the SQLite database:
   ```bash
   python - <<'PY'
   from model.repository.database_creator import creat_database
   creat_database()
   PY
   ```
4. Run the main application (three-section management panel):
   ```bash
   python main.py
   ```

## Project structure
- `model/entity/`: Entities such as `Guest`, `Room`, and `Reservation` with field validation.
- `model/repository/`: CRUD operations on SQLite for each entity, plus `database_creator.py` to build the initial tables.
- `model/tool/validation.py`: Input validators (codes, dates, prices, capacities, and more).
- `controller/`: Connects views to repositories, constructing data objects and handling errors.
- `view/`: Tkinter UI for managing guests, rooms, and reservations, plus the main panel `panel_view.py`.
- `test/`: Example scripts for manual testing of repository and controller methods (most lines are commented; uncomment what you need before running).

## Usage notes
- Run the database creation step before first launch to ensure `hotel_db.sqlite` exists.
- Tkinter requires a display; running the app on a headless machine (e.g., GUI-less server) can fail. Use a system with a graphical environment.
- UI images live in `view/` and are loaded via `Pillow`; avoid renaming or moving them.

## Sample tests
The `test/` directory includes examples for saving, editing, deleting, and searching. To run a test, uncomment the scenario you want and execute the file with Python:
```bash
python test/room_test.py
```
Make sure the database has been created beforehand so inserts and queries work without errors.
