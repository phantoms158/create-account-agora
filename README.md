# create-account-agora
Auto create account agora

if you use ubuntu
step1: install pip
apt-get install python3-pip
step2: install lib
sudo pip3 install -r requirements.txt
step3: install chromedriver 
sudo apt-get install chromium-chromedriver

Adding the path to the selenium line 10 file python-selenium:

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


#### Run auto ####
python3 python-selenium
