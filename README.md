CS4474B - Final Group Project

This project aims to serve as a replacemen to The Weather Network mobile app. 


To run this project, ensure you have the following items installed:
  - Qt Creator (v6.6.1)
      - git clone the file to your local directory
      - When opening the project in Qt creator, open the .pyproject when prompted to open a project
      - When the project has been added to the file view of Qt Creator, it will be incomplete, right click the .pyproject file again and this time select 'Show in File View.' This will expadnd the project to reveal all files associated with the file
  - Go ahead and open the mainwindow.py file, this wil prompt a header that will ask you to install a new venv for the project, this **must** be installed in the directory of the project. Select install for the following dependencies:
      - PySide 6
      - Python 3.9.X or newer
  - Once everything has been installed, in the terminal of QtCreator, use the venv's instance of pip to run the following commands:
      - pip install openmeteo_requests
      - pip install pandas
      - pip install pyinstaller
    
