# -*- coding: utf-8 -*-

from odoo.tests.common import HttpCase, new_test_user


class TestDatarobotController(HttpCase):
    def setUp(self):
        super().setUp()
        self.user = new_test_user(self.env, "test_user_1", email="test_user_1@nowhere.com", password="P@ssw0rd!", tz="UTC")

    def test_submit_form(self):
        self.authenticate("test_user_1", "P@ssw0rd!")

        form_url = "/datarobot/form"
        form_res = self.url_open(form_url)
        self.assertEqual(form_res.status_code, 200, "Response should = OK")

        submit_url = "/datarobot/form/submit"
        submit_res = self.url_open(submit_url)
        self.assertEqual(submit_res.status_code, 200, "Response should = OK")
