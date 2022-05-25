#!/bin/bash
#

FLASK_APP=Ce/Services/handler_requests.py flask run --port 8002 &
python3 main.py & python3 Core/Service/dashboard_log.py