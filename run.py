from app import create_app

# pick function create_app (folder: app/) 
app = create_app()

if __name__ == '__main__':
    
    # Running server!
    print("Running Website...")

    # for development
    app.run(debug=False)