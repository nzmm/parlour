#!/bin/bash

echo "Starting celery worker..."
celery -A totallywired worker --loglevel=INFO