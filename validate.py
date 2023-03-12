import re
import sys
import yaml

def is_valid_rule(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

if __name__ == '__main__':
    failed = 0
    with open('src/filters.yaml', 'r') as f:
        filters = yaml.safe_load(f.read())['filters']
        for filter in filters:
            id = filter['id']
            if not is_valid_rule(filter['rule']):
                print('[%d] FAILED!' % id)
                failed += 1
    sys.exit(failed)
