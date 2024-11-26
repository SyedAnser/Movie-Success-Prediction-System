from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

# Set up the WebDriver
driver = webdriver.Chrome()  # Replace with the driver for your browser

try:
    # Start by navigating to the API endpoint
    driver.get('http://127.0.0.1:5000/predict')  # Flask endpoint

    # Interact with the API
    input_data = {
        "level_0": 1,
        "popularity": 5.0,
        "budget": 1000000,
        "runtime": 120,
        "vote_average": 7.5,
        "vote_count": 200,
        "release_month": 7,
        "genres": ["Action", "Adventure"],
        "production_companies": ["Warner Bros"]
    }

    # Send a POST request using JavaScript execution (for testing)
    script = f'''
    fetch('http://127.0.0.1:5000/predict', {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify({json.dumps(input_data)})
    }})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
    '''
    driver.execute_script(script)

    # Wait for the response to appear in the console (simulate API response check)
    time.sleep(3)  # Adjust delay as needed

    # Check the browser console for the prediction result
    logs = driver.get_log('browser')
    print("Logs from browser console:")
    for entry in logs:
        print(entry)

except Exception as e:
    print(f"An error occurred during the test: {e}")

finally:
    # Close the browser
    driver.quit()

