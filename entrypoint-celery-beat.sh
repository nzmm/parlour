#!/bin/bash

echo "Starting celery beat..."
celery -A totallywired beat --loglevel=INFO