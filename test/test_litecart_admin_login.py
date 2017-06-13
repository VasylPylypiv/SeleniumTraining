from selenium import webdriver


def test_litecart_admin_login():
    driver = webdriver.Firefox()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_class_name('btn.btn-default').click()
    driver.quit()
