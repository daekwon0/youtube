import csv
from datetime import datetime as dt

comments = []
#make sure that the date is up to date, and is formatted nicely
today = dt.today().strftime('%d-%m-%Y')

def process_comments(response_items, csv_output = False):
    for res in response_items:
        #handle replies
        if 'replies' in res.keys():
            for reply in res['replies']['comments']:
                comment = reply['snippet']
                comment['commentId'] = reply['id']
                comments.append(comment)
        #handle non-replies
        else:
            comment = {}
            comment['snippet'] = res['snippet']['topLevelComment']['snippet']
            comment['snippet']['parentId'] = None
            comment['snippet']['commentId'] = res['snippet']['topLevelComment']['id']
            
            comments.append(comment['snippet'])
    
    if csv_output:
        make_csv(comments)
    
    print(f'Finished processing {len(comments)} comments.')
    return(comments)

def make_csv(comments, channelID = None):
    header =  comments[0].keys()
    
    if channelID:
        filename = f'comments+{channelID}_{today}.csv'
    else:
        filename = f'comments_{today}.csv'

    #csv creation is simple, utf8 to get rid of emojis and non-English characters
    with open(filename, 'w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(comments)
    
