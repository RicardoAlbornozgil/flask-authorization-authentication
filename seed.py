from app import app, db
from models import User, Feedback
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

def seed_database():
    # Create tables if they don't exist
    db.create_all()

    # Create some sample users if they don't already exist
    if not User.query.filter_by(username='john_doe').first():
        hashed_password = bcrypt.generate_password_hash('password123').decode('utf-8')
        user1 = User(
            username='john_doe',
            password=hashed_password,
            email='john@example.com',
            first_name='John',
            last_name='Doe'
        )
        db.session.add(user1)

    if not User.query.filter_by(username='jane_smith').first():
        hashed_password = bcrypt.generate_password_hash('password456').decode('utf-8')
        user2 = User(
            username='jane_smith',
            password=hashed_password,
            email='jane@example.com',
            first_name='Jane',
            last_name='Smith'
        )
        db.session.add(user2)

    # Commit the session to persist the changes
    db.session.commit()

    # Create some sample feedback
    feedback1 = Feedback(
        title='Feedback 1',
        content='This is the first feedback.',
        user=User.query.filter_by(username='john_doe').first()  # Associate feedback with user
    )
    feedback2 = Feedback(
        title='Feedback 2',
        content='This is the second feedback.',
        user=User.query.filter_by(username='jane_smith').first()  # Associate feedback with user
    )

    # Add feedback to the session
    db.session.add(feedback1)
    db.session.add(feedback2)

    # Commit the session to persist the changes
    db.session.commit()

if __name__ == '__main__':
    # Connect to the Flask app
    with app.app_context():
        # Seed the database with sample data
        seed_database()
