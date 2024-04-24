class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        props_string = ""
        for key in self.props.keys():
            props_string += f" {key}={self.props[key]}"
        return props_string


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    def to_html(self):
        if self.value == None:
            raise ValueError("No value provided to leaf node")
        if self.tag != None:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        return f"{self.value}"

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None ):
        super().__init__(tag=tag, props=props, children=children)
    def to_html(self):
        if self.children == None or len(self.children) == 0:
            raise ValueError("No children of parent node")
        children_html = []
        first_tag = []
        last_tag = []
        if self.tag != None:
            first_tag.append(f"<{self.tag}{self.props_to_html()}>")
            last_tag.append(f"</{self.tag}>")
        for child in self.children:
            children_html.append(child.to_html())
        html = first_tag + children_html + last_tag
        return "".join(html)