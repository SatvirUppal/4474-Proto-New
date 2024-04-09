CS4474B - Final Group Project

This project aims to serve as a replacement to The Weather Network mobile app. 


To run this project, ensure you have the following items installed:
  - Qt Creator (v6.6.1)
      - ```git clone``` the repo to your local directory
      - When opening the project in Qt creator, open the .pyproject when prompted to open a project
      - When the project has been added to the file view of Qt Creator, it will be incomplete, right click the .pyproject file again and this time select 'Show in File View.' This will expadnd the project to reveal all files associated with the file
  - Go ahead and open the mainwindow.py file, this wil prompt a header that will ask you to install a new venv for the project, this **must** be installed in the directory of the project. Select install for the following dependencies:
      - If this is not installed, please contact Satvir Uppal (suppal46@uwo.ca) to resolve the issue, there sometimes is an issue with the code and we will be able to resolve it quickly via some finesse
      - PySide 6
      - Python 3.9.X or newer
  - Once everything has been installed, in the terminal of QtCreator, use the venv's instance of pip to run the commands. To change the pip on the current machine run the following command in the terminal:  
      - ```.\venv\Scripts\activate``` This should change to the venv of the project. You can proceed to run the commands below:
      - ```pip install openmeteo-requests```
      - ```pip install retry-requests```
      - ```pip install requests-cache```
      - ```pip install pandas```
      - ```pip install pyinstaller```
Now that the dependencies have been installed, you should be able to use QtCreator to run the application by clicking the green play arrow as a test to ensure the dependencies are installed correctly. If they are not, please repeat the above section again but using the venv/ instance of pip.

To create a .exe please use the following command:
``` pyinstaller --noconsole --onefile --windowed mainwindow.py```
Once the command has finished, navigate to the newly created ```dist``` folder and run mainwindow.exe

Here are a list of locations you are able to run the application from, please choose one:
- New York, NY
- Los Angeles, CA
- Chicago, IL
- Houston, TX
- Phoenix, AZ
- Philadelphia, PA
- San Antonia, TX
- San Deigo, CA
- Dallas, TX
- San Jose, FL
    
