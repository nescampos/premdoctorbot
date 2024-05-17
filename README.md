# Prem Doctor

Prem Doctor is a web app built with Python, [Streamlit](https://streamlit.io/), and [Snowflake Arctic](https://www.snowflake.com/en/data-cloud/arctic/) to allow simple medical consultations before attending a doctor. **Prom Doctor does not store the data, giving users greater confidence and security.**

The idea of this project is to save people time and money and to know which doctor to see in case of a medical problem they have.

## Licence
[MIT](./LICENCE)

## How works

1. Create a [Replicate](https://replicate.com/) account and get an API key.
2. Install [Streamlit](https://streamlit.io/) or use Streamlit Cloud.
3. Install all libraries in [requirements.txt](./requirements.txt).
4. Add these secrets in Streamlit:
   - _REPLICATE_API_TOKEN_: The API key from Replicate (step 1)
   - _max_tokens_: The maximum number of tokens allow for the question. 
5. Run the web app (in Streamlit Cloud just wait to compile automatically).

Created by [Néstor Nicolás Campos Rojas](https://www.linkedin.com/in/nescampos/)
