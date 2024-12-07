"""
项目：禹城一中成绩查询
作者：杨统斌 - YangTB
运维日期： 2024年7月14日
贡献者名单：{
    '孙泉坤': '宣传，试用，投资10元',
    '杨子成': '试用，投资6元',
    '聂永昊':'宣传',
}
"""

import json
from flask import Flask,request,render_template
import datetime
app = Flask(__name__)
app.debug = True


vip = {  # 投资或充值所得
    '杨统斌': 'index_yellow.html',
    '孙泉坤': 'index_sqk.html',  # 投资10元
    '杨子成': 'index_vip.html',  # 投资6元
}

@app.route('/',methods=['GET','POST'])
def hello_world():  # put application's code here
    return render_template('index_in.html', sign=True)

@app.route('/chengji/',methods=['GET','POST'])
def chengji():
    html_index = 'index_chengji.html'
    chengji = open('ok.json','r',encoding='utf-8')
    chengji =json.load(chengji)
    name = request.form.get('name')
    s_class = request.form.get('s_class')
    ip_address = request.remote_addr
    user_info = request.user_agent
    print(name)
    print(s_class)
    print(ip_address)
    print(user_info)
    now = datetime.datetime.now()  # 获取当前时间
    file = open('log.txt', 'a+', encoding='utf-8')
    now_time = now.strftime("%Y-%m-%d %H:%M:%S") # 格式化时间
    log = f'时间：{now_time}\n姓名:{name} || 班级:{s_class}\nip:{ip_address}\nuser_info:{user_info} \n'
    file.write(log)
    if name == r'作者' and s_class == r'作者':
        return render_template('maker.html')
    if name == '李忠鑫' and s_class == '生日快乐':
        return render_template('index_lzx.html')
    try:
        if name in vip.keys():
            html_index = vip[name]
        try:
            a = chengji[s_class][name]  # 检验姓名班级是否合法
            file.write('状态:查询成功\n=======================\n')
        except:
            file.write('状态:查询失败\n=======================\n')

        return render_template(
            f'{html_index}',
            name=name,
            s_class=s_class,
            s_id=chengji[s_class][name]['考号'],
            all_yuan=chengji[s_class][name]['原始总分'],
            all=chengji[s_class][name]['总分'],
            mingci_shi=chengji[s_class][name]['市名次'],
            mingci_xiao=chengji[s_class][name]['校名次'],
            mingci_ban=chengji[s_class][name]['班名次'],

            # s_school = chengji[s_class][name]['学校'],
            chinese=chengji[s_class][name]['语文']['分数'],
            chinese_m=chengji[s_class][name]['语文']['名次'],

            math=chengji[s_class][name]['数学']['分数'],
            math_m=chengji[s_class][name]['数学']['名次'],

            english=chengji[s_class][name]['英语']['分数'],
            english_m=chengji[s_class][name]['英语']['名次'],

            xiaoyuzhong=chengji[s_class][name]['小语种']['语种'],
            xiaoyuzhong_fenshu=chengji[s_class][name]['小语种']['分数'],

            wuli=chengji[s_class][name]['物理']['分数'],
            wuli_z=chengji[s_class][name]['物理']['转换'],
            wuli_m=chengji[s_class][name]['物理']['名次'],

            huaxue=chengji[s_class][name]['化学']['分数'],
            huaxue_z=chengji[s_class][name]['化学']['转换'],
            huaxue_m=chengji[s_class][name]['化学']['名次'],

            shengwu=chengji[s_class][name]['生物']['分数'],
            shengwu_z=chengji[s_class][name]['生物']['转换'],
            shengwu_m=chengji[s_class][name]['生物']['名次'],

            zhengzhi=chengji[s_class][name]['政治']['分数'],
            zhengzhi_z=chengji[s_class][name]['政治']['转换'],
            zhengzhi_m=chengji[s_class][name]['政治']['名次'],

            lishi=chengji[s_class][name]['历史']['分数'],
            lishi_z=chengji[s_class][name]['历史']['转换'],
            lishi_m=chengji[s_class][name]['历史']['名次'],

            dili=chengji[s_class][name]['地理']['分数'],
            dili_z=chengji[s_class][name]['地理']['转换'],
            dili_m=chengji[s_class][name]['地理']['名次'],
        )
    except:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
