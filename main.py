from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime, timedelta
import time

# Load environment variables from .env file
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Set up Chrome options
options = Options()
options.binary_location = "Change with your chrome app file"

# Set up the Chrome WebDriver service
service = Service('change path webdriver file')  # Make sure this path is correct
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# Initialize the driver
driver = webdriver.Chrome(service=service, options=options)
# Open the Loyverse login page
login_url = 'https://r.loyverse.com/#/'  # Update this if it's not the correct login URL
driver.get(login_url)

# Wait for the login page to load
wait = WebDriverWait(driver, 30)

# Find and fill in the login form
email_input = wait.until(EC.presence_of_element_located((By.ID, 'mat-input-0')))
password_input = wait.until(EC.presence_of_element_located((By.ID, 'mat-input-1')))
email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)
# Submit the form
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
login_button.click()

# Wait for the dashboard to load
wait.until(EC.url_contains('dashboard'))

# Calculate date range for the last 30 days
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

# Format the URL with the calculated date range
url = f'https://r.loyverse.com/dashboard/#/report/goods?page=0&limit=10&chart=bar&group=day&periodName=lastThirty&periodLength=30d&from={start_date.strftime("%Y-%m-%d")}%2000:00:00&to={end_date.strftime("%Y-%m-%d")}%2023:59:59&fromHour=0&toHour=0&outletsIds=all&merchantsIds=all'

# Navigate to the report page
driver.get(url)

# Wait for the report to load
time.sleep(10)  # You might need to adjust this

# Extract table data
items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.report-item-title')))
categories = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item[ng-if="tableConfig.category"] div')))
items_sold = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item[ng-if="tableConfig.saleQuantity"] span')))
net_sales = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item[ng-if="tableConfig.profitSum"] span')))
cost_of_goods = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item[ng-if="tableConfig.primeCost && displayCost"] span')))
gross_profit = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.item[ng-if="tableConfig.grossProfit && displayCost"] span')))

# Define lists to hold table data
data = {
    'Item': [item.text.strip() for item in items],
    'Category': [category.text.strip() for category in categories],
    'Items sold': [item_sold.text.strip() for item_sold in items_sold],
    'Net sales': [net_sale.text.strip() for net_sale in net_sales],
    'Cost of goods': [cost_of_good.text.strip() for cost_of_good in cost_of_goods],
    'Gross profit': [gross_pro.text.strip() for gross_pro in gross_profit]
}

# Close the WebDriver
driver.quit()

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('loyverse_data.xlsx', index=False)

print("Data scraped and saved to loyverse_data.xlsx")
