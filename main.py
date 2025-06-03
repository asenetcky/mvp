import os

import polars as pl
from sodapy import Socrata

APP_TOKEN = os.environ["APP_TOKEN"]


def main():
    with Socrata("data.ct.gov", APP_TOKEN) as client:
        results = client.get("qhtt-czu2", limit=10, offset=20)
        lf = pl.LazyFrame(results)
        print(lf.collect())


if __name__ == "__main__":
    main()
