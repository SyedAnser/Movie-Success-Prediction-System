from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to the app
    driver.get("http://localhost:3000")  # Ensure your React app is running locally
    
    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "content"))
    )

    # Step 2: Fill out the form fields
    # form_data = {
    #     "popularity": "85",
    #     "vote_count": "3500",
    #     "vote_average": "8.2",
    #     "budget": "160",
    #     "runtime": "150",
    #     "genres": "Action, Sci-Fi",
    #     "production_companies": "Warner Bros, Legendary Pictures",
    #     "release_month": "7",  # July
    # }
    form_data = {
    "popularity": random.uniform(0, 100),
    "vote_count": random.randint(0, 10000),
    "vote_average": random.uniform(0, 10),
    "budget": random.randint(0, 500),
    "runtime": random.randint(60, 240),
    "genres": ["Action", "Drama", "Comedy", "Sci-Fi"][random.randint(0, 3)],
    "production_companies": ["Warner Bros", "Disney", "Universal"][random.randint(0, 2)],
    "release_month": random.randint(1, 12),
}

    # Fill inputs
    for field, value in form_data.items():
        if field == "release_month":
            # Select dropdown for release month
            dropdown = driver.find_element(By.ID, field)
            dropdown.click()
            option = dropdown.find_element(By.XPATH, f'//option[@value="{value}"]')
            option.click()
        else:
            # Input fields
            input_field = driver.find_element(By.ID, field)
            input_field.clear()
            input_field.send_keys(value)

    # Step 3: Submit the form
    submit_button = driver.find_element(By.CLASS_NAME, "predict-button")
    submit_button.click()

    # Step 4: Wait for the prediction result
    prediction_result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "prediction-result"))
    )

    # Verify and print the result
    print(f"Prediction Result: {prediction_result.text}")

    # Verify error case (optional)
    # driver.find_element(By.ID, "vote_count").clear()
    # driver.find_element(By.ID, "vote_count").send_keys("-10")
    # submit_button.click()
    # error_message = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
    # )
    # print(f"Error Message: {error_message.text}")

finally:
    # Close the browser
    driver.quit()
