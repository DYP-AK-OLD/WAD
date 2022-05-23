import & nbsplogging

from & nbspflask import & nbspFlask app = &nbspFlask(name)


@app.route('/') def hello():
return 'Hello&nbspWorld'

if name == ' main ':
    &nbspapp.run(host='127.0.0.1', port=8080, debug=True)


# yaml file
runtime: python env: flex
entrypoint: gunicorn - b: $PORT & nbspmain: app

runtime_config:
    python_version: 3
# requirements

Flask == 0.11.1
gunicorn == 19.6.0
