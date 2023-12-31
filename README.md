# basic_chatgpt_python
 - basic_chatgpt_python
 
This code is a Python script that expains simple work with the OpenAI GPT-3.5 language model, specifically using the "gpt-3.5-turbo" variant. In the first part (LEVEL1), it sets up the API key required for making requests to the OpenAI API. This involves loading necessary libraries such as OpenAI, tiktoken, and dotenv, and setting the API key as an environment variable. Then, it defines a function called get_response that takes a user prompt, sends it to the GPT-3.5 model, and retrieves a response from the model. In this example, it asks a question about Barack Obama's age using the get_response function.

In the second part (LEVEL2), the code expands upon the interaction by defining a more complex get_response_complex function that allows for multi-message conversations. It can take a list of messages, including user and system roles, and interact with the model in a chat-like manner. In this example, it sets up a conversation where the user role asks for business advice about startup advertising in the style of Paul Graham. It then prints the model's response and token statistics (such as prompt tokens, completion tokens, and total tokens) obtained from the OpenAI API response.

Here is an article that explains things in a bit more detail here: https://pjstackdev.substack.com/p/getting-started-quickly-with-gpt
