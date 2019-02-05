from shared.madrunner import run_mad_anom_detection
from shared.percentilerunner import (run_percentile_detection, run_percentile_detection_flow)
from shared.madflowrunner import run_mad_anom_detection_flow

SAMPLE_FILE_PATH = './data/santaba-demo4.csv'

import sys
import getopt
def main():
    algo_type = 'mad'

    opts, args = getopt.getopt(sys.argv[1:], 'a:', ['algo'])
    for opt_name, opt_value in opts:
        if opt_name in ('-a', '--algo'):
            algo_type = opt_value

    plt = None

    sw = timer.Timer()
    sw.start()
    if algo_type == 'mad':
        run_mad_anom_detection(SAMPLE_FILE_PATH)
    elif algo_type == 'mad_flow':
        run_mad_anom_detection_flow(SAMPLE_FILE_PATH)
    elif algo_type == 'percentile_flow':
        run_percentile_detection_flow(SAMPLE_FILE_PATH)
    else:
        run_percentile_detection(SAMPLE_FILE_PATH)

main()
