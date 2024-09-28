from ui import create_main_window
from db import initialize_db

if __name__ == '__main__':
    initialize_db()  # Initialize the database
    create_main_window()  # Launch the GUI
