import re
import pandas as pd


def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[ap]m\s-\s'
    pattern2= '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    match_12_hour = re.search(pattern, data)
    if match_12_hour:
        pattern3='\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s-\s'
        check= re.search(pattern3, data)
        if check:
            messages = re.split(pattern, data)[1:]
            dates = re.findall(pattern, data)
            df = pd.DataFrame({'user_message': messages, 'message_date': dates})
            df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %I:%M %p - ')
            df.rename(columns={'message_date': 'date'}, inplace=True)
        else:
            messages = re.split(pattern, data)[1:]
            dates = re.findall(pattern, data)
            df = pd.DataFrame({'user_message': messages, 'message_date': dates})
            df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p - ')
            df.rename(columns={'message_date': 'date'}, inplace=True)

    match_24_hour = re.search(pattern2, data)
    if match_24_hour:
        pattern4= '\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s-\s'
        check2 = re.search(pattern4, data)
        if check2:
            messages = re.split(pattern2, data)[1:]
            dates = re.findall(pattern2, data)

            df = pd.DataFrame({'user_message': messages, 'message_date': dates})
                # convert message_date type
            df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')

            df.rename(columns={'message_date': 'date'}, inplace=True)
        else:
            messages = re.split(pattern2, data)[1:]
            dates = re.findall(pattern2, data)

            df = pd.DataFrame({'user_message': messages, 'message_date': dates})
            # convert message_date type
            df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ')

            df.rename(columns={'message_date': 'date'}, inplace=True)
    users = []
    messages = []
    for data in df['user_message']:
        user_message = data.split(':', 1)
        if len(user_message) == 2:
            user = user_message[0]
            message = user_message[1].strip()
            users.append(user)
            messages.append(message)
        else:
            users.append('group_notification')
            messages.append(data)

    # Create a DataFrame from the extracted data
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['only_date'] = df['date'].dt.date

    return df
