# NOTE: Generated By HttpRunner v3.1.3
# FROM: test_two.yaml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseTestTwo(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/api/payments/config")
            .post("https://sandbox-cs.lingjm365.com/api/payments/config")
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "Content-Length": "31",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Cookie": "lang=zh-CN; ma_id=acebbcf1-0716-4767-a3be-28333bccb2a1; gr_user_id=a91fbe93-1e80-4127-bbdf-b293c5c92bee; grwng_uid=17021336-fc2d-48a2-8c74-1f8d26dfa455; swh_yi_jing_zhan_bu_last_show=1564652055140; ai_shi_nian_wei_ji_last_show=1564652596502; ai_qian_shi_yin_yuan_last_show=1564655089953; mei_yue_liu_yue_last_show=1564655922753; sheng_ming_ling_shu_last_show=1564745004525; lian_ai_tao_hua_last_show=1568021443575; 53revisit=1568187091986; Hm_lvt_5e405002d5c49292fe521aba789da744=1566992715,1567134882,1568189684; shi_nian_da_yun_last_show=1574048789032; _ga=GA1.2.1259099948.1574835445; iUUID=00def475944d9ea25b42c8bada496461; LHMOUNT=03fe778a-7f9d-45a0-8360-6f914f5af5d9; zhen_ming_qing_ren_last_show=1575514708600; ba_zi_he_hun_shu_last_show=1575526764739; ba_zi_liu_nian_last_show=1575527365988; shi_ye_xiang_pi_last_show=1575527860157; USERIDTYPE=cookie; qian_shi_dang_an_last_show=1586862367211; ai_qing_xing_zuo_pei_dui_last_show=1586919592260; san_sheng_shi_last_show=1587106139609; mll_tou_fang_last_show=1594281028558; zhi_shang_ce_shi_last_show=1595398739262; _channel=test; ltvId=X01; Hm_lvt_da9f609f31e08775a3c08224838230b5=1595840232,1595840241,1595910472,1595916388; Hm_lpvt_da9f609f31e08775a3c08224838230b5=1595916388",
                    "Host": "sandbox-cs.lingjm365.com",
                    "Origin": "https://sandbox-cs.lingjm365.com",
                    "Referer": "https://sandbox-cs.lingjm365.com/taluoquanfangwei/pay?order_id=TLFW159591653200000060",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
                }
            )
            .with_cookies(
                **{
                    "53revisit": "1568187091986",
                    "Hm_lpvt_da9f609f31e08775a3c08224838230b5": "1595916388",
                    "Hm_lvt_5e405002d5c49292fe521aba789da744": "1566992715,1567134882,1568189684",
                    "Hm_lvt_da9f609f31e08775a3c08224838230b5": "1595840232,1595840241,1595910472,1595916388",
                    "LHMOUNT": "03fe778a-7f9d-45a0-8360-6f914f5af5d9",
                    "USERIDTYPE": "cookie",
                    "_channel": "test",
                    "_ga": "GA1.2.1259099948.1574835445",
                    "ai_qian_shi_yin_yuan_last_show": "1564655089953",
                    "ai_qing_xing_zuo_pei_dui_last_show": "1586919592260",
                    "ai_shi_nian_wei_ji_last_show": "1564652596502",
                    "ba_zi_he_hun_shu_last_show": "1575526764739",
                    "ba_zi_liu_nian_last_show": "1575527365988",
                    "gr_user_id": "a91fbe93-1e80-4127-bbdf-b293c5c92bee",
                    "grwng_uid": "17021336-fc2d-48a2-8c74-1f8d26dfa455",
                    "iUUID": "00def475944d9ea25b42c8bada496461",
                    "lang": "zh-CN",
                    "lian_ai_tao_hua_last_show": "1568021443575",
                    "ltvId": "X01",
                    "ma_id": "acebbcf1-0716-4767-a3be-28333bccb2a1",
                    "mei_yue_liu_yue_last_show": "1564655922753",
                    "mll_tou_fang_last_show": "1594281028558",
                    "qian_shi_dang_an_last_show": "1586862367211",
                    "san_sheng_shi_last_show": "1587106139609",
                    "sheng_ming_ling_shu_last_show": "1564745004525",
                    "shi_nian_da_yun_last_show": "1574048789032",
                    "shi_ye_xiang_pi_last_show": "1575527860157",
                    "swh_yi_jing_zhan_bu_last_show": "1564652055140",
                    "zhen_ming_qing_ren_last_show": "1575514708600",
                    "zhi_shang_ce_shi_last_show": "1595398739262",
                }
            )
            .with_data({"order_id": "TLFW159591653200000060"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json; charset=UTF-8")
            .assert_equal("body.order_id", "TLFW159591653200000060")
            .assert_equal("body.created_at", 1595916532)
            .assert_equal("body.amount", 0.01)
            .assert_equal("body.channel", "test")
            .assert_equal("body.platform", "default")
            .assert_equal("body.status", "created")
            .assert_equal("body.origin_amount", 50.01)
        ),
        Step(
            RunRequest("/api/orders/TLFW159591653200000060")
            .get("https://sandbox-cs.lingjm365.com/api/orders/TLFW159591653200000060")
            .with_params(**{"rand": "0.40024777386524524"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "Cookie": "lang=zh-CN; ma_id=acebbcf1-0716-4767-a3be-28333bccb2a1; gr_user_id=a91fbe93-1e80-4127-bbdf-b293c5c92bee; grwng_uid=17021336-fc2d-48a2-8c74-1f8d26dfa455; swh_yi_jing_zhan_bu_last_show=1564652055140; ai_shi_nian_wei_ji_last_show=1564652596502; ai_qian_shi_yin_yuan_last_show=1564655089953; mei_yue_liu_yue_last_show=1564655922753; sheng_ming_ling_shu_last_show=1564745004525; lian_ai_tao_hua_last_show=1568021443575; 53revisit=1568187091986; Hm_lvt_5e405002d5c49292fe521aba789da744=1566992715,1567134882,1568189684; shi_nian_da_yun_last_show=1574048789032; _ga=GA1.2.1259099948.1574835445; iUUID=00def475944d9ea25b42c8bada496461; LHMOUNT=03fe778a-7f9d-45a0-8360-6f914f5af5d9; zhen_ming_qing_ren_last_show=1575514708600; ba_zi_he_hun_shu_last_show=1575526764739; ba_zi_liu_nian_last_show=1575527365988; shi_ye_xiang_pi_last_show=1575527860157; USERIDTYPE=cookie; qian_shi_dang_an_last_show=1586862367211; ai_qing_xing_zuo_pei_dui_last_show=1586919592260; san_sheng_shi_last_show=1587106139609; mll_tou_fang_last_show=1594281028558; zhi_shang_ce_shi_last_show=1595398739262; _channel=test; ltvId=X01; Hm_lvt_da9f609f31e08775a3c08224838230b5=1595840232,1595840241,1595910472,1595916388; Hm_lpvt_da9f609f31e08775a3c08224838230b5=1595916388",
                    "Host": "sandbox-cs.lingjm365.com",
                    "Referer": "https://sandbox-cs.lingjm365.com/taluoquanfangwei/pay?order_id=TLFW159591653200000060",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
                }
            )
            .with_cookies(
                **{
                    "53revisit": "1568187091986",
                    "Hm_lpvt_da9f609f31e08775a3c08224838230b5": "1595916388",
                    "Hm_lvt_5e405002d5c49292fe521aba789da744": "1566992715,1567134882,1568189684",
                    "Hm_lvt_da9f609f31e08775a3c08224838230b5": "1595840232,1595840241,1595910472,1595916388",
                    "LHMOUNT": "03fe778a-7f9d-45a0-8360-6f914f5af5d9",
                    "USERIDTYPE": "cookie",
                    "_channel": "test",
                    "_ga": "GA1.2.1259099948.1574835445",
                    "ai_qian_shi_yin_yuan_last_show": "1564655089953",
                    "ai_qing_xing_zuo_pei_dui_last_show": "1586919592260",
                    "ai_shi_nian_wei_ji_last_show": "1564652596502",
                    "ba_zi_he_hun_shu_last_show": "1575526764739",
                    "ba_zi_liu_nian_last_show": "1575527365988",
                    "gr_user_id": "a91fbe93-1e80-4127-bbdf-b293c5c92bee",
                    "grwng_uid": "17021336-fc2d-48a2-8c74-1f8d26dfa455",
                    "iUUID": "00def475944d9ea25b42c8bada496461",
                    "lang": "zh-CN",
                    "lian_ai_tao_hua_last_show": "1568021443575",
                    "ltvId": "X01",
                    "ma_id": "acebbcf1-0716-4767-a3be-28333bccb2a1",
                    "mei_yue_liu_yue_last_show": "1564655922753",
                    "mll_tou_fang_last_show": "1594281028558",
                    "qian_shi_dang_an_last_show": "1586862367211",
                    "san_sheng_shi_last_show": "1587106139609",
                    "sheng_ming_ling_shu_last_show": "1564745004525",
                    "shi_nian_da_yun_last_show": "1574048789032",
                    "shi_ye_xiang_pi_last_show": "1575527860157",
                    "swh_yi_jing_zhan_bu_last_show": "1564652055140",
                    "zhen_ming_qing_ren_last_show": "1575514708600",
                    "zhi_shang_ce_shi_last_show": "1595398739262",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json; charset=UTF-8")
            .assert_equal("body.order_id", "TLFW159591653200000060")
            .assert_equal("body.channel", "test")
            .assert_equal("body.schannel", "")
            .assert_equal("body.amount", 0.01)
            .assert_equal("body.origin_amount", 50.01)
            .assert_equal("body.status", "created")
            .assert_equal("body.phone", "")
            .assert_equal("body.email", "")
            .assert_equal("body.created_at", "2020-07-28 14:08:52")
            .assert_equal("body.is_free", "no")
            .assert_equal(
                "body.next", "/taluoquanfangwei/pay?order_id=TLFW159591653200000060"
            )
        ),
    ]


if __name__ == "__main__":
    TestCaseTestTwo().test_start()