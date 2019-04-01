import smtplib
import os
import readConfig as readConfig
from datetime import datetime

from email.mime.text import MIMEText#html格式和文本格式邮件
from email.mime.multipart import MIMEMultipart  #导入MIMEMultipart类，带多个部分的邮件
from email.mime.image import MIMEImage   #导入MIMEImage类，带图片格式邮件
from email.utils import formataddr   #分隔标题与地址
from email.mime.base import MIMEBase  #MIME子类的基类
from email.header import Header #设置标题字符集
from email import encoders#编码器
from email.mime.application import MIMEApplication  #主要类型的MIME消息对象应用





localReadConfig = readConfig.ReadConfig()
class Email():
    def __init__(self):
        global mail_host, mail_user, mail_pass, mail_port,mail_replyto, sender, title,receivers,content

        sender = localReadConfig.get_email("sender")  # 发送邮件名称
        receivers = ['8463299@qq.com']  # 收件人
        # receivers = ['test@163.com','test@vip.qq.com']  # 接收多个邮件，可设置为你的QQ邮箱或者其他邮箱
        mail_host = localReadConfig.get_email("mail_host")  # 设置服务器
        mail_port = localReadConfig.get_email("mail_port")  # 设置服务器
        mail_user = localReadConfig.get_email("mail_user")  # QQ邮件登陆名称
        mail_pass = localReadConfig.get_email("mail_pass")  # QQ邮箱的授权码
        mail_replyto = localReadConfig.get_email("mail_replyto")  #
        content= localReadConfig.get_email("content")  #
        title = localReadConfig.get_email("subject")  # 邮件主题

        # 定义邮件主题
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = "接口测试报告 " + date

        self.message=MIMEMultipart('related')  #创建MIMEMultipart对象，创建一个多部分的邮件对象
        self.message['Reply-to'] = mail_replyto




    def config_header(self):
        self.message['From'] = Header(sender)  # 发件人
        self.message['To'] = Header(str(";".join(receivers)))  # 收件人
        self.message['Subject'] = Header(self.subject)  # 邮件主题

    def config_content(self):
        #定义内容

        #self.message.attach(MIMEText(content,'plain','utf-8'))##构建文本邮件内容
        #self.config_file_html()#构建HTML格式的邮件内容
        self.config_file_html_img()#构建HTML格式邮件带图片内容
        self.config_file()#添加附件
        self.config_file_2()
        self.config_image()#添加附件图片

    def config_file_html(self):
        file_path = os.path.join(readConfig.path, 'testFile', 'emailStyle.xml')  # 文件路径
        with open(file_path, 'rb') as fp:  # 读取文件内容
            msgtext = MIMEText(fp.read(), 'html', 'utf-8')  # 创建Text对象，包括文本内容
        self.message.attach(msgtext)  # 构建HTML格式的邮件内容

    def config_file_html_img(self):
        file_path = os.path.join(readConfig.path, 'testFile', 'emailStyle.xml')  # 文件路径
        with open(file_path, 'rb') as fp:  # 读取文件内容
            msgtext = MIMEText(fp.read(), 'html', 'utf-8')  # 创建Text对象，包括文本内容
        self.message.attach(msgtext)  # 构建HTML格式的邮件内容

        image1_path = os.path.join(readConfig.path, 'testFile', 'img', '1.png')  # 图片路径
        self.message.attach(self.addimg(image1_path, 'io'))  # 构建HTML格式的邮件内容


    def config_image(self):#添加图片附件
        """
        config image that be used by content
        :return:
        """
        #添加附件图片1
        image1_path = os.path.join(readConfig.path, 'testFile', 'img', '1.png')#图片路径

        attachfile = MIMEBase('applocation', 'octet-stream')  # 创建对象指定主要类型和次要类型
        attachfile.set_payload(open(image1_path, 'rb').read())  # 将消息内容设置为有效载荷
        attachfile.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', image1_path))  # 扩展标题设置
        encoders.encode_base64(attachfile)
        self.message.attach(attachfile)  # 附加对象加入到msg



    def config_file(self):#带附件的邮件MIMEApplication
        filename = os.path.join(readConfig.path, 'testFile', 'img', 'test.txt')
        with open(filename, 'rb') as f:
            attachfile = MIMEApplication(f.read())
        attachfile.add_header('Content-Disposition', 'attachment', filename=filename)
        self.message.attach(attachfile)

    def config_file_2(self):#带多个附件的邮件MIMEApplication
        filename = [os.path.join(readConfig.path, 'testFile', 'img', 'test.txt'),os.path.join(readConfig.path, 'testFile', 'img', 'test2.txt')]
        for tmp in filename:
            with open(tmp, 'rb') as f:
                attachfiles = MIMEApplication(f.read())
                attachfiles.add_header('Content-Disposition', 'attachment', filename=tmp)
                self.message.attach(attachfiles)

    def addimg(self,src, imgid):
        # xml中添加图片
        with open(src, 'rb') as f:
            msgimage = MIMEImage(f.read())  # 读取图片内容
        msgimage.add_header('Content-ID', imgid)  # 指定文件的Content-ID,<img>,在HTML中图片src将用到
        return msgimage


    def post_email(self):
        self.config_content()
        self.config_header()
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)#创建一个SMTP（）对象，建立连接
            smtpObj.login(mail_user, mail_pass)#登录邮箱
            smtpObj.sendmail(sender, receivers, self.message.as_string())#邮件发送
            smtpObj.quit()#关闭邮箱
            return '邮件发送成功'
        except smtplib.SMTPException:
            return '发送失败'


if __name__ == '__main__':
    result = Email().post_email()
    print(result)