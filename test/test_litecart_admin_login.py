from selenium import webdriver


def test_litecart_admin_login():
    driver = webdriver.Firefox()
    driver.get("http://demo.litecart.net/admin/login.php")
    driver.find_element_by_name('username').send_keys('demo')
    driver.find_element_by_name('password').send_keys('demo')
    driver.find_element_by_class_name('btn.btn-default').click()
    driver.quit()
