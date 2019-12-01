"""
============================
Author:柠檬班-木森
Time:2019/11/15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
# 测试需求2：（作业）
users = [{'user': 'python24', 'password': '123456'}]


def register(username, password1, password2):
    # 判断是否有参数为空
    if not all([username, password1, password2]):
        return {"code": 0, "msg": "所有参数不能为空"}
    # 注册功能
    for user in users:  # 遍历出所有账号，判断账号是否存在
        if username == user['user']:
            # 账号存在
            return {"code": 0, "msg": "该账户已存在"}
    else:
        if password1 != password2:
            # 两次密码不一致
            return {"code": 0, "msg": "两次密码不一致"}
        else:
            # 账号不存在 密码不重复，判断账号密码长度是否在 6-18位之间
            if 6 <= len(username) >= 6 and 6 <= len(password1) <= 18:
                # 注册账号
                users.append({'user': username, 'password': password2})
                return {"code": 1, "msg": "注册成功"}
            else:
                # 账号密码长度不对，注册失败
                return {"code": 0, "msg": "账号和密码必须在6-18位之间"}


if __name__ == "__main__":
    res = register('python14', '123456', '123456')
    print(res)

"""
函数入参：
注意：参数传字符串类型，不需要考虑其他类型。
参数1：账号  
参数2：密码1
参数2：密码2 


函数内部处理的逻辑：
	判断是否有参数为空，
    判断账号密码是否在6-18位之间，
    判断账号是否被注册过，
    判断两个密码是否一致。
    上面添加都校验通过才能注册成功，其他情况都注册失败，
各种情况的返回结果如下：  
	注册成功               返回结果：{"code": 1, "msg": "注册成功"}
	有参数为空，            返回结果 {"code": 0, "msg": "所有参数不能为空"}   
	两次密码不一致          返回结果：{"code": 0, "msg": "两次密码不一致"}
	账户已存在             返回结果：{"code": 0, "msg": "该账户已存在"}
	密码不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}           	  
	账号不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}


作业要求：请设计用例，对此功能函数进行单元测试，           

提示：上面已经被注册的账号：python24
提示：不需要去看功能函数内部的代码是怎么实现的，也不要改里面的代码，直接复制过去就好，函数内部有bug,自己设计用例去测，测到了自己记录下来            
"""
