import scrapy
from ..items import ZzzsItem

class ZzzsSpider(scrapy.Spider):
    name = "zzzs"
    start_urls=["https://gaokao.chsi.com.cn/zzbm/mdgs/orgs.action?lx=1&a=a"]
    allowed_domains = ['gaokao.chsi.com.cn']

    def parse(self, response):
        '''
        首页提取学校和学校链接
        :param response:
        :return:
        '''
        schoolName=response.xpath("//div[@id='cnt1']//li[not(@title)]/a/text()").extract()  #学校名列表
        schoolLink=response.xpath("//div[@id='cnt1']//li[not(@title)]/a/@href").extract()   #学校链接列表
        for i in range(len(schoolName)):
            curUrl="https://gaokao.chsi.com.cn"+schoolLink[i]
            yield scrapy.Request(curUrl,meta={"schoolName":schoolName[i]},callback=self.getinfo)

    def getinfo(self,response):
        '''
        获取信息函数
        :param response:
        :return:
        '''
        table=response.xpath("//table[@id='YKTabCon2_10']")
        eachMsg=table.xpath("//tr[not(@class)]")
        for i in eachMsg:
            name=i.xpath("./td/text()").extract()[0]
            sex=i.xpath("./td/text()").extract()[1]
            middleSchool=i.xpath("./td/text()").extract()[2]
            province=i.xpath("./td/text()").extract()[3]
            item=ZzzsItem(gaoxiao=response.meta["schoolName"],
                          name=name,
                          sex=sex,
                          middleSchool=middleSchool,
                          province=province)
            yield item

        next_page=""
        for i in response.xpath("//a[@style='color:#06C;']"):
            if i.xpath("./text()").extract()[0]=="下一页>>":
                next_page="https://gaokao.chsi.com.cn"+i.xpath("./@href").extract()[0]
        if next_page:
            yield scrapy.Request(next_page,meta={"schoolName":response.meta["schoolName"]},callback=self.getinfo)