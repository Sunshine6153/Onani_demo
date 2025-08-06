# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define s = Character("圣娅")
define m = Character("玛丽")

image bedroom:
    "images/bedroom.jpg"
    zoom 1.5

image church:
    "images/church.jpg"
    zoom 1.5

image corridor:
    "images/corridor.png"
    zoom 1.2

image examroom:
    "images/examroom.jpg"
    zoom 1.5
# 定义一个通用的 transform（变换）
transform default_transform:
    zoom 0.8
    xanchor 0.5
    yanchor 0.5
    xpos 960
    ypos 1000

transform left_transform:
    zoom 0.8
    xanchor 0.5
    yanchor 0.5
    xpos 500
    ypos 1000

transform right_transform:
    zoom 0.8
    xanchor 0.5
    yanchor 0.5
    xpos 1920-500
    ypos 1000

image seia:
    "images/seia.png"

image seia01:
    "images/seia01.png"

image seia02:
    "images/seia02.png"

image seia03:
    "images/seia03.png"

image mari:
    "images/mari.png"

image mari01:
    "images/mari01.png"

image mari02:
    "images/mari02.png"

image mari03:
    "images/mari03.png"

image hiyo:
    "images/hiyo.png"

image hiyo1:
    "images/hiyo1.png"



define flag = 0

define mark = 0
# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene start
    with fade
    play music "audio/backgroundvoice.mp3" fadein 1.0
    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。
    "前言：这是Sunshine第一次尝试制作galgame的伟大尝试。"
    "为了梦想，旮旯启动！"
    scene bedroom
    with fade

    show seia at default_transform
    with dissolve
    # 此处显示各行对话。
    voice "voice/01.mp3"
    s "每到学院的期末周，瓦达西蛙颠三倒四的复习，作息乱成非人类。"
    voice "voice/02.wav"
    s "俗话说：小考小玩，大考大玩。一会儿学一会儿玩，主打一个愉悦。"
    voice "voice/03.mp3"
    s "感受期末厄运重压！最后什么都不想做，感觉在期末周失去了人生的意义。"
    voice "voice/04.wav"
    s "当我无所事事的时候，身体深处的悸动就更加明显，似乎在告诉我时间到了..."

    menu:
        "为了排解压力，小圣娅的选择是"
        "发动技能：欧娜尼":
            $ flag = 1
        "看答辩小视频":
            $ flag = 2

    if flag == 1:
        jump s1
    elif flag == 2:
        jump ykn
      
label ykn:
    $ renpy.music.set_volume(1.0, channel="movie")

    play movie "videos/yknloud.webm"  # 播放视频
    show movie  # 显示视频
    
    $ renpy.pause(21.0)  # 暂停
    
    stop movie  # 停止视频
    hide movie  # 隐藏视频

    voice "voice/ykn01.wav"
    s "没想到现在学院这么卷,又增加了应考压力。"
    "学习热情 level——UP!"
    voice "voice/ykn02.wav"
    s "我更想欧娜尼了,开始吧！"

    jump s1


label s1:
    show seia01 at default_transform
    "因为选择欧娜尼..."
    hide seia01 at default_transform
    show seia02 at default_transform
    "圣娅感觉要起飞了！"
    hide seia02 at default_transform
    show seia03 at default_transform
    "一番解放之后，圣娅身心倍感平静。"
    "进入贤者模式后，放纵欲望的负罪感让她感觉自己只是一只发情的狐狸。"
    hide seia03 at default_transform
    show seia at default_transform
    voice "voice/05.wav"
    s "天父在上，圣娅想要忏悔！"
    "说罢，疲惫感袭来，圣娅几乎是晕了过去..."
    stop music fadeout 1.0

    scene church
    with fade
    "PS:此处引用b站up主FrostMusic版本的垂怜经。"
    "圣娅恢复意识后，来到教堂。"
    play music "audio/kyrie.ogg" 

    show seia at left_transform
    with dissolve    
    show mari at right_transform
    with dissolve
    voice "voice/06.wav"
    s "我要忏悔！"
    
    show mari01 at right_transform
    voice "voice/m01.wav"
    m "圣娅酱，你怎么了，犯错了吗？"

    show seia01 at left_transform
    voice "voice/07.wav"
    s "因为期末周拉平均绩点压力太大，我又放纵自己欧娜尼了。"
    hide seia01 at default_transform
    show seia02 at left_transform
    voice "voice/08.wav"
    s "累的几乎晕了过去，醒来已经是下午了。"
    voice "voice/09.wav"
    s "浪费了大量的复习时间，还伤了身体..."
    hide seia02 at default_transform
    voice "voice/m02.wav"
    m "等下，等下，圣娅酱。欧娜尼是什么啊？"

    show seia01 at left_transform
    voice "voice/10.wav"
    s "就是用花洒什么等奇怪的东西，如此这般那般..."
    hide seia01 at default_transform

    hide mari01 at default_transform
    show mari03 at right_transform
    voice "voice/m03.wav"
    m "竟然是这样羞耻的东西！"
    
    show seia at left_transform
    voice "voice/11.wav"
    s "对不起，我是坏孩子,QAQ。"
    voice "voice/m04.wav"
    m "不是的！不是的！"
    hide mari03 at right_transform
    show mari02 at right_transform
    voice "voice/m05.wav"
    m "圣娅是顺应自己的内心的欲望，没有伤害任何人..."
    voice "voice/m06.wav"
    m "一个人偷偷地欧娜尼,因为对他人的思念..."
    voice "voice/m07.wav"
    m "请不要把自己的欲望看得那么下作！"

    show seia03 at left_transform
    voice "voice/12.wav"
    s "真的吗，顺应自己的欲望是可以的？"
    hide mari02 at right_transform

    show mari at right_transform
    voice "voice/m08.wav"
    m "也不能完全说是可以的哦，来走廊吧，我给你讲个故事，你就知道怎么控制欲望了。"
    hide seia03 at left_transform with dissolve
    hide mari at right_transform with dissolve

    scene corridor
    with fade
    "此时真值下午，阳光正好，如果不是期末周，应该是个散心的好时候。"
    show seia at left_transform
    with dissolve    
    show mari at right_transform
    with dissolve
    voice "voice/m09.wav"
    m "我有两个不同的故事，圣娅酱想听什么的故事？"
    voice "voice/m10.wav"
    m "一个是爱上亲哥哥的妹妹的故事，一个是负心女和痴情男的故事..."

    menu:
        "选择是"
        "爱上亲哥哥的妹妹":
            $ mark = 2
        "负心女和复读男":
            $ mark = 1
    if mark == 2:
        jump hiyo
    elif mark == 1:
        jump zll

