# coding:utf-8

import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from email.mime.application import MIMEApplication  #主要类型的MIME消息对象应用
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime
import threading
import readConfig as readConfig
from common import Log


localReadConfig = readConfig.ReadConfig()


class Email:
    def __init__(self):
        global host, user, password, port, sender, title,receivers

        sender = localReadConfig.get_email("sender")  # 发件人
        receivers = ['8463299@qq.com']  # 收件人
        # receivers = ['test@163.com','test@vip.qq.com']  # 接收多个邮件，可设置为你的QQ邮箱或者其他邮箱
        host = localReadConfig.get_email("mail_host")# 设置服务器
        port = localReadConfig.get_email("mail_port")  # 设置服务器
        user = localReadConfig.get_email("mail_user")# QQ邮件登录名称
        password = localReadConfig.get_email("mail_pass")# QQ邮箱的授权码

        title = localReadConfig.get_email("subject")#邮件主题

        # 定义邮件主题
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = "接口测试报告" + " " + date

        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

        self.msg = MIMEMultipart('related')

    def config_header(self):
        """
        defined email header include subject, sender and receiver
        :return:
        """
        self.msg['Subject'] = Header(self.subject)  # 邮件主题
        self.msg['From'] = Header(sender)  # 发件人
        self.msg['To'] = Header(str(";".join(receivers)))  # 收件人

    def config_content(self):
        """
        write the content of email
        :return:
        """
        self.config_file_html_img()
        self.config_file()

    def config_file_html_img(self):
        file_path = os.path.join(readConfig.ProDir, 'testFile', 'emailStyle.html')  # 文件路径
        with open(file_path, 'rb') as fp:  # 读取文件内容
            msg_text = MIMEText(fp.read(), 'html', 'utf-8')  # 创建Text对象，包括文本内容
        self.msg.attach(msg_text)  # 构建HTML格式的邮件内容

        image2_path = os.path.join(readConfig.ProDir, 'testFile', 'img', 'smile.jpg')  # 图片路径
        self.msg.attach(self.add_image(image2_path, '<image2>'))  # 构建HTML格式的邮件内容

    def config_file_html(self):
        report_file_path = Log.Log().get_report_file_path()
        with open(report_file_path, encoding='utf-8') as f:  # 打开html报告
            email_body = f.read()  # 读取报告内容
        self.msg = MIMEMultipart()  # 混合MIME格式
        self.msg.attach(MIMEText(email_body, 'html', 'utf-8'))

    def config_file(self):

        if self.check_file():
            report_folder_path = self.log.get_result_folder_path()
            filename = [os.path.join(report_folder_path, 'output.log'),
                        os.path.join(report_folder_path, 'report.html')]
            for tmp in filename:
                with open(tmp, 'rb') as f:
                    attach_files = MIMEApplication(f.read())
                    attach_files.add_header('Content-Disposition', 'attachment', filename=tmp)
                    self.msg.attach(attach_files)

    def add_image(self,src, img_id):
        # xml中添加图片
        with open(src, 'rb') as f:
            msg_image = MIMEImage(f.read())  # 读取图片内容
        msg_image.add_header('Content-ID', img_id)  # 指定文件的Content-ID,<img>,在HTML中图片src将用到
        return msg_image

    def check_file(self):
        """
        check test report
        :return:
        """
        report_path = self.log.get_report_file_path()
        if os.path.isfile(report_path) and not os.stat(report_path) == 0:
            return True
        else:
            return False

    def send_email(self):
        """
        send email
        :return:
        """
        global smtp
        self.config_content()
        self.config_header()
        try:
            smtp = smtplib.SMTP_SSL(host,port)
            smtp.login(user, password)
            smtp.sendmail(sender, receivers, self.msg.as_string())
            self.logger.info("测试报告已通过电子邮件发送给开发人员")
        except Exception as ex:
            self.logger.error(str(ex))
            return "邮件发送失败"
        finally:
            smtp.quit()

class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_email():

        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email


if __name__ == "__main__":
    email = MyEmail.get_email()
