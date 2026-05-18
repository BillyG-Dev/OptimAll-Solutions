# OptmAll Django Project

A minimal Django site for the `pages` app with homepage and contact page templates.

## Project structure

- `manage.py` — Django command-line utility
- `config/` — core project settings and URL routing
- `pages/` — app views, URLs, and placeholder models
- `templates/` — shared HTML templates and page content
- `static/css/` — site styling
- `db.sqlite3` — development database

## Setup

1. Activate the virtual environment:
   - Windows PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
2. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
3. Run the development server:
   ```powershell
   python manage.py runserver
   ```
4. Visit `http://127.0.0.1:8000/` in your browser.

## Updating dependencies

This project includes a helper script that regenerates `requirements.txt` from the active Python environment.

```powershell
python update_requirements.py
```

This will overwrite `requirements.txt` with the current `pip freeze` output.

If you prefer manual regeneration, run:

```powershell
python -m pip freeze > requirements.txt
```

## Notes

- `STATICFILES_DIRS` is configured in `config/settings.py` to load the `static/` folder.
- The project uses Django 6.0.3 and a small set of core dependencies.
