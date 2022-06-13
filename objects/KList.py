class KList:
    head = None

    def __init__(self):
        self.head = None

    def append(self, node):
        if (self.head is None):
            self.head = node
            return

        last = self.head
        while (last.after):
            last = last.after

        last.after = node
        node.before = last

    def prepend(self, node):
        if (self.head is None):
            self.head = node
            return

        node.after = self.head
        self.head.before = node
        self.head = node

    def beyond(self, select, node):
        if (self.head is None):
            self.head = node

        selected = self.head
        while (selected.data != select.data and selected is not None):
            selected = selected.after

        if (selected is None):
            self.append(node)

        node.after = selected.after
        node.before = selected
        selected.after.before = node
        selected.after = node

    def __str__(self):
        current = self.head
        while (current):
            print(str(current.data))
            current = current.after
        return ""