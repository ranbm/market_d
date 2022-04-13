from market import app
import os


#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=os.environ.get('DEBUG') == '1')