# Notes Application with AI Categorization

A Django-based web application for managing notes with automatic category classification using Google's Gemini AI.

## Features
- Create, view, and manage notes
- Automatic category classification (Work, Personal, Study, Health, Shopping, Finance, Other)
- Simple and intuitive interface
- Deployed on Vercel

## Technologies
- Python 3.x
- Django
- Google Gemini AI API
- SQLite (development)

## Setup
1. Clone the repository
2. Create and activate virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create `.env` file
   - Add your Gemini API key: `GEMINI_API_KEY=your_api_key_here`

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start development server:
   ```
   python manage.py runserver
   ```

## Deployment
This app is configured for Vercel deployment:
- `vercel.json` handles routing
- Static files are served from `/static`

## Live Demo
Access the deployed version at: [https://task-er1ktjmv0-tayyab-chattahs-projects-ec164f8d.vercel.app/](https://task-er1ktjmv0-tayyab-chattahs-projects-ec164f8d.vercel.app/)

## Project Structure
```
notes_project/
├── notes/               # Main app
│   ├── models.py        # Notes model definition
│   ├── utils.py         # AI categorization logic
│   └── ...
├── notes_project/       # Project settings
├── manage.py            # Django management
├── requirements.txt     # Dependencies
└── vercel.json          # Vercel config
```

## AI Categorization
The app uses Google's Gemini API to automatically classify notes into categories based on their title and description.

## Contributing
Pull requests are welcome. For major changes, please open an issue first.