label hiyo:
    voice "voice/mh01.wav"
    m "这是一个幸福的故事呢。"
    hide mari at right_transform
    show mari01 at right_transform
    voice "voice/mh02.wav"
    m "有一对可怜的兄妹，早早失去了双亲，只能彼此相伴。"
    voice "voice/mh03.wav"
    m "哥哥虽然有点废柴，但是一直守护着妹妹，将她视为最重要的人，为了妹妹努力。"
    show hiyo
    voice "voice/mh04.wav"
    m "妹妹也为了家庭早早参加了工作，负责家务..."
    voice "voice/mh05.wav"
    m "于是乎，禁忌的爱恋诞生了。"
    voice "voice/mh06.wav"
    m "妹妹对自己的爱恋和欲望感到恶心，否定自己，拼命隐藏自己的欲望..."
    voice "voice/hi01.wav"
    s "兄妹相爱，似乎也是一种诅咒呢。"
    voice "voice/mh07.wav"
    m "虽然是这样，但是在一次大危机中，"
    voice "voice/mh08.wav"
    m "脆弱的妹妹终于面对了自己欲望，袒露了自己的心意。"
    voice "voice/mh09.wav"
    m "哥哥也意识到自己的感情，面对自己对妹妹的爱欲..."
    hide hiyo
    show hiyo1
    voice "voice/mh10.wav"
    m "最后，两个人在一起，走进了婚姻的殿堂，幸福生活了在一起..."
    voice "voice/hi02.wav"
    s "看来他们家似乎是要绝后了..."
    voice "voice/mh11.wav"
    m "只要两个人幸福也无所谓啦。"
    hide hiyo1
    "听到妃爱和哥哥甜蜜的爱情故事，获得鼓舞！"
    "学习热情 level-UP ！"
    hide seia at left_transform with dissolve
    hide mari01 at right_transform with dissolve

    stop music fadeout 1.0

    if flag == 1:
        jump normal
    elif flag == 2:
        jump good

label zll:
    hide mari at right_transform
    show mari01 at right_transform
    voice "voice/zm01.wav"
    m "这是一个令人心碎的故事呢..."
    voice "voice/zm02.wav"
    m "在一所高中，一个男孩爱上了隔壁班的女孩。"
    voice "voice/zm03.wav"
    m "他无法克制自己的欲望，天天下课就去隔壁班看她，想跟她说话。"
    voice "voice/zm04.wav"
    m "就算女孩不理他，他也拼命想和好。"
    voice "voice/zll01.wav"
    s "哇，有点恶心了..."
    hide mari01 at right_transform
    show mari02 at right_transform
    voice "voice/zm05.wav"
    m "可能是在恋爱花了太多时间，最后两个人在最终考试没考好..."
    voice "voice/zm06.wav"
    m "两人本来相约再读一年，结果女孩抛弃了男孩上大学去了。"
    voice "voice/zm07.wav"
    m "到了大学，女孩立马跟一个富人家孩子恋爱了，留下痛苦的男孩在高中..."
    voice "voice/zll02.wav"
    s "其实算是男孩看走眼了吧。"
    voice "voice/zm08.wav"
    m "总之，不让欲望泛滥是没错的。"

    "听了逆天男女的爱情狗血故事，圣娅感觉有被逆天到，感觉拼命学习还是不如有钱人。"
    "学习热情 level——DOWN ！"

    stop music fadeout 1.0

    if flag == 1:
        jump bad
    elif flag == 2:
        jump normal

label good:
    scene examroom
    show seia03 at default_transform with dissolve
    "今年圣娅学习热情高涨，期末考胸有成竹!"
    "期末考试课平均绩点4.0！"
    "达成好结局，恭喜恭喜喵！"
    return

label normal:
    scene examroom
    show seia at default_transform with dissolve
    "今年圣娅学习热情正常，期末考尽力发挥。"
    "期末考试课平均绩点3.0！"
    "达成普通结局，再接再厉喵！"
    return

label bad:
    scene examroom
    show seia01 at default_transform with dissolve
    "今年圣娅学习热情下降，期末考还想着欧娜尼..."
    "期末考试课平均绩点2.0！"
    "达成坏结局，再接再厉喵！"
    return