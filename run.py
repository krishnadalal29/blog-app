from app import create_app, db

app = create_app()

if __name__ == "__main__":
    app.app_context().push()
    # Create the database tables
    db.create_all()
    app.run(debug=True)
