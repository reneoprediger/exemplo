from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This "renders" the index.html file located in your /templates folder
    return render_template('index.html', title="My Python App")

if __name__ == "__main__":
    app.run()

