import pandas as pd
import os
import re

# Get directory structure right for Visual Studio project
HERE = os.path.dirname(__file__)
DATA = os.path.abspath(os.path.join(HERE, '..', 'data'))

def extract_digits(code):
    result = re.findall(r"[0-9]+", code)
    if not result:
        print("Problem:", code)
        return None
    return result[0]

def extract_letters(code):
    result = re.findall(r"[A-Z]+", code)
    return result[0] if result else None

def preprocess(
    raw_csv=os.path.join(DATA, 'stations.csv'),
    out_csv=os.path.join(DATA, 'processed_stations.csv')
):
    # Load original data
    data = pd.read_csv(raw_csv)

    # Build simplified features DataFrame
    feats = pd.DataFrame({
        'name': data['STN_NAME'],
        'code': data['STN_NO']
    })

    # Duplicate rows where a station belongs to multiple lines
    rows = feats.values.tolist()
    extras = []
    for name, code in feats.values:
        parts = code.split('/')
        if len(parts) > 1:
            rows[rows.index([name, code])][1] = parts[0]
            for p in parts[1:]:
                extras.append([name, p])
    rows += extras

    # Build final DataFrame
    df = pd.DataFrame(rows, columns=['name', 'code'])
    df['line'] = df['code'].apply(extract_letters)
    df['num'] = df['code'].apply(extract_digits)

    # Drop bad rows (no line or no num)
    df = df.dropna(subset=['line', 'num'])
    df['num'] = pd.to_numeric(df['num'], downcast='integer')

    # Remove bus lines (BP)
    df = df[df['line'] != 'BP'].reset_index(drop=True)

    # Sort alphabetically by station name to match professor's file
    df = df.sort_values(['name'], ascending=True)

    # Save to file
    df.to_csv(out_csv, index=False)
    print(f"Processed {len(df)} stations to: {out_csv}")
    return df

if __name__ == '__main__':
    preprocess()
