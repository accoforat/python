# -*- coding: utf-8 -*-
from asyncio import wait
from telnetlib import EC

from selenium import webdriver
import unittest, time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


class test_01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.driver.get("http://intgr-test-2.stage.erp.vseinstrumenti.net/")

    def test_01(self):
        driver = self.driver
        self.driver.get("http://intgr-test-2.stage.erp.vseinstrumenti.net/")
        driver.find_element_by_name("_username").click()
        driver.find_element_by_name("_username").clear()
        driver.find_element_by_name("_username").send_keys("ZolotovDA")

        driver.find_element_by_name("_password").click()
        driver.find_element_by_name("_password").clear()
        driver.find_element_by_name("_password").send_keys("@#$WERSDFXCV234")

        driver.find_element_by_xpath("//button[@class='btn btn-vi login-button']").click()

        driver.get("http://intgr-test-2.stage.erp.vseinstrumenti.net/docs/Zayavka_Doc/add/?journal_type=doc_zayavki")
        time.sleep(5)
        driver.switch_to_alert().accept()
        time.sleep(1)

        driver.find_element_by_id("newContFacePhone").click()
        driver.find_element_by_id("newContFacePhone").send_keys("9058680002")
        driver.find_element_by_id("contFaceSurname").click()
        driver.find_element_by_name("kontrSelected").click()
        driver.find_element_by_id("chooseFoundContractorButton").click()
        print(driver.current_window_handle)
        driver.find_element_by_id("addNomenclatureBtn").click()

        base_window = print(driver.current_window_handle)  # CDwindow-415AACC4894338D1E80DD585682E0AFB

        handles = driver.window_handles

        for handle in handles:
            driver.switch_to.window(handle)
            print(driver.title)

        driver.find_element_by_id("nom_id").click()
        driver.find_element_by_id("nom_id").send_keys("15791387")
        print(driver.current_window_handle)
        # x = driver.current_window_handle
        # print(x)

        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[4]//input[1]")))
        element.click()

        time.sleep(5)

        # работа с фреймом
        # iframe_form = driver.find_element_by_id("searchResults") инициализация фрейма в переменную

        driver.switch_to.frame(driver.find_element_by_id("searchResults"))
        driver.find_element_by_xpath("//*[@type='button'][@value='Добавить']").click()
        driver.switch_to.default_content()

        print(driver.window_handles)
        print(driver.current_window_handle)
        driver.close()

        # print(driver.current_window_handle)

        time.sleep(10)

        # author = Select(driver.find_element_by_id("author"))
        # author.select_by_index(10)
        # driver.find_element_by_id("newContFacePhone").send_keys("9058680002")


if __name__ == '__main__':
    unittest.main()