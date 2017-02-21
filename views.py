from django.shortcuts import render

def index(request):
    block_info=[{"name":"人间词话","descp":"好文章投过来","admin":"管理员：Freddy"},
                {"name":"工作","descp":"公司列表","admin":"管理员：Freddy"},
               {"name":"学校","descp":"人脉网络","admin":"管理员：Freddy"},]
    return render(request,"index.html",{"blocks":block_info})

