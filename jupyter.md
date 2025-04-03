安裝:
安裝步驟 1:
在終端中輸入以下內容：(如果已經有安裝過的可以略過)
```
sudo apt-get update
sudo apt-get install python3-matplotlib
sudo apt-get install python3-scipy
sudo apt install libffi-dev
sudo pip3 install cffi
sudo reboot
pip3 install — upgrade pip
```
安裝步驟 2:
Raspberry Pi通常使用SD卡作為儲存，他們沒有電腦那麼多的空間。下命令來清理為更新Raspberry Pi而下載的軟件包。
```
sudo apt-get clean
```
安裝步驟 3:
Raspian的最新版本用Chromium（Chrome瀏覽器的開源版本）代替了Epiphany Web瀏覽器。下命令要將Chromium設置為稍後用於IPython筆記本的默認瀏覽器。
```
sudo update-alternatives — config x-www-browser
sudo reboot
```
測試:
從終端發出以下命令來啟動IPython。
```
jupyter-notebook
```
