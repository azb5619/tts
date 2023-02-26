import openai, os

openai.api_key = os.environ.get('OPENAI_API_KEY')


def generate_response(prompt):
    response = openai.Completion.create(
            engine='text-davinci-002',
            prompt=prompt,
            max_tokens=255,
            n=1,
            stop=None,
            temperature=.4
            )
    return response.choices[0].text.strip()

def __main__:
    text_string = input("question ")
    response = generate_response(text_string)
    print(response)

if __name__ == '__main__':
    main()
