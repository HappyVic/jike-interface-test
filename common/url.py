# -*- coding:utf-8 -*-
#!/usr/bin/python

#user

users_loginWithPhoneAndPassword = "/1.0/users/loginWithPhoneAndPassword/"#手机号密码登录
users_getSmsCode = "/1.0/users/getSmsCode"#获取验证码
users_profile = "/1.0/users/profile"#个人主页
users_register= "/1.0/users/register"#注册匿名帐号


#主理人申请接口
topics_roles_admin_checkQualification = "/1.0/topics/roles/admin/checkApplicationQualification?topicId=<topicId>" #检查用户的申请资格
topics_roles_admin_submit = "/1.0/topics/roles/admin/submitApplication" #提交用户的主理人申请

#客户端主理人相关接口
topics_getDetail = "/1.0/topics/getDetail"#主题详情页
topics_listInvolvedUsers ="￿/1.0/topics/listInvolvedUsers￿"#rol

#客户端动态详情页接口
originalPosts_get = "/1.0/originalPosts/get?refTopicId=<topicId>" #主题详情页进入动态详情页
comments_listPrimary = "/1.0/comments/listPrimary" #评论列表




