# Flask Recipe Application

A modern web application built with Flask that allows users to manage and share recipes. This application demonstrates the use of Flask blueprints for modular application development, along with user authentication and database management.

## Features

- User Authentication System
  - Registration
  - Login/Logout functionality
  - Password hashing with Bcrypt
- Recipe Management (Coming Soon)
- Responsive UI with Bootstrap
- SQLAlchemy Database Integration
- Environment Variable Configuration
- Blueprint-based Architecture

## Tech Stack

- **Backend**: Python/Flask
- **Database**: SQLAlchemy (configurable for SQLite or other databases)
- **Frontend**: Bootstrap 5
- **Authentication**: Flask-Login, Bcrypt
- **Configuration**: python-dotenv

## Project Structure

```
blueprint-app/
├── run.py                 # Application entry point
├── app/
│   ├── __init__.py
│   ├── app.py            # Main application configuration
│   ├── auth/             # Authentication blueprint
│   │   ├── app.py       # Auth routes and logic
│   │   ├── models.py    # User model
│   │   └── templates/   # Auth-specific templates
│   └── recipes/         # Recipes blueprint (WIP)
```

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/777marc/blueprint-app.git
   cd blueprint-app
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with:

   ```
   DATABASE_URL=sqlite:///./site.db
   SECRET_KEY=your-secret-key
   ```

5. Initialize the database:

   ```bash
   flask db upgrade
   ```

6. Run the application:
   ```bash
   python run.py
   ```

The application will be available at `http://localhost:5000`

## Environment Variables

- `DATABASE_URL`: Database connection string (defaults to SQLite)
- `SECRET_KEY`: Secret key for session management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
