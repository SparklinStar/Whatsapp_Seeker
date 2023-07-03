# Whatsapp Seeker - Analyze Your Whatsapp Chats

[WhatsApp Seeker]
Deployed at [streamlit](https://whatsapp-seeker.streamlit.app/)
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Privacy](#data-privacy)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Whatsapp Seeker is a powerful tool that allows you to analyze your Whatsapp chats with ease. It takes an exported Whatsapp chat and converts it into a pandas DataFrame, enabling you to gain valuable insights from your conversations. The tool offers various visualizations, including monthly and daily timelines, emoji counts, the most popular words used, and word clouds. Whether you want to understand your own messaging habits or analyze group dynamics, Whatsapp Seeker has got you covered.

## Features

- Converts exported Whatsapp chat to a pandas DataFrame for easy analysis.
- Utilizes `matplotlib` and `seaborn` libraries to display monthly and daily timelines of your conversations.
- Counts the number of emojis used in the chat.
- Identifies the most popular words used in your chats.
- Uses the `urlextract` library to count the number of links shared in your conversations.
- Generates a word cloud representation of the most frequently used words.
- Works seamlessly on both group and individual chat levels.
- Deployed on Streamlit for a user-friendly experience.
- Ensures 100% data safety - no data is stored on the server.

## Installation

To use Whatsapp Seeker, follow these steps:

1. Clone this GitHub repository to your local machine.

```bash
git clone https://github.com/your-username/whatsapp-seeker.git
cd whatsapp-seeker
```

2. Install the required dependencies using `pip`.

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app.

```bash
streamlit run app.py
```

## Usage

1. Export your desired Whatsapp chat from the app.
2. Launch the Whatsapp Seeker Streamlit app using the steps mentioned in the Installation section.
3. Upload the exported chat file to the app.
4. Explore various visualizations and insights generated from your Whatsapp chat.

## Data Privacy

We take data privacy seriously. Whatsapp Seeker does not store any data on the server or any external databases. All processing and analysis are performed locally on your machine. Your chat data remains completely confidential and secure.

## Contributing

We welcome contributions to improve Whatsapp Seeker and add new features. To contribute, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name.
3. Make your desired changes and enhancements.
4. Test your changes thoroughly.
5. Create a pull request and describe the improvements you've made.

We'll review your contribution and merge it if it aligns with the project's goals.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as per the terms of the license.

---

Start exploring your Whatsapp conversations like never before! For any questions or feedback, please don't hesitate to reach out to us at souradip1000@gmail.com. Happy analyzing!
