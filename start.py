import time 
import groundlight 
from dotenv import load_dotenv
import os

def load_and_validate_api_key():
    """
    Loads the contents of the .env file into the environment,
    including your Groundlight API Token.
    Validates that the token is set correctly, and raises an error if not.
    """

    load_dotenv()

    api_token = os.getenv("GROUNDLIGHT_API_TOKEN")
    if not api_token or not api_token.startswith("api_"):
        raise ValueError(
            "The 'GROUNDLIGHT_API_TOKEN' is not set correctly in the .env file. "
            "It should start with 'api_'. You can create a token here: "
            "https://app.groundlight.ai/reef/my-account/api-tokens."
        )



def main():
    load_and_validate_api_key()
    while True:
        print("<wildlife> sending a dog image to Groundlight.")
        time.sleep(10)
    
    
if __name__ == "__main__":
    main()