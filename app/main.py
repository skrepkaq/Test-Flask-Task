from app import create_app, run_migrations

app = create_app()

if __name__ == '__main__':
    run_migrations()
    app.run(host='0.0.0.0', port=5000)
