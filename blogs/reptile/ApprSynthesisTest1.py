# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome('C:\driver\chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("http://localhost:80/ApprBase/admin/system/index/toIndex.do")

        driver.find_element_by_xpath(u'//*[@id="j_username"]').click()
        driver.find_element_by_xpath(u'//*[@id="j_username"]').clear()
        driver.find_element_by_xpath(u'//*[@id="j_username"]').send_keys("HUB_01")
        driver.find_element_by_id("j_password").click()
        driver.find_element_by_id("j_password").clear()
        driver.find_element_by_id("j_password").send_keys("abc123456")
        driver.find_element_by_link_text(u"登    录").click()
        driver.find_element_by_xpath(u'//*[@id="j-nav"]/li[9]/a').click()

        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='综合窗口'])[1]/following::span[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        # driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='广东省'])[3]/following::font[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=2 | ]]
        frame1 = driver.find_element_by_xpath(u'//*[@id="j-tab"]/div[2]/div[2]/iframe')
        driver.switch_to.frame(frame1)
        driver.find_element_by_xpath(u'//*[@id="datagrid-row-r1-2-1e08df4953dd4ad7ae5a54de627a63a7"]/td[6]/div/a').click()
        # driver.find_element_by_xpath(u'//*[@id="datagrid-row-r1-2-0"]').click()
        # driver.find_element_by_id("selectedButton").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        time.sleep(1)
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        print('now_handle: %s' % now_handle)
        print('all_handles: %s' % all_handles)
        for windowId in all_handles:
            if (windowId != now_handle):
                driver.switch_to.window(windowId)
                break
        print('current_window: %s' % driver.current_window_handle)
        driver.switch_to.frame('iframeId')
        # driver.find_element_by_xpath(u'//*[@id="selectCustQY"]').click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=6 | ]]
        # driver.find_element_by_xpath(u'//*[@id="datagrid-row-r1-2-0"]').click()
        # driver.find_element_by_id("selectedButton").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        #企业信息填写
        driver.find_element_by_xpath(u'//*[@id="enterpriseName"]').click()
        driver.find_element_by_xpath(u'//*[@id="enterpriseName"]').clear()
        driver.find_element_by_xpath(u'//*[@id="enterpriseName"]').send_keys('广州盛大')
        driver.find_element_by_xpath(u'//*[@id="custAddr"]').click()
        driver.find_element_by_xpath(u'//*[@id="custAddr"]').clear()
        driver.find_element_by_xpath(u'//*[@id="custAddr"]').send_keys('广州市天河区中山大道403号')
        driver.find_element_by_xpath(u'//*[@id="legalMan"]').click()
        driver.find_element_by_xpath(u'//*[@id="legalMan"]').clear()
        driver.find_element_by_xpath(u'//*[@id="legalMan"]').send_keys('WUXiaoTing')
        driver.find_element_by_xpath(u'//*[@id="custCerId"]').click()
        driver.find_element_by_xpath(u'//*[@id="custCerId"]').clear()
        driver.find_element_by_xpath(u'//*[@id="custCerId"]').send_keys('441581199407012397')
        driver.find_element_by_xpath(u'//*[@id="bookNum"]').click()
        driver.find_element_by_xpath(u'//*[@id="bookNum"]/option[2]').click()
        driver.find_element_by_xpath(u'//*[@id="enterprise"]/table[1]/tbody/tr[5]/td[2]/input').click()
        driver.find_element_by_xpath(u'//*[@id="enterprise"]/table[1]/tbody/tr[5]/td[2]/input').clear()
        driver.find_element_by_xpath(u'//*[@id="enterprise"]/table[1]/tbody/tr[5]/td[2]/input').send_keys('1000')
        driver.find_element_by_xpath(u'//*[@id="typeId"]').click()
        driver.find_element_by_xpath(u'//*[@id="typeId"]/option[2]').click()
        driver.find_element_by_xpath(u'//*[@id="investType"]').click()
        driver.find_element_by_xpath(u'//*[@id="investType"]/option[2]').click()
        driver.find_element_by_xpath(u'//*[@id="manageItem"]').click()
        driver.find_element_by_xpath(u'//*[@id="manageItem"]').clear()
        driver.find_element_by_xpath(u'//*[@id="manageItem"]').send_keys('游戏')
        driver.find_element_by_xpath(u'//*[@id="orgCode"]').click()
        driver.find_element_by_xpath(u'//*[@id="orgCode"]').clear()
        driver.find_element_by_xpath(u'//*[@id="orgCode"]').send_keys('WXTM00913343455')
        driver.find_element_by_xpath(u'//*[@id="credNum"]').click()
        driver.find_element_by_xpath(u'//*[@id="credNum"]').clear()
        driver.find_element_by_xpath(u'//*[@id="credNum"]').send_keys('67373')
        driver.find_element_by_xpath(u'//*[@id="regNum"]').click()
        driver.find_element_by_xpath(u'//*[@id="regNum"]').clear()
        driver.find_element_by_xpath(u'//*[@id="regNum"]').send_keys('67373')

        time.sleep(2)
        #申请人信息填写
        driver.find_element_by_xpath(u'//*[@id="custContactPerson"]').click()
        driver.find_element_by_xpath(u'//*[@id="custContactPerson"]').clear()
        driver.find_element_by_xpath(u'//*[@id="custContactPerson"]').send_keys('WUXiaoTing')
        driver.find_element_by_xpath(u'//*[@id="cardType"]').click()
        driver.find_element_by_xpath(u'//*[@id="cardType"]/option[1]').click()
        driver.find_element_by_xpath(u'//*[@id="idCard"]').click()
        driver.find_element_by_xpath(u'//*[@id="idCard"]').clear()
        driver.find_element_by_xpath(u'//*[@id="idCard"]').send_keys('441581199407012397')
        driver.find_element_by_xpath(u'//*[@id="custMobile"]').click()
        driver.find_element_by_xpath(u'//*[@id="custMobile"]').clear()
        driver.find_element_by_xpath(u'//*[@id="custMobile"]').send_keys('18814118018')
        driver.find_element_by_xpath(u'//*[@id="custContactWay"]').click()
        driver.find_element_by_xpath(u'//*[@id="custContactWay"]').clear()
        driver.find_element_by_xpath(u'//*[@id="custContactWay"]').send_keys('020-1234567')

        # 保存按钮
        # driver.find_element_by_xpath(u'//*[@id="doSave"]').click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_id("doSave").click()
        driver.find_element_by_id("nav_sbcl").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_id("attaStatusSelect").click()
        Select(driver.find_element_by_id("attaStatusSelect")).select_by_visible_text(u"合格")
        driver.find_element_by_id("attaStatusSelect").click()
        driver.find_element_by_link_text(u"上传").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=6 | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='把文件(文件夹)拖拽到这里'])[1]/preceding::div[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='--:--:--'])[1]/following::button[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='文件上传'])[1]/preceding::button[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='材料2(纸质件必须)'])[1]/following::a[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=6 | ]]
        driver.find_element_by_id("i_select_files").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='--:--:--'])[1]/following::button[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='文件上传'])[1]/preceding::button[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_id("auditResult0").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='删除'])[2]/following::div[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_id("doSend").click()
        driver.find_element_by_id("select-people").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=17 | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='hj(hj测试单位)'])[1]/following::span[5]").click()
        driver.find_element_by_link_text(u"确定").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_id("doSend").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='进入受理'])[1]/following::button[1]").click()
        driver.find_element_by_id("nav_sbcl").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_id("auditResult0").click()
        Select(driver.find_element_by_id("auditResult0")).select_by_visible_text(u"合格")
        driver.find_element_by_id("auditResult0").click()
        driver.find_element_by_id("auditResult1").click()
        Select(driver.find_element_by_id("auditResult1")).select_by_visible_text(u"合格")
        driver.find_element_by_id("auditResult1").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='HUB_01(HUB)'])[1]/following::button[2]").click()
        driver.find_element_by_id("doSave").click()
        self.assertEqual(u"受理之后，办件开始倒计时。", self.close_alert_and_get_its_text())
        driver.find_element_by_id("doSend").click()
        driver.find_element_by_id("doSend").click()
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_id("doSend").click()
        driver.find_element_by_name("handleInfo.apprResult").click()
        driver.find_element_by_id("select-people").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=17 | ]]
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='HUB_03(HUB-湛江市)'])[1]/following::span[5]").click()
        driver.find_element_by_link_text(u"确定").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_id("doSend").click()
        driver.find_element_by_id("commonWordBySel").click()
        Select(driver.find_element_by_id("commonWordBySel")).select_by_visible_text(u"同意")
        driver.find_element_by_id("commonWordBySel").click()
        driver.find_element_by_id("msg").click()
        driver.find_element_by_id("doSave").click()
        driver.find_element_by_id("doSend").click()
        driver.close()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
