# 페이지 교체 알고리즘을 직접 구현해보아요 with FIFO
class PageReplacementAlgorithmFIFO:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []
    
    def access_page(self, page):
        if page not in self.pages:
            if len(self.pages) >= self.capacity:
                self.pages.pop(0)
            self.pages.append(page)

    def print_status(self):
        print("현재 페이지 상태:", self.pages)


# 페이지 교체 알고리즘 테스트
page_replacement = PageReplacementAlgorithmFIFO(capacity=3)

# 초기 페이지 상태
page_replacement.print_status()

# 페이지에 접근
page_replacement.access_page(1)
page_replacement.print_status()

page_replacement.access_page(2)
page_replacement.print_status()

page_replacement.access_page(3)
page_replacement.print_status()

page_replacement.access_page(4)
page_replacement.print_status()

page_replacement.access_page(1)
page_replacement.print_status()

page_replacement.access_page(2)
page_replacement.print_status()