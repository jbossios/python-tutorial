import argparse
import sys
import logging


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputFile', action='store', dest='input_file', default='', help='Input file')
    parser.add_argument('--enableSomething',action='store_true', dest='enable_something', default=False, help='Enable option to do something')
    args = parser.parse_args()

    logging.basicConfig(level='INFO',format='%(levelname)s: %(message)s')
    log = logging.getLogger()

    if not args.input_file:
        log.fatal('Missing --inputFile flag')
        parser.print_help()  # print help for each argument and exit
        sys.exit(1)

    if args.enable_something:
        log.info('Something was enabled')
    else:
        log.info('Something was not enabled')


if __name__ == '__main__':
    main()
