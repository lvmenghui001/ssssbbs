
def add_node(tree_dic,comment):
    if comment.parent_comment is None:
        # 如果我是顶层，就放到这
        tree_dic[comment] = {}

    else:#循环当前整个dict，直到找到为止
        for k,v in tree_dic.items():
            if k == comment.parent_comment:#找到了你爸
                tree_dic[comment.parent_comment][comment] = {}
            else:#进入下一层继续找
                print("keeping going deeper...")
                add_node(v,comment)



def build_tree(comment_set):
    print(comment_set)
    tree_dic = {}
    for comment in comment_set:
        add_node(tree_dic,comment)

    print(tree_dic)
    return tree_dic

def render_tree_note(tree_dic,margin_val):
    html = ""
    for k, v in tree_dic.items():
        ele = "<div class='comment-note' style='margin-left:%spx'>"%margin_val + "<span style='color:red'>%s</span>"%k.user.name + ":"\
              + "<span style='margin-left:20px'>%s</span>"%k.comment \
              + "<span style='margin-left:20px;color:gray'>%s</span>" % k.date \
              + "<span comment-id='%s' style='margin-left: 20px' class='glyphicon glyphicon-comment add-comment' aria-hidden='true'></span>"%k.id \
              + "</div>"
        html += ele
        html += render_tree_note(v,margin_val+20)
    return html


def render_comment_tree(tree_dic):
    html = ""
    for k, v in tree_dic.items():
        ele = "<div class='root-comment'>" + "<span style='color:red;margin-left:20px'>%s</span>"%k.user.name + ":"\
              + "<span style='margin-left:20px'>%s</span>"%k.comment \
              + "<span style='margin-left:20px;color:gray'>%s</span>"%k.date \
              + "<span comment-id='%s' style='margin-left:20px' class='glyphicon glyphicon-comment add-comment' aria-hidden='true'></span>"%k.id\
              +"</div>"
        html += ele
        html += render_tree_note(v,20)
    return html


