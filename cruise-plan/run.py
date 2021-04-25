from app import app
app.jinja_env.auto_reload = True
app.run(host='127.0.0.1', debug=True)
