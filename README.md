This repo has two main scripts, data_acquisition.py and data_prep.py, which fetch and prepare NFL data for future analysis intended to study the tendencies of team play calling on 4th down. 

This data comes from an incredibly detailed database at Pro Football Focus, a company recently acquired by TeamWorks. The API key to access this data is exclusive to select B2B partners, such as BYU's football team. The general manager gave us permission to use this specific data for our project, but due to the terms and conditions of this api key, we cannot publish the data on any public area, such as github. 

The data_acquisition.py script has two functions other than the main() function. The first exchanges the api key with a temporary jwt token, and the second exchanges this token, accepts a designated year, and fetches the detailed play by play data at it's designated endpoint. I will not publish the api documentation. Out of an abundance of caution, I designed the data acquisition script to only make one call at a time, accepting the desired year as an unput from the command line. I did not want to get rate limited or cause any issues with PFF on behalf of BYU's football team, where this key is shared by many departments. 

The second script, data_prep.py, combines all the data into one csv, filters the data to the down of interest, and performs transformations that prepare the data for further analysis of our research question. 

The resulting data set is a 15145 x 41 dimentional data set with columns:

'down', 'penalty', 'hash', 'sort_order', 'week', 'season', 'offense',
'defense', 'home_team', 'away_team', 'game_id', 'play_id', 'quarter',
'field_position', 'distance', 'clock', 'ball_carrier', 'tackle',
'kicker', 'penalty_yards', 'defense_score', 'gain_loss_net',
'game_date', 'offense_score', 'special_teams_type', 'gsis_play_id',
'away_special_team_sort_order', 'gsis_game_key',
'home_special_team_sort_order', 'drive_end_event', 'drive',
'drive_play', 'run_pass', 'personnel_basic', 'pass_result', 'passer',
'touchdown', 'home_asset_guid', 'home_media_element_id',
'home_play_guid', 'go_for_it'