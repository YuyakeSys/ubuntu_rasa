# ubuntu_rasa
Local developing environment: i7-7700Khq GTX1060 6g 24G RAM <br>
There are two ways for deploying: local mode and docker-compose <br>
Cloud Environment:  Ubuntu 20.04 <br>
Local mode <br>
1st Set up rasa, we recommend using virtual environment install venv and create the virtual environment. Then source ./venv/bin/activate<br>
Pip 3 install rasa<br>
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple<br>
Then deploy the mySQL database for query<br>
Sudo apt-get install mysql<br>
Pip3 install pymysql<br>
For local mode it requires software like ngrok, so <br>
Sudo apt-get install snap<br>
Snap ngrok<br>
Ngrok http 5005(your rasa run protocol)<br>
Rasa run actions<br>
Then do rasa run to run the code.<br>
Docker-compose<br>
First get rasa x<br>
curl -sSL -o install.sh https://storage.googleapis.com/rasa-x-releases/0.42.5/install.sh<br>
sudo bash ./install.sh<br>
cd /etc/rasa<br>
sudo docker-compose up -d<br>
In this way, you require to do the certbot or other software for SSL.<br>
Then you can deploy your custom action server, see here for a guide
https://sundayposts.sundaybots.com/rasa/2020/11/30/Deploying-RASA-X-on-server-with-Docker-Compose.html#manually-building-action-server
Lastly, connect your domain name to you server.
