
# Chatbot for Food Delivery App using Dialogflow

Welcome to the Chatbot for Food Delivery App project! This chatbot is designed to enhance the user experience of your food delivery application by providing a conversational interface powered by Dialogflow. With custom entity recognition for food names, a FastAPI backend, and MySQL database integration for orders and menu management, this project aims to streamline the ordering process for your users.

## Features

- **Dialogflow Integration**: Seamlessly interacts with users using Dialogflow's natural language processing capabilities.
- **Custom Entity Recognition**: Enhances accuracy in identifying food items through custom entities.
- **FastAPI Backend**: Provides a robust and high-performance backend solution.
- **MySQL Database**: Stores and manages orders, order tracking, and the food menu efficiently.
- **Secure Tunneling with Ngrok**: Enables secure communication by converting HTTP to HTTPS.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Aftabmallick/chatbot-for-food_delivery-app-using-dialogflow.git
```

2. Install dependencies:

```bash
cd chatbot-for-food_delivery-app-using-dialogflow
pip install -r requirements.txt
```

3. Set up MySQL database:
   - Create a MySQL database and update the database configuration in `config.py`.

4. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

5. Set up Ngrok for secure tunneling:
   - Download and install Ngrok from [https://ngrok.com/](https://ngrok.com/).
   - Start Ngrok to expose your local server:

```bash
./ngrok config add-authtoken <authtoken>
```

```bash
./ngrok http 8000
```

6. Update the Ngrok HTTPS URL in Dialogflow fulfillment settings.

## Usage

- Integrate the chatbot into your food delivery application.
- Users can interact with the chatbot to place orders, track orders, and explore the menu.
- The chatbot utilizes custom entities to accurately recognize food names, providing relevant responses to user queries.

## Contributors

- [Aftab Mallick](https://github.com/Aftabmallick)



## Acknowledgements

- Special thanks to the developers of Dialogflow, FastAPI, MySQL, and Ngrok for providing powerful tools and technologies for building this project.



