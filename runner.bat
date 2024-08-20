@ECHO OFF
pip3 install -r requirements.txt
pytest .\TestCases\test_flipkart_product_search.py --alluredir="./allureReports/
allure serve allureReports