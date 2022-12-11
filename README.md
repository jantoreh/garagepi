# TuftCam

## Install

```bash
pip3 install -r requirements.txt
```

## Launch app

Run from project root:

```bash
python3 app.py
```

## Crontab

To ensure the endpoint is up and running also after power loss etc, add the `start_server` script as a `cron` job. Open the configuration file with `crontab -e` and add: `*/15 * * * * /home/pi/garagepi/scripts/start_server.sh` to ensure that the server is checked for life signs every 15 minutes.
