
from app import app
from flask_autoindex import AutoIndex
from app.blueprints.hello_world import hello_world_bp
#from app.blueprints.login import login_bp
from app.auth.auth import auth_bp 



#registry blueprints for all routes
app.register_blueprint(hello_world_bp, url_prefix = "/hello_world")
app.register_blueprint(auth_bp)
#app.register_blueprint(browser_bp, url_prefix = "/browse")


#project folder browse funtionality
files_index = AutoIndex(app, '/usr/src/app/', add_url_rules=False)

#Custom indexing
@app.route('/browse/')
@app.route('/browse/<path:path>')
def autoindex(path='.'):
    return files_index.render_autoindex(path)