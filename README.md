# python-projects

## FLASK

'''
    # flask --app main.py --debug run

    from flask import Flask, jsonify, request
    import json

    app = Flask(__name__)
    
    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"    

    if "main" in __name__:
        app.run()

'''

