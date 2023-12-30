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
python3 -m ipykernel install --user --name=cv

```
