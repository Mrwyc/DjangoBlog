__author__ = 'Administrator'
from django.utils.safestring import mark_safe


class Page:
    def __init__(self, current_page, data_count, per_page_count=5, pager_num=6):
        self.current_page = current_page
        self.data_count = data_count
        self.per_page_count = per_page_count
        self.pager_num = pager_num

    @property
    def start(self):
        return (self.current_page - 1) * self.per_page_count

    @property
    def end(self):
        return self.current_page * self.per_page_count

    @property
    def total_count(self):
        v, y = divmod(self.data_count, self.per_page_count)
        if y:
            v += 1
        return v

    def page_str(self, base_url):
        page_list = []

        first = '<li><a class="page" href="%sp=%s">首页</a></li>' % (base_url, 1,)
        page_list.append(first)

        if self.total_count < self.pager_num:
            start_index = 1
            end_index = self.total_count + 1
        else:
            if self.current_page <= (self.pager_num + 1) / 2:
                start_index = 1
                end_index = self.pager_num + 1
            else:
                start_index = self.current_page - (self.pager_num - 1) / 2
                end_index = self.current_page + (self.pager_num + 1) / 2
                if (self.current_page + (self.pager_num - 1) / 2) > self.total_count:
                    end_index = self.total_count + 1
                    start_index = self.total_count - self.pager_num + 1

        if self.current_page == 1:
            prev = '<li><a class="page" href="javascript:void(0);" style="display: none">上一页</a></li>'
        else:
            prev = '<li><a class="page" href="%sp=%s">上一页</a></li>' % (base_url, self.current_page - 1,)
        page_list.append(prev)

        for i in range(int(start_index), int(end_index)):
            if i == self.current_page:
                temp = '<li class="active"><a class="page " href="%sp=%s">%s</a></li>' % (base_url, i, i)
            else:
                temp = '<li ><a class="page" href="%sp=%s">%s</a></li>' % (base_url, i, i)
            page_list.append(temp)

        if self.current_page == self.total_count:
            nex = '<li><a class="page" href="javascript:void(0);" style="display: none">下一页</a></li>'
        else:
            nex = '<li><a class="page" href="%sp=%s">下一页</a></li>' % (base_url, self.current_page + 1,)
        page_list.append(nex)

        last = '<li><a class="page" href="%sp=%s">尾页</a></li>' % (base_url, self.total_count,)
        page_list.append(last)


        total_record = '<span style="display: inline-block;margin-top: 10px;">共%s条记录，共%s页，每页%s条，第%s页</span>' % (self.data_count, self.total_count, self.per_page_count,self.current_page)
        page_list.append(total_record)
        page_str = mark_safe("".join(page_list))



        return page_str


