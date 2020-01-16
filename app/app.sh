#!/bin/sh

pip install bottle==0.12.18 psycopg2==2.8.4 redis==2.10.6
python -u sender.py
