from __future__ import print_function
import metrics

def add(old, new):
    return int(old) + int(new)

def max_metric(old, new):
    return max(int(old), int(new))

def latest(_old, new):
    return new

def no_update(old, _new):
    return old

combine_fns = {
    "metric1": latest,
    "metric2": max_metric,
    "metric4": latest,
}

"""
new metrics should be in the following form:
{
  "name1": {"metric1": 1, "metric2": 134, "metric3": 11}
  "name2": {"metric1": 2, "metric3": 8}
  "name3": {"metric2": 412}
}
"""
def main():
    new_metrics = {"user3": {"metric1": 100, "metric4": 11}}
    metrics.upload_new_metrics("Week1Metrics", combine_fns, new_metrics)

if __name__ == '__main__':
    main()
