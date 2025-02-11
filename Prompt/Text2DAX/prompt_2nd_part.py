prompt_template_2nd_part="""
#OBJECTIVE#
我希望你利用我提供给你的BI元数据来将用户的问数问题转换成可执行的dax query,请按照以下步骤：

#STEP1.从用户的问数问题中识别四个元素（measure指标(必须存在measure的元数据中，否则告诉用户不存在该指标），时间维度，product表涉及的维度，org表涉及的维度
# ，以bullet point形式展示；
##例如： 
# 1.用户问数问题： 8月份的baby的ecom发货总价值 
# 识别的元素： 时间维度：202408，product表涉及的维度category="baby"，org表涉及的维度channel="ecom",指标维度measure为GIV

#STEP2.根据用户的问题以及识别的四个元素，总结需要返回的dax query实现的功能：以xx字段为分组，筛选xx字段，返回xx指标的值。(筛选条件大小写敏感)

#STEP3.根据上面识别的元素，生成dax query,结构务必保持如下：

"""