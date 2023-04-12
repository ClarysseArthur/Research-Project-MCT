# Research-Project-MCT
Traffic lights optimized using DQN

# Installation
## Anaconda
I used [Anacoda](https://www.anaconda.com/) for the virtual environment. The easiest way to install all the packages is through Anaconda. Download the installer and follow the installation steps through the Anaconda website [anaconda.com/](https://www.anaconda.com/). Run the application after it is successfully installed.

![Anaconda startpage](https://raw.githubusercontent.com/ClarysseArthur/Research-Project-MCT/main/rm_assets/Picture1.png?raw=true)

Once Anaconda is started, import "anaconda_env.yml" via the environments tab. If everything succeeded, "IntersectionEnv" will be in the list of environments.

## Jupyter Notebook
The best way to work with Jupyter notebook is through Visual Studio Code. Start installing Visual Studio Code by following the steps on the website https://code.visualstudio.com/. Once Visual Studio Code is successfully installed, launch the program and go to the extensions tab. Using the search bar, search for "Jupyter". Install the official extension issued by Microsoft. 

![Jupyter extension in VS Code](https://raw.githubusercontent.com/ClarysseArthur/Research-Project-MCT/main/rm_assets/Picture2.png?raw=true)

After installation, you can open and run "DemoTraining.ipynb" in VS Code. Don't forget to choose the correct environment (IntersectionEnv) at the top right.

![DemoTraining.ipynb in VS Code](https://raw.githubusercontent.com/ClarysseArthur/Research-Project-MCT/main/rm_assets/Picture3.png?raw=true)

## Single file
To run a pre-made intersection from a Python file, copy the Complex.py or Simple.py file to /Environment and run `python Complex.py` in the anaconda environment.

# 3D render
In the Render_3d.py file is class defined with a list of approaches and exits as parameters. It automatically  calculates how many lanes each side has and stores it in `lanes_length[]`. 