#!/usr/bin/env python
import os
import sys
import NLP.sentiment_analyser.sentiment_analyser
from NLP.sentiment_detector.sentiment_detector_nb import tweet_contains_sentiment

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
