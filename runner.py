import yaml
import subprocess
import sys

filename = '.pipeline.yml'
branch = 'default'

with open(filename, 'r') as pipeline_config:
    pipeline = yaml.load(pipeline_config)

    steps = []

    if branch in pipeline['pipelines'].keys():
        steps = pipeline['pipelines'][branch]
    else:
        steps = pipeline['pipelines']['default']

    for step in steps:
        print "- {}".format(step['name'])

        p = subprocess.Popen(step['script'], shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  stdin=subprocess.PIPE)
        out, err = p.communicate()
        if out.strip() != "":
            print out
        if err.strip() != "":
            print err
        if p.returncode != 0:
            sys.exit(p.returncode)

print "DONE"
sys.exit(0)
