from selenium import webdriver


def test_litecart_admin_login():
    driver = webdriver.Firefox()
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_class_name('btn.btn-default').click()

    driver.implicitly_wait(5)
    links = driver.find_elements_by_css_selector("li[id='app-']")
    for i in range(len(links)):
        links = driver.find_elements_by_css_selector("li[id='app-']")
        links[i].click()
        sublinks = driver.find_elements_by_css_selector(".docs li")
        if len(sublinks) != []:
            for s in range(len(sublinks)):
                sublinks = driver.find_elements_by_css_selector(".docs li")
                sublinks[s].click()
                assert len(driver.find_elements_by_tag_name('h1')) == 1
        else:
            assert len(
                driver.find_elements_by_tag_name('h1')) == 1

    driver.quit()
