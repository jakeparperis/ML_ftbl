from statsbombpy import sb
import pandas as pd
import statsbomb_ids as ids

pd.set_option('display.max_rows', 500)

comps = sb.competitions()
print(comps[['competition_id', 'competition_name', 'season_id', 'season_name']])



