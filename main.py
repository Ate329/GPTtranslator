# Import necessary libraries
import openai
import tkinter as tk

# Initialize API key variable
api_key = ""


# Initialize API key variable
def api_window():
    global api_key
    api_key = entry.get()
    if window:
        window.destroy()


# Create GUI window for API key input
window = tk.Tk()
window.title("API key")
window.geometry("200x135")

# Add label and entry field for API key input
label = tk.Label(window, text="Enter api key")
label.pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=10)

# Add button to submit API key
button = tk.Button(window, text="Enter", command=api_window)
button.pack(pady=10)

# Run GUI window
window.mainloop()

# Set OpenAI API key
openai.api_key = api_key


# Function to translate text using OpenAI API
def translate_text(text, model_engine, target_language):
    prompt = f"translate '{text}' into {target_language}"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    translation = response.choices[0].text.strip()
    return translation


# List of available OpenAI engines
available_engines = ["text-davinci-003", "text-babbage-001", "text-curie-001", "gpt-3.5-turbo", "text-ada-001", "gpt-4"]

# Dictionary of engine descriptions
engine_descriptions = {
    "text-davinci-003": "Most capable GPT-3 model. Can do any task the other models can do, often with higher quality.",
    "text-babbage-001": "Capable of straightforward tasks, very fast, and lower cost.",
    "text-curie-001": "	Very capable, faster and lower cost than Davinci(Sometimes not working, no idea why)",
    "gpt-3.5-turbo": "Most capable GPT-3.5 model and optimized for chat at 1/10th the cost of text-davinci-003(currently not working).",
    "text-ada-001": "Capable of very simple tasks, usually the fastest model in the GPT-3 series, and lowest cost(currently not working).",
    "gpt-4": "More capable than any GPT-3.5 model, able to do more complex tasks, but very expensive"
}

# Print the available engines and their descriptions
print("Available engines:")
for i, engine in enumerate(available_engines, start=1):
    print(f"{i}. {engine} - {engine_descriptions.get(engine, 'No description available')}")

# Loop to select OpenAI engine
while True:
    try:
        engine_choice = int(input("Select an engine by number: ")) - 1
        if engine_choice < 0 or engine_choice >= len(available_engines):
            raise ValueError("Invalid engine number")
        model_engine = available_engines[engine_choice]
        break
    except ValueError as e:
        print(e)
        print("Please enter a valid engine number.")

# Loop to translate text and allow user to change engine
while True:
    try:
        text_to_translate = input('Input the text you want to translate: ')
        target_language = input('Input the target language: ')
        translated_text = translate_text(text_to_translate, model_engine=model_engine, target_language=target_language)
        print(translated_text)

        change_engine = input("Do you want to change the model engine? (yes/no): ")
        if change_engine.lower() == "yes":
            while True:
                try:
                    engine_choice = int(input("Select an engine by number: ")) - 1
                    if engine_choice < 0 or engine_choice >= len(available_engines):
                        raise ValueError("Invalid engine number")
                    model_engine = available_engines[engine_choice]
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid engine number.")
        elif change_engine.lower() == "no":
            continue
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    except KeyboardInterrupt:
        print("Translation stopped by user")
        break
