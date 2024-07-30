from config import config
from src import init__app

configuration = config['development']
app = init__app(configuration)

if __name__ == '__main__':

    # host='0.0.0.0', port=5000
    app.run()