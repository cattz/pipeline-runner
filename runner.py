import yaml
import subprocess
import sys
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
        print "Starting pipeline for {}".format(options.branch)
    else:
        print "Starting pipeline for Default"
        steps = pipeline['pipelines']['default']

    for step in steps:
        print "==============================="
        print "== Step: {}".format(step['name'])
        print "==============================="

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

print "Pipeline DONE"
sys.exit(0)
