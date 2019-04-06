from plistlib import writePlist
import os

PLIST_FILENAME = os.environ['HOME'] + '/Library/LaunchAgents/com.9gag.scraper.plist'

plist_content = dict(
    EnvironmentVariables=dict(
        PYTHONPATH="/Users/travis/virtualenvs/scraper/lib/python2.7/site-packages/",
    ),
    Label="com.9gag.scraper",
    ProgramArguments=["{}/scraping.py".format(os.getcwd())],
    StartInterval=10 * 60,
    RunAtLoad=True,
    StandardErrorPath='/tmp/mycommand.err'
)

with open(PLIST_FILENAME, 'w') as plist_file:
    writePlist(plist_content, plist_file)

