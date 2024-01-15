<<<<<<< HEAD
* sudo pip3 install jupyter    
* jupyter notebook --generate-config
* 修改 ~/.jupyter/jupyter_notebook_config.py 找到 
* #c.NotebookApp.ip = ‘localhost' 
*
* 改成 

* c.NotebookApp.ip = '0.0.0.0’ 
##
* $ jupyter notebook password
* ip -I
* $ jupyter notebook
* http://<ip>:8888
=======
* sudo pip3 install jupyter    
* jupyter notebook --generate-config
* 修改 ~/.jupyter/jupyter_notebook_config.py 找到 
* #c.NotebookApp.ip = ‘localhost' 
*
* 改成 

* c.NotebookApp.ip = '0.0.0.0’ 
##
* $ jupyter notebook password
* ip -I
* $ jupyter notebook
* http://\<ip\>:8888
##
```
python3 -m pip install ipykernel
python3 -m ipykernel install --user --name=cv
pip3 install jupyterlab
## verify
jupyter lab --allow-root --ip=0.0.0.0 --no-browser
sudo apt-get install nodejs
node -v
npm -v
pip install jupyterhub
jupyter lab build
jupyter lab --allow-root --ip=0.0.0.0 --no-browser
mkdir -p /home/$USER/Dev/jupyterlab
export WorkingDirectory=/home/$USER/Dev/jupyterlab
```
### Create service
```
cat << EOF | sudo tee /etc/systemd/system/jupyter-lab.service
[Unit]
Description=Jupyter Lab
[Service]
Type=simple
PIDFile=/run/jupyter.pid
ExecStart=/home/$USER/.local/bin/jupyter-lab --config=/home/$USER/.jupyter/jupyter_notebook_config.py
WorkingDirectory=$WorkingDirectory
User=$USER
Group=$USER
Restart=always
RestartSec=10
#KillMode=mixed
[Install]
WantedBy=multi-user.target
EOF
```
### Enable service
```
sudo systemctl daemon-reload
sudo systemctl enable jupyter-lab.service
sudo systemctl start jupyter-lab.service
sudo systemctl status jupyter-lab.service
```
