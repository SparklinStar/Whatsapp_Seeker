import streamlit as st
import helper
import preprocessor
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Whatsapp Seeker")
st.text("A tool to analyse your whatsapp chats.")
st.text("Just upload the exported chat as txt file.")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    st.dataframe(df)

    #fetching users unique
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"overall")

    selected_user = st.selectbox("Show Analysis wrt",user_list)

    if st.button("Show Analysis"):
        num_messages,words,media,poll,link = helper.fetch_stats(selected_user,df)

        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total words")
            st.title(words)
        with col3:
            st.header("Total media")
            st.title(media)
        with col4:
            st.header("Total Polls")
            st.title(poll)
        with col5:
            st.header("Total Links")
            st.title(link)
        if selected_user =='overall':
            st.title('Most Busy User')
            x,new_df=helper.most_busy_users(df)
            fig,ax = plt.subplots()

            col1,col2=st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation="vertical")
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        # monthly timeline

        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)


        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)



        #wordcloud
        st.title("WorldCloud")
        df_wc = helper.create_worldcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)





        col1,col2 =st.columns(2)
        # most common words
        with col1:
            st.header("Word counter")
            most_common_df=helper.most_common_words(selected_user,df)
            st.dataframe(most_common_df)

        #emoji counter
        with col2:
            st.header("Emoji counter")
            emoji_df = helper.emoji_helper(selected_user,df)
            st.dataframe(emoji_df)
