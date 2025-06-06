class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_str = ""
        if self.props is None:
            return ""
        
        for key, value in self.props.items():
            props_str += f" {key}=\"{value}\""

        return props_str
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"