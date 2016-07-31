import yaml
import subprocess
import sys
import shlex
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", default='.pipeline.yml',
                  help="Parse pipeline from FILE", metavar="FILE")
parser.add_option("-b", "--branch", dest="branch", default='default',
                  help="Parse pipeline for branch BRANCH", metavar="BRANCH")

(options, args) = parser.parse_args()

with open(options.filename, 'r') as pipeline_config:
    pipeline = yaml.load(pipeline_config)

    steps = []

    if options.branch in pipeline['pipelines'].keys():
        steps = pipeline['pipelines'][options.branch]
        print "Starting pipeline for %s" % (options.branch)
    else:
        print "Starting pipeline for Default"
        steps = pipeline['pipelines']['default']
    i = 1
    for step in steps:
        # print step
        if 'name' in step.keys():
            print "==============================="
            print "== Step %s: %s" % (i, step['name'])
            print "==============================="

        # check if we have a list of steps
        if not isinstance(step['script'], basestring):
            script = ';'.join(step['script'])
        else:
            script = step['script']

        p = subprocess.Popen(script, shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  stdin=subprocess.PIPE)
        out, err = p.communicate()
        if out.strip() != "":
            print out
        if err.strip() != "":
            print err
        if p.returncode != 0:
            sys.exit(p.returncode)

        i += 1

print "==============================="
print "======== PIPELINE DONE ========"
print "==============================="
sys.exit(0)