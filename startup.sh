#!/bin/sh
gunicorn --workers=5 --bind=0.0.0.0:5000 --access-logfile - --error-logfile - 'run:app'
