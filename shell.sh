# added 
jenkins    ALL = NOPASSWD: ALL
# to sudoers of my GCE


sudo apt-get install python3
sudo apt-get install python3-pip

pip3 install virtualenv
python3 -m venv venv
venv/Scripts/activate

pip3 install flask
python -m pip install --upgrade pip
pip3 install -r requirements.txt
pip3 install pylint
pip3 install pytest

pylint --rcfile ..filename.cfg pythonfile.py
python -m unittest tests/tets_routes.py
pip3 freeze > requirements.txt
 