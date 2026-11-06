import re
from pathlib import Path
import pandas as pd

def combine_csvs(pattern, files):
    years = set()
    for f in files:
        match = pattern.search(f.name)
        if match:
            years.add(int(match.group(1)))

    frames = []
    for f in files:
        match = pattern.search(f.name)
        if not match:
            continue
        year = int(match.group(1))
        if year in years:
            years.remove(year)
            df = pd.read_csv(f)
            df["season"] = year
            frames.append(df)

    combined = pd.concat(frames, ignore_index=True)

    return combined

def filter_and_clean(combined):
    fourth = combined[
        (combined['down'] == 4) & (combined['special_teams_type'] != 'PRE-SNAP PENALTY')
        ].copy()
    fourth['go_for_it'] = (
        ~fourth['special_teams_type'].isin(['PUNT', 'FIELD GOAL'])
    ).astype(int)

    return fourth


def __main__():
    data_dir = Path("data/raw")
    pattern = re.compile(r"nfl_(\d{4})_plays\.csv$")
    files = sorted(data_dir.rglob("nfl_*_plays.csv"))

    combined = combine_csvs(pattern, files)
    fourth = filter_and_clean(combined)

    Path('data/processed').mkdir(parents=True, exist_ok=True)
    fourth.to_csv("data/processed/data_complete.csv", index=False)

if __name__ == __main__():
    __main__()