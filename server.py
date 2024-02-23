from flask import jsonify #从flask导入jsonify函数，用于将数据转换为JSON格式的响应
from flask import request #从flask导入request对象，用于获取客户端发送的请求数据。
import json #导入json模块，用于处理jison数据
from flask import Flask #从flask模块中导入Flask类，用于创建web应用
from wored2 import func



app=Flask(__name__) #创建一个Flask应用实例

# def get_word(word): #定义一个函数，接受一个单词作为参数，目标函数体仅返回接收的单词

    # return word+" "+word
    # return word**2
    # return func(word)


@app.route("/nlp/words",methods=["GET","POST"]) #使用app.route装饰器定义路由，指定url路径和接受的请求方法

def nlp_service():#定义处理该路由请求的函数。
    data=request.get_data() #从请求中获取数据
    result_data=json.loads(data)#将获取的数据从json格式解析为python字典
    word1=result_data.get("word1","") #从解析后的数据中获取键为“word"的值，如果不存在则默认为空字符串
    word2=result_data.get("word2","")
    # value=get_word(word) #调用get_word函数处理获取到的单词
    value=func(word1,word2)
    return jsonify({"code":200,"result":value}) #使用jsonify函数构建json格式的响应，包含状态码和处理结果

if __name__ == '__main__':  #判断是否为主程序运行，而非模块导入
    app.run(host="0.0.0.0",port=50001) #启动flask应用，指定监听的主机地址和端口号
    #0.0.0.0.在同一个设备上用