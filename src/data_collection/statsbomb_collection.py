from statsbombpy import sb
import pandas as pd

pd.set_option('display.max_rows', 500)

comp_ids = {
    'UCL': 16,
    'Bundesliga': 9,
    'Ligue 1': 7,
    'Premier League': 2
}

season_ids_ligue1 = {
    '22/23': 235,
    '21/22': 108,
    '15/16': 27,
}

comps = sb.competitions()
print(comps[['competition_id', 'competition_name', 'season_id', 'season_name']])



