# wienerlinien_api_mirror
Since the wiener linien api is rate limited I mirror it to a file every 10s to not get my servers IP banned.

## Getting started

Install Python3.8 (or higher)

Install all dependencies with:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Deployment

How we deploy this app on Ubuntu.

Install the requirements with:

```bash
sudo apt -y install python3-venv python3-pip
```

Create a virtual env with:

```bash
python3 -m venv venv
```

Edit all constants in main.py.

Open `wiener-linien-api-mirror.service` and edit all paths to the working
directory.

Start the systemd service with:

```bash
sudo cp wiener-linien-api-mirror.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable wiener-linien-api-mirror.service
sudo systemctl start wiener-linien-api-mirror.service
```

The service should now be up and running 🎉

To stop the service run:

```bash
sudo systemctl stop wiener-linien-api-mirror.service
```

To update the service to a new version (commit) run:

```bash
git pull
sudo systemctl restart wiener-linien-api-mirror.service
```
