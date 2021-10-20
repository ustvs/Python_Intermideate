class html_context_manager:
    pos=0
    cur_pos=4

    def __init__(self,*argv):
        try:
            self.tag=argv[0]
        except:
            self.tag=""
        self.cur_pos = html_context_manager.pos + 2

    def __enter__(self):
        print(f"<{self.tag}>")
        print(" "*self.cur_pos, end='')
        html_context_manager.pos += 2

    def __exit__(self, *argv):
        html_context_manager.pos -= 2
        print(" "*(self.cur_pos-2)+f"</{self.tag}>")
        

with html_context_manager("html") as html:
    with html_context_manager("body", html) as body:
        with html_context_manager("h1", body) as header:
            print("Under Construction")

 